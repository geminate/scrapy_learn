from scrapy import Item, Field


class V2exLoginItem(Item):
    # 标题
    title = Field()

    # 节点
    node = Field()

    # 作者
    auth = Field()
