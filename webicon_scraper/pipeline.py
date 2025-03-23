from scrapy import Request
from scrapy.pipelines.files import FilesPipeline


class FavIconPipeline(FilesPipeline):
    def __init__(self, store_uri, crawler):
        super().__init__(store_uri, crawler)
        self.crawler = crawler

    @classmethod
    def from_crawler(cls, crawler):
        # Get FILES_STORE from settings
        store_uri = crawler.settings.get("FILES_STORE")
        return cls(store_uri, crawler)

    def get_icon_requests(self, item, info):
        icon_url = item.get("icon_url")
        if icon_url:
            yield Request(url=icon_url)

    def file_path(self, request, response=None, info=None, *, item=None):
        super().file_path(request, response, info, item=item)
        file_name = request.url.split("/")[-1]
        import pdb

        pdb.set_trace()
        return f"./assets/data/{file_name}"

    def process_item(self, item, spider):
        requests = list(self.get_media_requests(item, spider))
        for request in requests:
            # Mock file download or response processing
            file_path = self.file_path(request)
            print(f"File would be saved at: {file_path}")
        return item
