from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.models.page import Page
from app.services.post_service import PostService
from sqlalchemy.future import select

router = APIRouter()
service = PostService()

@router.get("/pages/{page_id}/posts")
async def get_posts(page_id: str, db: AsyncSession = Depends(get_db)):
    result = await db.execute(
        select(Page).where(Page.linkedin_page_id == page_id)
    )
    page = result.scalar_one_or_none()

    if not page:
        return []

    posts = await service.get_posts_by_page(page.id, db)

    return [
        {"content": post.content, "likes": post.likes}
        for post in posts
    ]
