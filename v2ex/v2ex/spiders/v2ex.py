# 爬取 v2ex 帖子信息

from scrapy.spiders import CrawlSpider
from scrapy import Request
from pyquery import PyQuery
from ..items import V2exItem
import json


class V2ex(CrawlSpider):
    name = "v2ex"

    def start_requests(self):
        yield Request(url='https://www.v2ex.com/?tab=tech',
                      headers={
                          'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36"
                      },
                      callback=self.parse)

    def parse(self, response):
        query = PyQuery(response.body.decode('UTF-8'))
        v2ex_item = V2exItem()
        for item in query('.cell.item').items():
            v2ex_item['title'] = item.find('.item_title').text()
            v2ex_item['node'] = item.find('.node').text()
            v2ex_item['auth'] = item.find('.node').next().text()
            yield v2ex_item
