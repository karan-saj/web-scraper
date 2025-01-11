from playwright.async_api import async_playwright


class Fetcher:
    def __init__(self):
        self.browser = None

    async def start_browser(self):
        async with async_playwright() as p:
            self.browser = await p.chromium.launch(headless=True)

    async def fetch_page(self, url):
        if not self.browser:
            await self.start_browser()

        try:
            page = await self.browser.new_page()
            await page.goto(url, timeout=10000)
            html_content = await page.content()
            return html_content
        except Exception as e:
            print(f"An error occurred while fetching {url}: {e}")
            return None
        finally:
            await page.close()

    async def close_browser(self):
        if self.browser:
            await self.browser.close()
