from .items import AirHistoryInfo


# 将结果保存至 Mysql
class MySqlPipeline(object):

    def __init__(self):
        pass

    def open_spider(self, spider):
        if not AirHistoryInfo.table_exists():
            AirHistoryInfo.create_table()

    def process_item(self, item, spider):
        if AirHistoryInfo.get_or_none(date=item['date'], city=item['city']):
            AirHistoryInfo(**item).save()
        else:
            AirHistoryInfo.create(**item)
        return item

    def close_spider(self, spider):
        pass

    @classmethod
    def from_crawler(cls, crawler):
        return cls()
