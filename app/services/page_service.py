from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.page import Page
from app.services.scraper_service import LinkedInScraper  # ✅ FIX

class PageService:

    def __init__(self):
        self.scraper = LinkedInScraper()

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

        return page
