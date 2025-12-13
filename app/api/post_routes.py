from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_db
from app.services.post_service import PostService

router = APIRouter()
service = PostService()

@router.get("/pages/{page_id}/posts")
async def get_posts(page_id: str, db: AsyncSession = Depends(get_db)):
    posts = await service.get_posts_for_page(page_id, db)

    return [
        {
            "content": post.content,
            "likes": post.likes
        }
        for post in posts
    ]
