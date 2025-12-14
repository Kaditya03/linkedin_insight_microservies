from sqlalchemy.future import select
<<<<<<< HEAD
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.page import Page
from app.models.post import Post
from app.services.scraper_service import LinkedInScraper

class PageService:

    def __init__(self):
        self.scraper = LinkedInScraper()

    async def get_page(self, page_id: str, db: AsyncSession):
=======
from app.models.page import Page
from app.services.scraper_service import LinkedInScraper

class PageService:
    def __init__(self):
        self.scraper = LinkedInScraper()

    async def get_page(self, page_id: str, db):
        # 1️⃣ Always check DB first
>>>>>>> master
        result = await db.execute(
            select(Page).where(Page.linkedin_page_id == page_id)
        )
        page = result.scalar_one_or_none()

        if page:
<<<<<<< HEAD
            return page

        # 1️⃣ Scrape page details
        page_data = await self.scraper.scrape_page(page_id)

        page = Page(**page_data)
=======
            return page  # ✅ ORM object

        # 2️⃣ If not found, scrape
        data = await self.scraper.scrape_page(page_id)

        page = Page(
            linkedin_page_id=data["linkedin_page_id"],
            name=data["name"],
            url=data["url"],
            industry=data["industry"],
            followers_count=data["followers_count"],
            description=data["description"]
        )

>>>>>>> master
        db.add(page)
        await db.commit()
        await db.refresh(page)

<<<<<<< HEAD
        # 2️⃣ Scrape & store posts (MANDATORY)
        posts = await self.scraper.scrape_posts()

        for post in posts:
            db.add(
                Post(
                    content=post["content"],
                    likes=post["likes"],
                    page_id=page.id
                )
            )

        await db.commit()

        return page
=======
        return page  # ✅ ORM object only
>>>>>>> master
