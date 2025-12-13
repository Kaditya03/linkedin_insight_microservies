
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.post import Post
from app.services.scraper_service import LinkedInScraper

class PostService:
    def __init__(self):
        self.scraper = LinkedInScraper()

    async def store_posts(self, page_id: int, db: AsyncSession):
        scraped_posts = await self.scraper.scrape_posts()

        for item in scraped_posts:
            post = Post(
                content=item["content"],
                likes=item["likes"],
                page_id=page_id
            )
            db.add(post)

        await db.commit()
