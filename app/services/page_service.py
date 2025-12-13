from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.models.page import Page
from app.services.scraper_service import LinkedInScraper
from app.services.post_service import PostService

class PageService:

    def __init__(self):
        self.scraper = LinkedInScraper()
        self.post_service = PostService()

    async def get_page(self, page_id: str, db: AsyncSession):
        result = await db.execute(
            select(Page).where(Page.linkedin_page_id == page_id)
        )
        page = result.scalar_one_or_none()

        if page:
            return page

        data = await self.scraper.scrape_page(page_id)
        page = Page(**data)

        db.add(page)
        await db.commit()
        await db.refresh(page)

        # 🔹 STORE POSTS AFTER PAGE IS CREATED
        await self.post_service.create_posts_for_page(page.id, db)

        return page
