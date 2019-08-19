from scrapy.spiders import CrawlSpider
from scrapy import Request
import json


class Bilibili(CrawlSpider):
    name = "bilibili"  # 爬虫名称

    def start_requests(self):
        for i in range(1, 150):
            request = Request(url='https://api.bilibili.com/x/web-interface/archive/stat?aid=' + str(i),
                              callback=self.parse)
            request.meta['aid'] = str(i)
            yield request

    def parse(self, response):
        yield json.loads(response.text)
