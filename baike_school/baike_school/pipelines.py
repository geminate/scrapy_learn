from scrapy.exporters import JsonLinesItemExporter
import os
from .items import BaikeSchoolInfo


# 将结果保存为 .json 文件
class SaveFilePipeline(object):

    def __init__(self, path):
        self.path = path
        self.fp = open(self.path, 'wb')
        self.exporter = JsonLinesItemExporter(self.fp, encoding='utf-8')

    def open_spider(self, spider):
        self.fp.write(b'[')
        self.exporter.start_exporting()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        self.fp.write(b',')
        return item

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.fp.seek(-2, os.SEEK_END)  # 定位到倒数第二个字符，即最后一个逗号
        self.fp.truncate()  # 删除最后一个逗号
        self.fp.write(b']')
        self.fp.close()

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.settings.get('FILE_PATH'))


# 将结果保存至 Mysql
class MySqlPipeline(object):

    def __init__(self):
        pass

    def open_spider(self, spider):
        if not BaikeSchoolInfo.table_exists():
            BaikeSchoolInfo.create_table()

    def process_item(self, item, spider):
        if BaikeSchoolInfo.get_or_none(chinese_name=item['chinese_name']):
            BaikeSchoolInfo(**item).save()
        else:
            BaikeSchoolInfo.create(**item)
        return item

    def close_spider(self, spider):
        pass

    @classmethod
    def from_crawler(cls, crawler):
        return cls()
