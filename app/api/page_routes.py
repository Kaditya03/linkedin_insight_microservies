from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.core.database import get_db
from app.models.page import Page
from app.services.page_service import PageService

router = APIRouter()
service = PageService()


@router.get("/pages/{page_id}")
async def get_page(page_id: str, db: AsyncSession = Depends(get_db)):
    page = await service.get_page(page_id, db)
    return {
        "name": page.name.strip(),
        "industry": page.industry,
        "followers": page.followers_count,
        "description": page.description
    }


@router.get("/pages")
async def filter_pages(
    min_followers: int = 0,
    max_followers: int = 10_000_000,
    industry: str | None = None,
    db: AsyncSession = Depends(get_db)
):
    query = select(Page).where(
        Page.followers_count.between(min_followers, max_followers)
    )

    if industry:
        query = query.where(Page.industry.ilike(f"%{industry}%"))

    result = await db.execute(query)

    pages = result.scalars().all()

    return [
        {
            "id": p.id,
            "name": p.name.strip(),
            "industry": p.industry,
            "followers": p.followers_count
        }
        for p in pages
    ]
