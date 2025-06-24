"""
Initial Data Creation Script

Creates initial data for development and testing.
"""

import asyncio
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import async_engine, AsyncSessionLocal
from app.core.security import get_password_hash
from app.models.models import User, Company, Job


async def create_initial_data():
    """Create initial data for development."""
    
    async with AsyncSessionLocal() as db:
        print("🌱 Creating initial data...")
        
        # Create admin user
        admin_user = User(
            email="admin@jobboard.com",
            username="admin",
            hashed_password=get_password_hash("admin123"),
            first_name="Admin",
            last_name="User",
            is_active=True,
            is_superuser=True,
        )
        db.add(admin_user)
        
        # Create test user
        test_user = User(
            email="user@example.com",
            username="testuser",
            hashed_password=get_password_hash("password123"),
            first_name="Test",
            last_name="User",
            title="Software Developer",
            location="San Francisco, CA",
            is_active=True,
        )
        db.add(test_user)
        
        # Create sample companies
        companies = [
            Company(
                name="TechCorp Inc.",
                description="Leading technology company",
                website="https://techcorp.com",
                location="San Francisco, CA",
                size="51-200",
                industry="Technology",
            ),
            Company(
                name="DataViz Solutions",
                description="Data visualization and analytics",
                website="https://dataviz.com", 
                location="New York, NY",
                size="11-50",
                industry="Data & Analytics",
            ),
            Company(
                name="CloudFirst Startup",
                description="Cloud-native solutions provider",
                website="https://cloudfirst.io",
                location="Remote",
                size="1-10",
                industry="Cloud Computing",
            ),
        ]
        
        for company in companies:
            db.add(company)
        
        await db.commit()
        
        # Refresh to get IDs
        await db.refresh(admin_user)
        await db.refresh(test_user)
        for company in companies:
            await db.refresh(company)
        
        # Create sample jobs
        jobs = [
            Job(
                title="Senior Python Developer",
                description="We're looking for a senior Python developer to join our backend team.",
                requirements="5+ years Python experience, FastAPI, PostgreSQL, Docker",
                benefits="Health insurance, 401k, flexible hours, remote work",
                location="San Francisco, CA",
                job_type="full-time",
                experience_level="senior",
                salary_min=120000,
                salary_max=160000,
                remote_allowed=True,
                company_id=companies[0].id,
                owner_id=admin_user.id,
            ),
            Job(
                title="Data Scientist",
                description="Join our data science team to build ML models and analytics.",
                requirements="PhD in data science, Python, SQL, ML frameworks",
                benefits="Competitive salary, stock options, learning budget",
                location="New York, NY",
                job_type="full-time", 
                experience_level="mid",
                salary_min=100000,
                salary_max=140000,
                remote_allowed=False,
                company_id=companies[1].id,
                owner_id=admin_user.id,
            ),
            Job(
                title="DevOps Engineer",
                description="Help us build and maintain our cloud infrastructure.",
                requirements="Kubernetes, AWS, Terraform, CI/CD, Python/Go",
                benefits="Equity, unlimited PTO, top-tier equipment",
                location="Remote",
                job_type="full-time",
                experience_level="mid",
                salary_min=90000,
                salary_max=130000,
                remote_allowed=True,
                company_id=companies[2].id,
                owner_id=test_user.id,
            ),
            Job(
                title="Junior Frontend Developer",
                description="Entry-level position for frontend development with React.",
                requirements="1+ years React, JavaScript, HTML/CSS, Git",
                benefits="Mentorship program, health insurance, growth opportunities",
                location="San Francisco, CA",
                job_type="full-time",
                experience_level="entry",
                salary_min=70000,
                salary_max=90000,
                remote_allowed=True,
                company_id=companies[0].id,
                owner_id=admin_user.id,
            ),
        ]
        
        for job in jobs:
            db.add(job)
        
        await db.commit()
        
        print("✅ Initial data created successfully!")
        print(f"👤 Admin user: admin@jobboard.com / admin123")
        print(f"👤 Test user: user@example.com / password123")
        print(f"🏢 Created {len(companies)} companies")
        print(f"💼 Created {len(jobs)} job postings")


if __name__ == "__main__":
    asyncio.run(create_initial_data())
