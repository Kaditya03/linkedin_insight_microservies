from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.post import Post
from app.models.page import Page

class PostService:

    async def get_posts_for_page(self, page_id: str, db: AsyncSession):
        result = await db.execute(
            select(Page).where(Page.linkedin_page_id == page_id)
        )
        page = result.scalar_one_or_none()

        if not page:
            return []

        result = await db.execute(
            select(Post).where(Post.page_id == page.id)
        )
        return result.scalars().all()
