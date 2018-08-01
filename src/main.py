from src.config import Config
from src.request import Request


class Main(object):

    __config = None
    __request = None
    __url = ''
    __type = ''
    __yyyyMM = ''
    __dd = ''

    def __init__(self, yyyymm, dd):
        self.__config = Config()
        self.__request = Request()
        self.__url = self.__config.get(Config.req_section, 'url')
        self.__type = self.__config.get(Config.req_section, 'type')
        self.__yyyyMM = yyyymm
        self.__dd = dd

    def main(self):
        typeList = self.__type.strip(',').split(',')
        print(typeList)
        url = self.__url.replace("YYYYMM", self.__yyyyMM, 1).replace("DD", self.__dd, 1)
        for type in typeList:
            print(url.replace("TYPE", type, 1))
            response = self.__request.open(url)
