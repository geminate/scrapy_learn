BOT_NAME = 'v2ex_login'

SPIDER_MODULES = ['v2ex_login.spiders']
NEWSPIDER_MODULE = 'v2ex_login.spiders'

ROBOTSTXT_OBEY = False

# LOG 等级
LOG_LEVEL = 'DEBUG'

# 输出
ITEM_PIPELINES = {
    # 'v2ex_login.pipelines.SaveFilePipeline': 300,
}

# 输出文件路径
FILE_PATH = './data/data.json'

# cookie
COOKIES_ENABLED = True
COOKIES_DEBUG = True
