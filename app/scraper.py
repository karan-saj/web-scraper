import asyncio
import httpx
import logging
from typing import List, Dict
from bs4 import BeautifulSoup

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

RATE_LIMIT_DELAY = 2

async def fetch_page(url: str) -> str:
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url)
            if response.status_code == 200:
                logger.info(f"Page loaded successfully: {url}")
                return response.text
            else:
                logger.error(f"Failed to fetch {url}. Status code: {response.status_code}")
                return ""
        except Exception as e:
            logger.error(f"Error during fetching page {url}: {e}")
            return ""

def parse_page(content: str) -> Dict:
    soup = BeautifulSoup(content, 'html.parser')

    title = soup.find("title").get_text() if soup.find("title") else "No Title"
    price = soup.find("span", {"class": "price"})
    price = price.get_text() if price else "No Price"

    return {
        "title": title,
        "price": price,
    }

async def scrape_shallow(url: str) -> Dict[str, str]:
    content = await fetch_page(url)
    if content:
        data = parse_page(content)
        return {"domain": url, "content": data}
    return {"domain": url, "error": "Failed to fetch page"}

async def scrape(urls: List[str]) -> List[Dict[str, str]]:
    results = []
    for url in urls:
        result = await scrape_shallow(url)
        results.append(result)
        await asyncio.sleep(RATE_LIMIT_DELAY)
    return results
