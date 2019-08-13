# 爬取 v2ex_login 帖子信息

from scrapy.spiders import CrawlSpider
from scrapy import Request, FormRequest
from pyquery import PyQuery
import re
from PIL import Image
import matplotlib.pyplot as plt
from io import BytesIO


class V2exLogin(CrawlSpider):
    name = "v2ex_login"
    once = ''

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
                              'aa9a75c6e3e218487fb8e6ad8b5248c1d9a3692140ff7d5f98b8db20b3069899': username,
                              '8e2bf3152acfd62ac0f31973f65376d634e2e6fda9bd07730b0ca5e8cfa658a8': password,
                              '9653091ecb4ddc0d1c0dcce07e2884ddc39c2ae83cb4dad04b47674a159ad809': captcha,
                              'once': self.once,
                              'next': '/'
                          },
                          callback=self.parse_after_login)

    def parse_after_login(self, response):
        print(response.text)
        pass
