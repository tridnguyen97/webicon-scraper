from webicon_scraper.spider import MultiSpider
from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings


def run() -> None:
    store_uri = "file://./results"
    settings = Settings()
    settings.set("ITEM_PIPELINES", {"webicon_scraper.pipeline.FavIconPipeline": 1})
    settings.set("FILES_STORE", store_uri)
    process = CrawlerProcess(settings=settings)
    process.crawl(MultiSpider)
    process.start()
