"""
Pydantic Schemas

Request/Response models for API serialization.
"""

from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, EmailStr, validator

# Base schemas
class BaseSchema(BaseModel):
    """Base schema with common configuration."""
    
    class Config:
        orm_mode = True
        validate_assignment = True

# User schemas
class UserBase(BaseModel):
    """Base user schema."""
    email: EmailStr
    username: str
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    title: Optional[str] = None
    bio: Optional[str] = None
    location: Optional[str] = None
    website: Optional[str] = None

class UserCreate(UserBase):
    """Schema for user creation."""
    password: str
    
    @validator("password")
    def validate_password(cls, v):
        if len(v) < 8:
            raise ValueError("Password must be at least 8 characters long")
        return v

class UserUpdate(BaseModel):
    """Schema for user updates."""
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    title: Optional[str] = None
    bio: Optional[str] = None
    location: Optional[str] = None
    website: Optional[str] = None

class UserInDB(UserBase):
    """User schema as stored in database."""
    id: int
    is_active: bool
    is_superuser: bool
    resume_filename: Optional[str] = None
    created_at: datetime
    updated_at: Optional[datetime] = None
    
    class Config:
        orm_mode = True

class User(UserInDB):
    """Public user schema (without sensitive data)."""
    pass

# Company schemas
class CompanyBase(BaseModel):
    """Base company schema."""
    name: str
    description: Optional[str] = None
    website: Optional[str] = None
    location: Optional[str] = None
    size: Optional[str] = None
    industry: Optional[str] = None

class CompanyCreate(CompanyBase):
    """Schema for company creation."""
    pass

class CompanyUpdate(BaseModel):
    """Schema for company updates."""
    name: Optional[str] = None
    description: Optional[str] = None
    website: Optional[str] = None
    location: Optional[str] = None
    size: Optional[str] = None
    industry: Optional[str] = None

class Company(CompanyBase):
    """Company schema with ID and timestamps."""
    id: int
    logo_url: Optional[str] = None
    created_at: datetime
    updated_at: Optional[datetime] = None
    
    class Config:
        orm_mode = True

# Job schemas
class JobBase(BaseModel):
    """Base job schema."""
    title: str
    description: str
    requirements: Optional[str] = None
    benefits: Optional[str] = None
    location: Optional[str] = None
    job_type: str
    experience_level: Optional[str] = None
    salary_min: Optional[float] = None
    salary_max: Optional[float] = None
    salary_currency: str = "USD"
    remote_allowed: bool = False

class JobCreate(JobBase):
    """Schema for job creation."""
    company_id: int
    expires_at: Optional[datetime] = None

class JobUpdate(BaseModel):
    """Schema for job updates."""
    title: Optional[str] = None
    description: Optional[str] = None
    requirements: Optional[str] = None
    benefits: Optional[str] = None
    location: Optional[str] = None
    job_type: Optional[str] = None
    experience_level: Optional[str] = None
    salary_min: Optional[float] = None
    salary_max: Optional[float] = None
    remote_allowed: Optional[bool] = None
    is_active: Optional[bool] = None
    expires_at: Optional[datetime] = None

class Job(JobBase):
    """Job schema with relationships."""
    id: int
    is_active: bool
    owner_id: int
    company: Company
    expires_at: Optional[datetime] = None
    created_at: datetime
    updated_at: Optional[datetime] = None
    
    class Config:
        orm_mode = True

class JobList(BaseModel):
    """Schema for job listings."""
    id: int
    title: str
    company: Company
    location: Optional[str] = None
    job_type: str
    experience_level: Optional[str] = None
    salary_min: Optional[float] = None
    salary_max: Optional[float] = None
    remote_allowed: bool
    created_at: datetime
    
    class Config:
        orm_mode = True

# Application schemas
class ApplicationBase(BaseModel):
    """Base application schema."""
    cover_letter: Optional[str] = None

class ApplicationCreate(ApplicationBase):
    """Schema for application creation."""
    job_id: int

class ApplicationUpdate(BaseModel):
    """Schema for application updates."""
    cover_letter: Optional[str] = None
    status: Optional[str] = None

class Application(ApplicationBase):
    """Application schema with relationships."""
    id: int
    job_id: int
    applicant_id: int
    status: str
    resume_filename: Optional[str] = None
    created_at: datetime
    updated_at: Optional[datetime] = None
    
    class Config:
        orm_mode = True

# Pagination schemas
class PaginationParams(BaseModel):
    """Pagination parameters."""
    page: int = 1
    size: int = 20
    
    @validator("page")
    def validate_page(cls, v):
        if v < 1:
            raise ValueError("Page must be >= 1")
        return v
    
    @validator("size")
    def validate_size(cls, v):
        if v < 1 or v > 100:
            raise ValueError("Size must be between 1 and 100")
        return v

class PaginatedResponse(BaseModel):
    """Generic paginated response."""
    items: List[BaseModel]
    total: int
    page: int
    size: int
    pages: int

# Authentication schemas
class Token(BaseModel):
    """JWT token response."""
    access_token: str
    token_type: str = "bearer"

class TokenData(BaseModel):
    """Token payload data."""
    username: Optional[str] = None

class LoginRequest(BaseModel):
    """Login request schema."""
    username: str
    password: str
