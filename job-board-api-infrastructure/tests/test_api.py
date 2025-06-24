"""
Basic API Tests

Test basic functionality and health checks.
"""

import pytest
from httpx import AsyncClient


class TestBasicAPI:
    """Test basic API functionality."""
    
    async def test_health_check(self, client: AsyncClient):
        """Test health check endpoint."""
        response = await client.get("/health")
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "healthy"
        assert "service" in data
        assert "version" in data
    
    async def test_root_endpoint(self, client: AsyncClient):
        """Test root endpoint."""
        response = await client.get("/")
        assert response.status_code == 200
        data = response.json()
        assert "message" in data
        assert "docs" in data
        assert "health" in data
    
    async def test_docs_endpoints(self, client: AsyncClient):
        """Test documentation endpoints."""
        # These should be available in development
        docs_response = await client.get("/docs")
        assert docs_response.status_code == 200
        
        redoc_response = await client.get("/redoc")
        assert redoc_response.status_code == 200
        
        openapi_response = await client.get("/openapi.json")
        assert openapi_response.status_code == 200


class TestAuthentication:
    """Test authentication endpoints."""
    
    async def test_register_user(self, client: AsyncClient):
        """Test user registration."""
        user_data = {
            "email": "newuser@example.com",
            "username": "newuser",
            "password": "password123",
            "first_name": "New",
            "last_name": "User"
        }
        response = await client.post("/api/v1/auth/register", json=user_data)
        assert response.status_code == 201
        data = response.json()
        assert data["email"] == user_data["email"]
        assert data["username"] == user_data["username"]
        assert "id" in data
        assert "hashed_password" not in data  # Should not return password
    
    async def test_login_user(self, client: AsyncClient, test_user):
        """Test user login."""
        login_data = {
            "username": test_user.username,
            "password": "testpassword"
        }
        response = await client.post("/api/v1/auth/login", data=login_data)
        assert response.status_code == 200
        data = response.json()
        assert "access_token" in data
        assert data["token_type"] == "bearer"
    
    async def test_get_current_user(self, client: AsyncClient, auth_headers, test_user):
        """Test getting current user info."""
        response = await client.get("/api/v1/auth/me", headers=auth_headers)
        assert response.status_code == 200
        data = response.json()
        assert data["email"] == test_user.email
        assert data["username"] == test_user.username
    
    async def test_unauthorized_access(self, client: AsyncClient):
        """Test accessing protected endpoint without auth."""
        response = await client.get("/api/v1/auth/me")
        assert response.status_code == 401


class TestCompanies:
    """Test company endpoints."""
    
    async def test_create_company(self, client: AsyncClient, auth_headers):
        """Test creating a company."""
        company_data = {
            "name": "Test Company",
            "description": "A test company",
            "website": "https://testcompany.com",
            "location": "San Francisco, CA",
            "size": "11-50",
            "industry": "Technology"
        }
        response = await client.post(
            "/api/v1/companies/", 
            json=company_data, 
            headers=auth_headers
        )
        assert response.status_code == 201
        data = response.json()
        assert data["name"] == company_data["name"]
        assert "id" in data
    
    async def test_get_companies(self, client: AsyncClient):
        """Test getting companies list."""
        response = await client.get("/api/v1/companies/")
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)


if __name__ == "__main__":
    pytest.main([__file__])
