"""
Job Management Endpoints

Job posting creation, listing, search, and management.
"""

from typing import Any, List, Optional

from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import selectinload

from app.core.database import get_db
from app.core.security import get_current_active_user
from app.models.models import Job, User, Company
from app.schemas.schemas import Job as JobSchema, JobCreate, JobList, JobUpdate

router = APIRouter()

@router.get("/", response_model=List[JobList])
async def get_jobs(
    skip: int = 0,
    limit: int = 20,
    location: Optional[str] = None,
    job_type: Optional[str] = None,
    experience_level: Optional[str] = None,
    remote_allowed: Optional[bool] = None,
    company_id: Optional[int] = None,
    db: AsyncSession = Depends(get_db)
) -> Any:
    """Get all active jobs with filtering."""
    
    query = select(Job).options(selectinload(Job.company)).where(Job.is_active == True)
    
    # Apply filters
    if location:
        query = query.where(Job.location.ilike(f"%{location}%"))
    if job_type:
        query = query.where(Job.job_type == job_type)
    if experience_level:
        query = query.where(Job.experience_level == experience_level)
    if remote_allowed is not None:
        query = query.where(Job.remote_allowed == remote_allowed)
    if company_id:
        query = query.where(Job.company_id == company_id)
    
    query = query.offset(skip).limit(limit).order_by(Job.created_at.desc())
    
    result = await db.execute(query)
    jobs = result.scalars().all()
    return jobs

@router.post("/", response_model=JobSchema, status_code=status.HTTP_201_CREATED)
async def create_job(
    job_data: JobCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
) -> Any:
    """Create a new job posting."""
    
    # Verify company exists
    result = await db.execute(select(Company).where(Company.id == job_data.company_id))
    company = result.scalar_one_or_none()
    
    if not company:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Company not found"
        )
    
    # Create new job
    job_dict = job_data.dict()
    job_dict["owner_id"] = current_user.id
    
    db_job = Job(**job_dict)
    db.add(db_job)
    await db.commit()
    await db.refresh(db_job, ["company"])
    
    return db_job

@router.get("/{job_id}", response_model=JobSchema)
async def get_job(
    job_id: int,
    db: AsyncSession = Depends(get_db)
) -> Any:
    """Get job by ID."""
    
    result = await db.execute(
        select(Job).options(selectinload(Job.company)).where(Job.id == job_id)
    )
    job = result.scalar_one_or_none()
    
    if not job:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Job not found"
        )
    
    return job

@router.put("/{job_id}", response_model=JobSchema)
async def update_job(
    job_id: int,
    job_update: JobUpdate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
) -> Any:
    """Update job posting."""
    
    result = await db.execute(
        select(Job).options(selectinload(Job.company)).where(Job.id == job_id)
    )
    job = result.scalar_one_or_none()
    
    if not job:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Job not found"
        )
    
    # Check ownership or admin
    if job.owner_id != current_user.id and not current_user.is_superuser:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not enough permissions"
        )
    
    # Update job fields
    for field, value in job_update.dict(exclude_unset=True).items():
        setattr(job, field, value)
    
    await db.commit()
    await db.refresh(job)
    
    return job

@router.delete("/{job_id}")
async def delete_job(
    job_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
) -> Any:
    """Delete job posting."""
    
    result = await db.execute(select(Job).where(Job.id == job_id))
    job = result.scalar_one_or_none()
    
    if not job:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Job not found"
        )
    
    # Check ownership or admin
    if job.owner_id != current_user.id and not current_user.is_superuser:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not enough permissions"
        )
    
    await db.delete(job)
    await db.commit()
    
    return {"message": "Job deleted successfully"}

@router.get("/search/", response_model=List[JobList])
async def search_jobs(
    q: str = Query(..., description="Search query"),
    skip: int = 0,
    limit: int = 20,
    location: Optional[str] = None,
    job_type: Optional[str] = None,
    experience_level: Optional[str] = None,
    remote_allowed: Optional[bool] = None,
    db: AsyncSession = Depends(get_db)
) -> Any:
    """Search jobs by title, description, or requirements."""
    
    search_term = f"%{q}%"
    query = select(Job).options(selectinload(Job.company)).where(
        Job.is_active == True
    ).where(
        (Job.title.ilike(search_term)) |
        (Job.description.ilike(search_term)) |
        (Job.requirements.ilike(search_term))
    )
    
    # Apply additional filters
    if location:
        query = query.where(Job.location.ilike(f"%{location}%"))
    if job_type:
        query = query.where(Job.job_type == job_type)
    if experience_level:
        query = query.where(Job.experience_level == experience_level)
    if remote_allowed is not None:
        query = query.where(Job.remote_allowed == remote_allowed)
    
    query = query.offset(skip).limit(limit).order_by(Job.created_at.desc())
    
    result = await db.execute(query)
    jobs = result.scalars().all()
    return jobs

@router.get("/my/", response_model=List[JobSchema])
async def get_my_jobs(
    skip: int = 0,
    limit: int = 20,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
) -> Any:
    """Get current user's job postings."""
    
    result = await db.execute(
        select(Job).options(selectinload(Job.company))
        .where(Job.owner_id == current_user.id)
        .offset(skip).limit(limit)
        .order_by(Job.created_at.desc())
    )
    jobs = result.scalars().all()
    return jobs
