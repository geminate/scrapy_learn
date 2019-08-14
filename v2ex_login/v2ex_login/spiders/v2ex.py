# 爬取 v2ex_login 帖子信息

from scrapy.spiders import CrawlSpider
from scrapy import Request, FormRequest
from pyquery import PyQuery
import re
from PIL import Image
import matplotlib.pyplot as plt
from io import BytesIO


class V2exLogin(CrawlSpider):
    name = "v2ex_login"  # 爬虫名称
    once = ''  # 验证码编号
    username_code = ''  # 用户名请求参数key
    password_code = ''  # 密码请求参数key
    captcha_code = ''  # 验证码请求参数key

    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36",
    }

    def start_requests(self):
        yield Request(url='https://www.v2ex.com/signin',
                      headers=self.headers,
                      meta={'cookiejar': True},
                      callback=self.parse_login)

    def parse_login(self, response):
        query = PyQuery(response.body.decode('UTF-8'))
        captcha_html = query('form tr:nth-of-type(3) td:nth-of-type(2)').html()
        self.once = re.search('once=(.*)\'\);', captcha_html).group(1)
        self.username_code = query('form tr:nth-of-type(1) input').attr('name')
        self.password_code = query('form tr:nth-of-type(2) input').attr('name')
        self.captcha_code = query('form tr:nth-of-type(3) input').attr('name')
        captcha_url = 'https://www.v2ex.com/_captcha?once=' + self.once
        yield Request(url=captcha_url, headers=self.headers, meta={'cookiejar': True}, callback=self.parse_captcha)

    def parse_captcha(self, response):
        f = BytesIO(response.body)
        img = Image.open(f)
        plt.figure("dog")
        plt.imshow(img)
        plt.show()

        print('请输入验证码：')
        captcha = input()
        print('请输入用户名：')
        username = input()
        print('请输入密码：')
        password = input()

        yield FormRequest(url='https://www.v2ex.com/signin',
                          headers=self.headers,
                          formdata={
                              self.username_code: username,
                              self.password_code: password,
                              self.captcha_code: captcha,
                              'once': self.once,
                              'next': '/'
                          },
                          callback=self.parse_after_login,
                          meta={'cookiejar': True})

    def parse_after_login(self, response):
        print(response.url)
        print(response.text)
        pass
