from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.core.database import get_db
from app.models.page import Page
from app.models.post import Post

router = APIRouter()

@router.get("/pages/{page_id}/posts")
async def get_page_posts(
    page_id: str,
    page: int = 1,
    limit: int = 10,
    db: AsyncSession = Depends(get_db)
):
    # 1️⃣ Find page by LinkedIn page id
    result = await db.execute(
        select(Page).where(Page.linkedin_page_id == page_id)
    )
    page_obj = result.scalar_one_or_none()

    if not page_obj:
        raise HTTPException(status_code=404, detail="Page not found")

    # 2️⃣ Pagination
    offset = (page - 1) * limit

    posts_result = await db.execute(
        select(Post)
        .where(Post.page_id == page_obj.id)
        .offset(offset)
        .limit(limit)
    )

    posts = posts_result.scalars().all()

    return [
        {
            "content": post.content,
            "likes": post.likes
        }
        for post in posts
    ]
