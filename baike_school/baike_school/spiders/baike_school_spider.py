# 获取百度百科上 985/211 学校相关基本信息

from scrapy import Request
from scrapy.spiders import CrawlSpider
from re import sub
from pyquery import PyQuery
from ..items import BaikeSchoolInfo


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
            request = Request(url=url, callback=self.parse_address)
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

            if label.find('类别') != -1:
                school_info['category'] = self.get_val_from_dt(dtItem)

            if label.find('类型') != -1:
                school_info['type'] = self.get_val_from_dt(dtItem)

            if label.find('属性') != -1:
                school_info['attribute'] = self.get_val_from_dt(dtItem)

            if label.find('主管部门') != -1:
                school_info['competent_department'] = self.get_val_from_dt(dtItem)

            if label.find('现任领导') != -1:
                school_info['present_leader'] = self.get_val_from_dt(dtItem)

            if label.find('专职院士') != -1:
                school_info['academician'] = self.get_val_from_dt(dtItem)

            if label.find('本科专业') != -1:
                school_info['undergraduate_major'] = self.get_val_from_dt(dtItem)

            if label.find('硕士点') != -1:
                school_info['master'] = self.get_val_from_dt(dtItem)

            if label.find('博士点') != -1:
                school_info['doctoral'] = self.get_val_from_dt(dtItem)

            if label.find('博士后') != -1:
                school_info['post_doctoral'] = self.get_val_from_dt(dtItem)

            if label.find('重点学科') != -1:
                school_info['key_disciplines'] = self.get_val_from_dt(dtItem)

            if label.find('院系') != -1:
                school_info['departments'] = self.get_val_from_dt(dtItem)

            if label.find('校庆日') != -1:
                school_info['decoration_day'] = self.get_val_from_dt(dtItem)

            if label.find('地址') != -1:
                school_info['address'] = self.get_val_from_dt(dtItem)

            if label.find('院校代码') != -1:
                school_info['code'] = self.get_val_from_dt(dtItem)

            if label.find('奖项') != -1:
                school_info['prize'] = self.get_val_from_dt(dtItem)

            if label.find('校友') != -1:
                school_info['alumnus'] = self.get_val_from_dt(dtItem)

        yield school_info

    # 从 dt 标签中获取数据，如果存在需要展开的标签则返回展开后的数据
    def get_val_from_dt(self, item):

        if item.next().find('.overlap'):
            text = item.next().find('.overlap dd').text()
        else:
            text = item.next().text()

        return sub(r'\[[0-9]\]', "", text.replace('\n', ' // ').replace('收起', ''))
