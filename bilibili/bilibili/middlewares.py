import requests


class RandomProxyMiddleware(object):

    def process_request(self, request, spider):
        request.headers.setdefault('User-Agent',
                                   "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36")
        proxy = self.proxy()
        print('开始使用代理：' + proxy + ' 获取 ID: ' + request.meta['aid'])
        request.meta['proxy'] = 'https://' + proxy

    def process_response(self, request, response, spider):
        if response.status != 200:
            print('使用代理：' + request.meta['proxy'] + ' 获取失败, ID: ' + request.meta['aid'] + ' ,response=' + response.text)
            return self.send_proxy_request(request)
        else:
            print('使用代理：' + request.meta['proxy'] + ' 成功获取, ID: ' + request.meta['aid'])
            return response

    def process_exception(self, request, exception, spider):
        print('使用代理：' + request.meta['proxy'] + ' 获取失败, ID: ' + request.meta['aid'] + ',Exception=' + str(exception))
        return self.send_proxy_request(request)

    def send_proxy_request(self, request):
        request.meta['proxy'] = 'https://' + self.proxy()
        return request

    @staticmethod
    def proxy():
        proxy = requests.get("http://127.0.0.1:5010/get").text
        return proxy
