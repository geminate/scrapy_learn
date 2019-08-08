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
