from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.services.page_service import PageService

router = APIRouter()   # 👈 THIS LINE IS CRITICAL

page_service = PageService()

@router.get("/pages/{page_id}")
async def get_page(page_id: str, db: AsyncSession = Depends(get_db)):
    page = await page_service.get_page(page_id, db)

    return {
        "name": page.name,
        "industry": page.industry,
        "followers": page.followers_count,
        "description": page.description
    }
