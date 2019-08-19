BOT_NAME = 'bilibili'

SPIDER_MODULES = ['bilibili.spiders']
NEWSPIDER_MODULE = 'bilibili.spiders'

ROBOTSTXT_OBEY = False

# LOG 等级
LOG_LEVEL = 'DEBUG'

DOWNLOADER_MIDDLEWARES = {
    'bilibili.middlewares.RandomProxyMiddleware': 543,
}

DOWNLOAD_TIMEOUT = 10

RETRY_ENABLED = False

FEED_EXPORT_ENCODING = 'UTF-8'

# 输出
ITEM_PIPELINES = {
    # 'bilibili.pipelines.SaveFilePipeline': 300,
}

# 输出文件路径
FILE_PATH = './data/data.json'
COOKIES_ENABLED = True
