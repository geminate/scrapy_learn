# 基本设置
BOT_NAME = 'bilibili'
SPIDER_MODULES = ['bilibili.spiders']
NEWSPIDER_MODULE = 'bilibili.spiders'

# 不遵守 robots.txt
ROBOTSTXT_OBEY = False

# LOG 等级
LOG_LEVEL = 'DEBUG'

# 下载中间件
DOWNLOADER_MIDDLEWARES = {
    'bilibili.middlewares.RandomProxyMiddleware': 543,
}

# 超时时间
DOWNLOAD_TIMEOUT = 10

# 失败后是否重试
RETRY_ENABLED = False

# 重定向
REDIRECT_ENALBED = False

# -o 导出文件编码
FEED_EXPORT_ENCODING = 'UTF-8'

# 输出
ITEM_PIPELINES = {
    # 'bilibili.pipelines.SaveFilePipeline': 300,
}

# 输出文件路径
FILE_PATH = './data/data.json'

# Cookie
COOKIES_ENABLED = True
