from app.models import ScraperModel
import logging

class ScraperController:
    def __init__(self):
        self.model = ScraperModel()

    async def scrape_domains(self, domains: list[str]):
        try:
            result = await self.model.scrape(domains)
            logging.info(f"Scraping finished: {result}")
            return result
        except Exception as e:
            logging.error(f"Error during scraping: {e}")
            return {"error": str(e)}
