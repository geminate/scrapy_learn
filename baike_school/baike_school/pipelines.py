from scrapy.exporters import JsonLinesItemExporter
import os
import pymysql


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
        self.connect = pymysql.connect(
            host='127.0.0.1',
            port=3306,
            db='scrapy_learn',
            user='root',
            passwd='root',
            charset='utf8',
            use_unicode=True)
        self.cursor = self.connect.cursor()

    def process_item(self, item, spider):
        self.cursor.execute('insert into `baike_school`(`chinese_name`, `foreign_name`) value (%s, %s)',
                            (item['chinese_name'], item['foreign_name'],))
        self.connect.commit()
        return item

    def close_spider(self, spider):
        self.cursor.close()
        self.connect.close()

    @classmethod
    def from_crawler(cls, crawler):
        return cls()
