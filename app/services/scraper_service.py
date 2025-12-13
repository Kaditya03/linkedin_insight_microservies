class LinkedInScraper:
    """
    Responsible only for fetching data from LinkedIn.
    No database logic here.
    """

    async def scrape_page(self, page_id: str) -> dict:
        # Placeholder logic (safe for demo)
        return {
            "linkedin_page_id": page_id,
            "name": page_id.capitalize(),
            "url": f"https://www.linkedin.com/company/{page_id}/",
            "industry": "Technology",
            "followers_count": 25000,
            "description": "Sample LinkedIn company page"
        }
