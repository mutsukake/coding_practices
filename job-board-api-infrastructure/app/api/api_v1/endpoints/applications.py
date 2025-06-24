"""
Job Application Endpoints

Job application management for applicants and employers.
"""

from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import selectinload

from app.core.database import get_db
from app.core.security import get_current_active_user
from app.models.models import Application, Job, User
from app.schemas.schemas import Application as ApplicationSchema, ApplicationCreate, ApplicationUpdate

router = APIRouter()

@router.get("/", response_model=List[ApplicationSchema])
async def get_applications(
    job_id: int = None,
    skip: int = 0,
    limit: int = 20,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
) -> Any:
    """Get applications. Job owners see all applications for their jobs."""
    
    if job_id:
        # Check if user owns the job
        result = await db.execute(select(Job).where(Job.id == job_id))
        job = result.scalar_one_or_none()
        
        if not job:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Job not found"
            )
        
        if job.owner_id != current_user.id and not current_user.is_superuser:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Not enough permissions"
            )
        
        # Get applications for this job
        result = await db.execute(
            select(Application)
            .where(Application.job_id == job_id)
            .offset(skip).limit(limit)
            .order_by(Application.created_at.desc())
        )
    else:
        # Get user's own applications
        result = await db.execute(
            select(Application)
            .where(Application.applicant_id == current_user.id)
            .offset(skip).limit(limit)
            .order_by(Application.created_at.desc())
        )
    
    applications = result.scalars().all()
    return applications

@router.post("/", response_model=ApplicationSchema, status_code=status.HTTP_201_CREATED)
async def create_application(
    application_data: ApplicationCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
) -> Any:
    """Apply for a job."""
    
    # Check if job exists and is active
    result = await db.execute(select(Job).where(Job.id == application_data.job_id))
    job = result.scalar_one_or_none()
    
    if not job:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Job not found"
        )
    
    if not job.is_active:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Job is no longer active"
        )
    
    # Check if user already applied
    result = await db.execute(
        select(Application).where(
            (Application.job_id == application_data.job_id) &
            (Application.applicant_id == current_user.id)
        )
    )
    existing_application = result.scalar_one_or_none()
    
    if existing_application:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="You have already applied for this job"
        )
    
    # Create application
    application_dict = application_data.dict()
    application_dict["applicant_id"] = current_user.id
    
    db_application = Application(**application_dict)
    db.add(db_application)
    await db.commit()
    await db.refresh(db_application)
    
    return db_application

@router.get("/{application_id}", response_model=ApplicationSchema)
async def get_application(
    application_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
) -> Any:
    """Get application by ID."""
    
    result = await db.execute(
        select(Application)
        .options(selectinload(Application.job))
        .where(Application.id == application_id)
    )
    application = result.scalar_one_or_none()
    
    if not application:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Application not found"
        )
    
    # Check if user is applicant or job owner
    is_applicant = application.applicant_id == current_user.id
    is_job_owner = application.job.owner_id == current_user.id
    
    if not (is_applicant or is_job_owner or current_user.is_superuser):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not enough permissions"
        )
    
    return application

@router.put("/{application_id}", response_model=ApplicationSchema)
async def update_application(
    application_id: int,
    application_update: ApplicationUpdate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
) -> Any:
    """Update application (applicant can update cover letter, job owner can update status)."""
    
    result = await db.execute(
        select(Application)
        .options(selectinload(Application.job))
        .where(Application.id == application_id)
    )
    application = result.scalar_one_or_none()
    
    if not application:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Application not found"
        )
    
    is_applicant = application.applicant_id == current_user.id
    is_job_owner = application.job.owner_id == current_user.id
    
    if not (is_applicant or is_job_owner or current_user.is_superuser):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not enough permissions"
        )
    
    # Applicants can only update cover letter
    # Job owners can update status
    update_data = application_update.dict(exclude_unset=True)
    
    if is_applicant and not is_job_owner:
        # Remove status from update if user is only applicant
        update_data.pop("status", None)
    
    # Update application fields
    for field, value in update_data.items():
        setattr(application, field, value)
    
    await db.commit()
    await db.refresh(application)
    
    return application

@router.delete("/{application_id}")
async def delete_application(
    application_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
) -> Any:
    """Delete application (withdraw application)."""
    
    result = await db.execute(select(Application).where(Application.id == application_id))
    application = result.scalar_one_or_none()
    
    if not application:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Application not found"
        )
    
    # Only applicant or admin can delete
    if application.applicant_id != current_user.id and not current_user.is_superuser:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not enough permissions"
        )
    
    await db.delete(application)
    await db.commit()
    
    return {"message": "Application withdrawn successfully"}
