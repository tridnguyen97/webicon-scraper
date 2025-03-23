from webicon_scraper.spider import MultiSpider
from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings


def run() -> None:
    settings = Settings()
    settings.set("ITEM_PIPELINES", {"webicon_scraper.pipeline.FavIconPipeline": 1})
    process = CrawlerProcess(settings=settings)
    process.crawl(MultiSpider)
    process.start()
