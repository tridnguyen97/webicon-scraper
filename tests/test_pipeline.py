import unittest
from scrapy.crawler import Crawler
from scrapy.settings import Settings
from webicon_scraper.pipeline import FavIconPipeline
from webicon_scraper.spider import TestSpider


class TestPipeline(unittest.TestCase):
    def setUp(self):
        # Mock the Scrapy crawler and settings
        self.img_test_url = "https://cdn.jsdelivr.net/gh/belaviyo/save-images@1.0.0/test/simples/2/text.png"
        self.store_uri = "file:./assets"
        self.spider = None
        settings = Settings(
            {"FILES_STORE": self.store_uri}
        )  # Set a temporary storage location
        self.crawler = Crawler(TestSpider, settings=settings)
        self.pipeline = FavIconPipeline.from_crawler(self.crawler)

    def test_pipeline(self):
        # Initialize a crawler instance
        test_item = {"image_url": self.img_test_url}
        processed_item = self.pipeline.process_item(test_item, self.spider)
        self.assertEqual(processed_item, test_item)
