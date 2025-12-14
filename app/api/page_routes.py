from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
<<<<<<< HEAD
from sqlalchemy.future import select
=======
from sqlalchemy import select
>>>>>>> master

from app.core.database import get_db
from app.models.page import Page
from app.services.page_service import PageService
<<<<<<< HEAD

router = APIRouter()
service = PageService()


@router.get("/pages/{page_id}")
async def get_page(page_id: str, db: AsyncSession = Depends(get_db)):
    page = await service.get_page(page_id, db)
    return {
        "id": page.id,
        "name": page.name,
=======
from app.services.ai_summary_service import AISummaryService

router = APIRouter()

page_service = PageService()
ai_service = AISummaryService()


# -----------------------------
# GET PAGE BY PAGE ID
# -----------------------------
@router.get("/pages/{page_id}")
async def get_page(page_id: str, db: AsyncSession = Depends(get_db)):
    page = await page_service.get_page(page_id, db)

    return {
        "id": page.id,
        "name": page.name.strip(),
>>>>>>> master
        "industry": page.industry,
        "followers": page.followers_count,
        "description": page.description
    }


<<<<<<< HEAD
=======
# -----------------------------
# FILTER PAGES (MANDATORY)
# -----------------------------
>>>>>>> master
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
<<<<<<< HEAD
    pages = result.scalars().all()
=======
>>>>>>> master

    return [
        {
            "id": p.id,
            "name": p.name.strip(),
            "industry": p.industry,
            "followers": p.followers_count
        }
<<<<<<< HEAD
        for p in pages
    ]
=======
        for p in result.scalars().all()
    ]


# -----------------------------
# AI SUMMARY (BONUS)
# -----------------------------
@router.get("/pages/{page_id}/summary")
async def get_page_summary(page_id: str, db: AsyncSession = Depends(get_db)):
    page = await page_service.get_page(page_id, db)

    summary = await ai_service.generate_summary({
        "name": page.name.strip(),
        "industry": page.industry,
        "followers": page.followers_count,
        "description": page.description
    })

    return {
        "page": page.name.strip(),
        "summary": summary
    }
>>>>>>> master
