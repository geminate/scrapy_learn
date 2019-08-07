from scrapy import Item, Field


class BaikeSchoolInfo(Item):
    # 中文名
    chinese_name = Field()

    # 外文名
    foreign_name = Field()

    # 简称
    abbreviation = Field()

    # 创办时间
    founding_time = Field()

    # 类别

    # 类型

    # 属性

    # 主管部门

    # 现任

    # 地址
    address = Field()

    # 校庆日
    decoration_day = Field()
