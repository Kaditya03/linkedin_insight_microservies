from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.core.database import get_db
from app.models.page import Page
from app.models.post import Post

router = APIRouter()


@router.get("/pages/{page_id}/posts")
async def get_posts(page_id: str, db: AsyncSession = Depends(get_db)):
    result = await db.execute(
        select(Page).where(Page.linkedin_page_id == page_id)
    )
    page = result.scalar_one_or_none()

    if not page:
        return []

    result = await db.execute(
        select(Post).where(Post.page_id == page.id)
    )
    posts = result.scalars().all()

    return [
        {
            "content": post.content,
            "likes": post.likes
        }
        for post in posts
    ]
