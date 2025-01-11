import unittest
from app.models import ScraperModel

class TestScraperModel(unittest.TestCase):
    def setUp(self):
        self.model = ScraperModel()

    def test_scrape(self):
        domains = ["https://www.example.com"]
        result = self.model.scrape(domains)
        self.assertTrue(len(result) > 0)

if __name__ == '__main__':
    unittest.main()
