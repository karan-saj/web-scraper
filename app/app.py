from fastapi import FastAPI, BackgroundTasks
from pydantic import BaseModel
import logging
from app.controllers import ScraperController

app = FastAPI()

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

class Domains(BaseModel):
    domains: list[str]

async def scrape_domains(domains: list[str]):
    controller = ScraperController()
    result = await controller.scrape_domains(domains)
    logging.info(f"Scraping finished: {result}")

@app.post("/scrape")
async def scrape(domains: Domains, background_tasks: BackgroundTasks):
    if not domains.domains:
        return {"error": "No domains provided"}

    background_tasks.add_task(scrape_domains, domains.domains)

    return {"message": "Scraping started"}
