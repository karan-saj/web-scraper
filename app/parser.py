from bs4 import BeautifulSoup

class Parser:

    async def parse(self, html_content):
        soup = BeautifulSoup(html_content, 'html.parser')
        product_urls = []

        for link in soup.find_all('a', href=True):
            if self.is_product_url(link['href']):
                product_urls.append(link['href'])

        return self.filter_product_urls(product_urls)

    def is_product_url(self, url):
        product_keywords = ['product', 'dp', 'item']

        return any(keyword in url for keyword in product_keywords)

    def filter_product_urls(self, urls):

        return [url for url in urls if self.is_product_url(url)]
