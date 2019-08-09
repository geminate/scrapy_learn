BOT_NAME = 'v2ex'

SPIDER_MODULES = ['v2ex.spiders']
NEWSPIDER_MODULE = 'v2ex.spiders'

ROBOTSTXT_OBEY = False

# LOG 等级
LOG_LEVEL = 'DEBUG'

# 输出
ITEM_PIPELINES = {
    'v2ex.pipelines.SaveFilePipeline': 300,
}

# 输出文件路径
FILE_PATH = './data/data.json'
