from scrapy import Item, Field


class V2exItem(Item):
    # 标题
    title = Field()

    # 节点
    node = Field()

    # 作者
    auth = Field()
