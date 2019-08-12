# 爬取 v2ex_cookie 帖子信息

from scrapy.spiders import CrawlSpider
from scrapy import Request
from pyquery import PyQuery
from ..items import V2exCookieItem
from utils import cookie_to_dict


class V2exCookie(CrawlSpider):
    name = "v2ex_cookie"

    # TODO change cookie
    cookie = 'cookie=YourCookie'

    def start_requests(self):
        yield Request(url='https://www.v2ex.com/recent?p=4',
                      headers={
                          'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36",
                      },
                      cookies=cookie_to_dict(self.cookie),
                      callback=self.parse)

    def parse(self, response):
        query = PyQuery(response.body.decode('UTF-8'))
        v2ex_cookie_item = V2exCookieItem()
        for item in query('.cell.item').items():
            v2ex_cookie_item['title'] = item.find('.item_title').text()
            v2ex_cookie_item['node'] = item.find('.node').text()
            v2ex_cookie_item['auth'] = item.find('.node').next().text()
            yield v2ex_cookie_item
