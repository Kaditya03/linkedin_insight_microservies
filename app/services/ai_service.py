from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class AISummaryService:
    def generate_summary(self, page):
        prompt = f"""
        Summarize this LinkedIn company:
        Name: {page.name}
        Industry: {page.industry}
        Followers: {page.followers_count}
        Description: {page.description}
        """

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
        )

        return response.choices[0].message.content
