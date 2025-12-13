class LinkedInScraper:
    """
    This class ONLY scrapes data.
    No DB logic here.
    """

    async def scrape_page(self, page_id: str) -> dict:
        return {
            "linkedin_page_id": page_id,
            "name": page_id.capitalize(),
            "url": f"https://www.linkedin.com/company/{page_id}/",
            "industry": "Technology",
            "followers_count": 25000,
            "description": "Sample LinkedIn company page"
        }

    async def scrape_posts(self):
        return [
            {"content": "We are hiring!", "likes": 120},
            {"content": "New product launch", "likes": 300}
        ]
