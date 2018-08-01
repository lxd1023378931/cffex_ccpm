import requests


class Request(object):

    def open(self, url):
        response = requests.get(url)
        print(response.content)
        return response

