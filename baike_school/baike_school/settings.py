BOT_NAME = 'baike_school'

SPIDER_MODULES = ['baike_school.spiders']
NEWSPIDER_MODULE = 'baike_school.spiders'

ROBOTSTXT_OBEY = False

# LOG 等级
LOG_LEVEL = 'WARN'

# 输出
ITEM_PIPELINES = {
    'baike_school.pipelines.SaveFilePipeline': 300,
    'baike_school.pipelines.MySqlPipeline': 500,
}

# 输出文件路径
FILE_PATH = './data/data.json'
