from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
<<<<<<< HEAD
from sqlalchemy.future import select
=======
from sqlalchemy import select
>>>>>>> master

from app.core.database import get_db
from app.models.post import Post
from app.models.page import Page

<<<<<<< HEAD
router = APIRouter()   # ✅ MUST EXIST


@router.get("/pages/{page_id}/posts")
async def get_page_posts(
    page_id: str,
    page: int = 1,
    limit: int = 10,
    db: AsyncSession = Depends(get_db)
):
    # find page
    result = await db.execute(
        select(Page).where(Page.linkedin_page_id == page_id)
    )
    page_obj = result.scalar_one_or_none()

    if not page_obj:
        return []

    offset = (page - 1) * limit

    posts_result = await db.execute(
        select(Post)
        .where(Post.page_id == page_obj.id)
        .offset(offset)
        .limit(limit)
    )

    posts = posts_result.scalars().all()
=======
router = APIRouter()

@router.get("/pages/{page_id}/posts")
async def get_posts(page_id: str, db: AsyncSession = Depends(get_db)):
    result = await db.execute(
        select(Post)
        .join(Page)
        .where(Page.linkedin_page_id == page_id)
        .order_by(Post.id.desc())
    )

    posts = result.scalars().all()
>>>>>>> master

    return [
        {
            "content": post.content,
            "likes": post.likes
        }
        for post in posts
    ]
