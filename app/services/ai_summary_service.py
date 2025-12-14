import os

class AISummaryService:
    """
    Generates a short human-readable summary for a LinkedIn page.
    This version is safe, simple, and interview-friendly.
    """

    async def generate_summary(self, page: dict) -> str:
        """
        page is expected to be a dictionary with keys:
        name, industry, followers, description
        """

        name = page.get("name", "This company")
        industry = page.get("industry", "Unknown industry")
        followers = page.get("followers", 0)

        summary = (
            f"{name} is a company operating in the {industry} domain. "
            f"It currently has around {followers} followers on LinkedIn. "
            f"The page shows steady activity and engagement."
        )

        return summary
