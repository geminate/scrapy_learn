import scrapy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class SeleniumMiddleware(object):
    def process_request(self, request, spider):
        browser = spider.browser
        browser.get(request.url)
        if request.url == 'https://www.aqistudy.cn/historydata/':
            pass
        else:
            WebDriverWait(browser, 10).until(lambda x: len(browser.find_elements_by_css_selector('.table tr')) > 1)
            return scrapy.http.HtmlResponse(url=request.url, body=spider.browser.page_source, encoding='utf-8',
                                            request=request)
