from scrapy import Item, Field
from peewee import CharField, IntegerField, MySQLDatabase, Model

db = MySQLDatabase("scrapy_learn", host='127.0.0.1', port=3306, user='root', passwd='root', charset='utf8')


class BaikeSchoolInfoItem(Item):
    index = Field()

    # 中文名
    chinese_name = Field()

    # 外文名
    foreign_name = Field()

    # 简称
    abbreviation = Field()

    # 创办时间
    founding_time = Field()

    # 类别
    category = Field()

    # 类型
    type = Field()

    # 属性
    attribute = Field()

    # 主管部门
    competent_department = Field()

    # 现任领导
    present_leader = Field()

    # 专职院士
    academician = Field()

    # 本科专业
    undergraduate_major = Field()

    # 硕士点
    master = Field()

    # 博士点
    doctoral = Field()

    # 博士后
    post_doctoral = Field()

    # 国家重点学科
    key_disciplines = Field()

    # 院系设置
    departments = Field()

    # 校庆日
    decoration_day = Field()

    # 地址
    address = Field()

    # 院校代码
    code = Field()

    # 主要奖项
    prize = Field()

    # 知名校友
    alumnus = Field()


class BaikeSchoolInfo(Model):
    index = IntegerField(primary_key=True, null=False)
    chinese_name = CharField(null=True)
    foreign_name = CharField(null=True)
    abbreviation = CharField(null=True)
    founding_time = CharField(null=True)
    category = CharField(null=True)
    type = CharField(null=True)
    attribute = CharField(null=True)
    competent_department = CharField(null=True)
    present_leader = CharField(null=True)
    academician = CharField(null=True)
    undergraduate_major = CharField(null=True)
    master = CharField(null=True)
    doctoral = CharField(null=True)
    post_doctoral = CharField(null=True)
    key_disciplines = CharField(null=True)
    departments = CharField(max_length=1000, null=True)
    decoration_day = CharField(null=True)
    address = CharField(max_length=1000, null=True)
    code = CharField(null=True)
    prize = CharField(max_length=1000, null=True)
    alumnus = CharField(null=True)

    class Meta:
        database = db
