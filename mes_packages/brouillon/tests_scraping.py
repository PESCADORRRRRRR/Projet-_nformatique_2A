import unittest
from scraping import WikipediaScraper

class TestWikipediaScraper(unittest.TestCase):
    def test_init(self):
        url = "https://www.example.com"
        scraper = WikipediaScraper(url)
        
        self.assertEqual(scraper.url, url)
        self.assertEqual(scraper.singles, [])
        
        
        

if __name__ == '__main__':
    unittest.main()