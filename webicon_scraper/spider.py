from scrapy import Spider, Request
from webicon_scraper.preprocess import get_domain_path, get_icon_url


class MultiSpider(Spider):
    name = "multi_domain_spider"

    def start_requests(self) -> Request:
        domain_path = get_domain_path()
        url_list = get_icon_url(domain_path)
        for icon_url in url_list:
            yield Request(url=icon_url, callback=self.parse)

    def parse(self, response):
        yield {"icon_url": response.url, "icon_bytes": response.body}


class TestSpider(Spider):
    name = "test_spider"

    def __init__(self, name=None, **kwargs):
        super().__init__(name, **kwargs)
        self.icon_url = kwargs["icon_url"]

    def start_requests(self):
        yield Request(url=self.icon_url, callback=self.parse_response)

    def parse_response(self, response):
        yield {"icon_url": response.url}
