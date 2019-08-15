from scrapy import Item, Field
from peewee import CharField, DoubleField, MySQLDatabase, Model, CompositeKey

db = MySQLDatabase("scrapy_learn", host='127.0.0.1', port=3306, user='root', passwd='root', charset='utf8')


class AirHistoryItem(Item):
    # 日期
    date = Field()

    # 城市
    city = Field()

    # 空气指数
    aqi = Field()

    # 质量等级
    level = Field()

    # PM2.5
    pm25 = Field()

    # PM10
    pm10 = Field()

    # 二氧化硫
    so2 = Field()

    # 一氧化碳
    co = Field()

    # 二氧化氮
    no2 = Field()

    # 臭氧
    o3 = Field()


class AirHistoryInfo(Model):
    date = CharField(null=False)
    city = CharField(null=False)
    aqi = DoubleField(null=True)
    level = CharField(null=True)
    pm25 = DoubleField(null=True)
    pm10 = DoubleField(null=True)
    so2 = DoubleField(null=True)
    co = DoubleField(null=True)
    no2 = DoubleField(null=True)
    o3 = DoubleField(null=True)

    class Meta:
        primary_key = CompositeKey('date', 'city')
        database = db
