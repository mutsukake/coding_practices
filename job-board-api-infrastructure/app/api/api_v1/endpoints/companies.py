"""
Company Management Endpoints

Company creation, listing, and management.
"""

from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.core.database import get_db
from app.core.security import get_current_active_user
from app.models.models import Company, User
from app.schemas.schemas import Company as CompanySchema, CompanyCreate, CompanyUpdate

router = APIRouter()

@router.get("/", response_model=List[CompanySchema])
async def get_companies(
    skip: int = 0,
    limit: int = 100,
    db: AsyncSession = Depends(get_db)
) -> Any:
    """Get all companies."""
    
    result = await db.execute(select(Company).offset(skip).limit(limit))
    companies = result.scalars().all()
    return companies

@router.post("/", response_model=CompanySchema, status_code=status.HTTP_201_CREATED)
async def create_company(
    company_data: CompanyCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
) -> Any:
    """Create a new company."""
    
    # Check if company with same name exists
    result = await db.execute(select(Company).where(Company.name == company_data.name))
    existing_company = result.scalar_one_or_none()
    
    if existing_company:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Company with this name already exists"
        )
    
    # Create new company
    db_company = Company(**company_data.dict())
    db.add(db_company)
    await db.commit()
    await db.refresh(db_company)
    
    return db_company

@router.get("/{company_id}", response_model=CompanySchema)
async def get_company(
    company_id: int,
    db: AsyncSession = Depends(get_db)
) -> Any:
    """Get company by ID."""
    
    result = await db.execute(select(Company).where(Company.id == company_id))
    company = result.scalar_one_or_none()
    
    if not company:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Company not found"
        )
    
    return company

@router.put("/{company_id}", response_model=CompanySchema)
async def update_company(
    company_id: int,
    company_update: CompanyUpdate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
) -> Any:
    """Update company information."""
    
    result = await db.execute(select(Company).where(Company.id == company_id))
    company = result.scalar_one_or_none()
    
    if not company:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Company not found"
        )
    
    # Update company fields
    for field, value in company_update.dict(exclude_unset=True).items():
        setattr(company, field, value)
    
    await db.commit()
    await db.refresh(company)
    
    return company

@router.delete("/{company_id}")
async def delete_company(
    company_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
) -> Any:
    """Delete company."""
    
    result = await db.execute(select(Company).where(Company.id == company_id))
    company = result.scalar_one_or_none()
    
    if not company:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Company not found"
        )
    
    await db.delete(company)
    await db.commit()
    
    return {"message": "Company deleted successfully"}

@router.get("/search/", response_model=List[CompanySchema])
async def search_companies(
    q: str,
    skip: int = 0,
    limit: int = 20,
    db: AsyncSession = Depends(get_db)
) -> Any:
    """Search companies by name or industry."""
    
    search_term = f"%{q}%"
    result = await db.execute(
        select(Company).where(
            (Company.name.ilike(search_term)) |
            (Company.industry.ilike(search_term))
        ).offset(skip).limit(limit)
    )
    companies = result.scalars().all()
    return companies
