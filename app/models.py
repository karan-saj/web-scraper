# models.py

from app.scraper import fetch_page

class ScraperModel:
    async def scrape(self, domains: list[str]):
        results = []
        for domain in domains:
            content = await fetch_page(domain)
            if content:
                results.append({"domain": domain, "content": content})
            else:
                results.append({"domain": domain, "error": "Failed to fetch page"})
        return results
