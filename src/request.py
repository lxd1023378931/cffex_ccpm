import requests


class Request(object):
    headers = {
        "User-Agent": "ozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36",
        "Accept": "text/html,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Host": "www.cffex.com.cn",
        "X-Requested-With": "XMLHttpRequest",
        "Connection": "keep-alive"
    }
    def open(self, url):
        session = requests.session()
        session.headers = self.headers
        response = session.get(url)
        print(response.content)
        return response

