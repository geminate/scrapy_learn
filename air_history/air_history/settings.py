BOT_NAME = 'air_history'

SPIDER_MODULES = ['air_history.spiders']
NEWSPIDER_MODULE = 'air_history.spiders'

ROBOTSTXT_OBEY = False

# LOG 等级
LOG_LEVEL = 'DEBUG'

DOWNLOADER_MIDDLEWARES = {
    'air_history.middlewares.SeleniumMiddleware': 543,
}

# 输出
ITEM_PIPELINES = {
    'air_history.pipelines.MySqlPipeline': 300,
}

# 输出文件路径
FILE_PATH = './data/data.json'

# cookie
COOKIES_ENABLED = True
COOKIES_DEBUG = True
