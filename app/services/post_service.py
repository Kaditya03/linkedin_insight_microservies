from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.models.post import Post
from app.services.scraper_service import LinkedInScraper

class PostService:

    def __init__(self):
        self.scraper = LinkedInScraper()

    async def create_posts_for_page(self, page_id: int, db: AsyncSession):
        scraped_posts = await self.scraper.scrape_posts()

        posts = []
        for item in scraped_posts:
            post = Post(
                content=item["content"],
                likes=item["likes"],
                page_id=page_id
            )
            db.add(post)
            posts.append(post)

        await db.commit()
        return posts

    async def get_posts_by_page(self, page_id: int, db: AsyncSession):
        result = await db.execute(
            select(Post).where(Post.page_id == page_id)
        )
        return result.scalars().all()
