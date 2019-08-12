# 爬取 v2ex_login 帖子信息

from scrapy.spiders import CrawlSpider
from scrapy import Request
from pyquery import PyQuery
import re
from ..items import V2exLoginItem
from utils import cookie_to_dict
import urllib.request
from scrapy.http.cookies import CookieJar

login_cookie = CookieJar()


class V2exLogin(CrawlSpider):
    name = "v2ex_login"

    def start_requests(self):
        yield Request(url='https://www.v2ex.com/signin',
                      headers={
                          'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36",
                      },
                      callback=self.parse)

    def parse(self, response):
        login_cookie.extract_cookies(response, response.request)
        query = PyQuery(response.body.decode('UTF-8'))
        captcha_html = query('form tr:nth-of-type(3) td:nth-of-type(2)').html()
        captcha_url = 'https://www.v2ex.com/' + re.search('url\(\'/(.*)\'\);', captcha_html).group(1)
        yield Request(url=captcha_url, callback=self.parse_captcha, meta={'cookiejar': login_cookie})

    def parse_captcha(self, response):
        self.log(response.body)
        pass
