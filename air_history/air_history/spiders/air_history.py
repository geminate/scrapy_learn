from scrapy.spiders import CrawlSpider
from scrapy import Request
from pyquery import PyQuery
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from ..items import AirHistoryItem


class AirHistory(CrawlSpider):
    name = "air_history"  # 爬虫名称
    browser = None  # 无头浏览器

    def __init__(self, *args, **kwargs):
        super(AirHistory, self).__init__(*args, **kwargs)
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--no-sandbox')
        self.browser = webdriver.Chrome(chrome_options=chrome_options)

    def closed(self, spider):
        self.browser.close()

    def start_requests(self):
        yield Request(url='https://www.aqistudy.cn/historydata/', callback=self.parse_main)

    def parse_main(self, response):
        print('开始获取城市列表：')
        query = PyQuery(response.body)
        for href_item in query('.all li a').items():
            request = Request(url='https://www.aqistudy.cn/historydata/' + href_item.attr('href'),
                              callback=self.parse_city)
            request.meta['city'] = href_item.text()
            yield request

    def parse_city(self, response):
        city = response.meta['city']
        print('开始获取 ' + city + ' 的月份列表：')
        query = PyQuery(response.body)
        for day in query('.table tr a').items():
            request = Request(url='https://www.aqistudy.cn/historydata/' + day.attr('href'),
                              callback=self.parse_day)
            request.meta['city'] = city
            yield request

    def parse_day(self, response):
        print('开始获取 ' + response.meta['city'] + ' 的详细数据：')
        query = PyQuery(response.body)
        for info in query('.table tr:not(:first-child)').items():
            air_history_info = AirHistoryItem(city=response.meta['city'])
            air_history_info['date'] = info.find('td:nth-of-type(1)').text()
            air_history_info['aqi'] = info.find('td:nth-of-type(2)').text()
            air_history_info['level'] = info.find('td:nth-of-type(3)').text()
            air_history_info['pm25'] = info.find('td:nth-of-type(4)').text()
            air_history_info['pm10'] = info.find('td:nth-of-type(5)').text()
            air_history_info['so2'] = info.find('td:nth-of-type(6)').text()
            air_history_info['co'] = info.find('td:nth-of-type(7)').text()
            air_history_info['no2'] = info.find('td:nth-of-type(8)').text()
            air_history_info['o3'] = info.find('td:nth-of-type(9)').text()
            yield air_history_info
