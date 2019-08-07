# 获取百度百科上 985/211 学校相关基本信息

from scrapy import Request
from scrapy.spiders import CrawlSpider
from re import sub
from pyquery import PyQuery
from scrapy_learn.items import BaikeSchoolInfo


class BaikeSchool(CrawlSpider):
    name = "baike_school"

    start_urls = ['https://www.dxsbb.com/news/2799.html']

    # 从学校列表页面爬取 985/211 大学列表
    def parse(self, response):
        query = PyQuery(response.body)
        for tableItem in query('#newsContent table:nth-of-type(2) tr:not(:first-child) td:nth-of-type(2)').items():
            url = 'https://baike.baidu.com/item/' + tableItem.text()
            if tableItem.text() == '北京师范大学':
                break
            request = Request(url=url,
                              headers={
                                  'User-Agent': "USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64) "
                                                "AppleWebKit/537.36 (KHTML, like Gecko) "
                                                "Chrome/58.0.3029.110 Safari/537.36'"
                              },
                              callback=self.parse_address)
            request.meta['school'] = tableItem.text()
            yield request

    # 从百度百科上爬取学校基本信息
    def parse_address(self, response):
        query = PyQuery(response.body)
        school_info = BaikeSchoolInfo()

        for dtItem in query('.basicInfo-block:not(.overlap) > dt').items():
            label = dtItem.text().replace(' ', '')

            if label.find('中文名') != -1:
                school_info['chinese_name'] = self.get_val_from_dt(dtItem)

            if label.find('外文名') != -1:
                school_info['foreign_name'] = self.get_val_from_dt(dtItem)

            if label.find('简称') != -1:
                school_info['abbreviation'] = self.get_val_from_dt(dtItem)

            if label.find('创办时间') != -1:
                school_info['founding_time'] = self.get_val_from_dt(dtItem)

            if label.find('地址') != -1:
                school_info['address'] = self.get_val_from_dt(dtItem)

        yield school_info

    # 从 dt 标签中获取数据，如果存在需要展开的标签则返回展开后的数据
    def get_val_from_dt(self, item):

        if item.next().find('.overlap'):
            text = item.next().find('.overlap dd').text()
        else:
            text = item.next().text()

        return sub(r'\[[0-9]\]', "", text.replace('\n', ' // ').replace('收起', ''))
