

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
import json

from app.models.page import Page
from app.services.scraper_service import LinkedInScraper
from app.core.cache import redis_client  # async redis client


class PageService:
    def __init__(self):
        self.scraper = LinkedInScraper()

    async def get_page(self, page_id: str, db: AsyncSession) -> Page:
        cache_key = f"page:{page_id}"

        # -------------------------
        # 1. CHECK CACHE
        # -------------------------
        cached = await redis_client.get(cache_key)
        if cached:
            data = json.loads(cached)
            return Page(**data)  # 🔥 convert back to ORM object

        # -------------------------
        # 2. CHECK DATABASE
        # -------------------------
        result = await db.execute(
            select(Page).where(Page.linkedin_page_id == page_id)
        )
        page = result.scalar_one_or_none()

        if page:
            await redis_client.setex(
                cache_key,
                300,
                json.dumps({
                    "id": page.id,
                    "linkedin_page_id": page.linkedin_page_id,
                    "name": page.name,
                    "industry": page.industry,
                    "followers_count": page.followers_count,
                    "description": page.description
                })
            )
            return page

        # -------------------------
        # 3. SCRAPE & SAVE
        # -------------------------
        data = await self.scraper.scrape_page(page_id)

        page = Page(**data)
        db.add(page)
        await db.commit()
        await db.refresh(page)

        await redis_client.setex(
            cache_key,
            300,
            json.dumps({
                "id": page.id,
                "linkedin_page_id": page.linkedin_page_id,
                "name": page.name,
                "industry": page.industry,
                "followers_count": page.followers_count,
                "description": page.description
            })
        )

        return page
