from scrapy.exporters import JsonLinesItemExporter
import os
from .items import V2exLoginItem


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
