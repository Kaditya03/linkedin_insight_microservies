from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.page import Page
from app.models.post import Post
from app.services.scraper_service import LinkedInScraper


class PageService:
    def __init__(self):
        self.scraper = LinkedInScraper()

    async def get_page(self, page_id: str, db: AsyncSession):
        page_id = page_id.strip().lower()

        # Check if page already exists
        result = await db.execute(
            select(Page).where(Page.linkedin_page_id == page_id)
        )
        page = result.scalar_one_or_none()

        if page:
            return page

        # Scrape page data
        page_data = await self.scraper.scrape_page(page_id)
        page = Page(**page_data)

        db.add(page)
        await db.commit()
        await db.refresh(page)

        # Scrape and save posts
        posts = await self.scraper.scrape_posts(page_id)

        for post in posts:
            db.add(
                Post(
                    content=post.get("content"),
                    likes=post.get("likes", 0),
                    comments=post.get("comments", 0),
                    page_id=page.id
                )
            )

        await db.commit()
        return page
