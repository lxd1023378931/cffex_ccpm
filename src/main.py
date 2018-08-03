from src.config import Config
from src.request import Request
from xml.dom.minidom import parse
from src.utqhjytj import utQHJYTJ
import xml.dom.minidom
import time

class Main(object):

    __config = None
    __request = None
    __url = ''
    __type = ''
    __yyyyMM = ''
    __dd = ''
    __dataList = []

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
            response = self.__request.open(url.replace("TYPE", type, 1))
            if(response.status_code == 200):
                self.__xml(response.content)
    def __xml(self,strs):
        domTree = xml.dom.minidom.parseString(strs)
        element = domTree.documentElement
        datas = element.getElementsByTagName("data")
        for data in datas:
            instrumentid = data.getElementsByTagName("instrumentid")[0].childNodes[0].data
            tradingday = data.getElementsByTagName("tradingday")[0].childNodes[0].data
            datatypeid = data.getElementsByTagName("datatypeid")[0].childNodes[0].data
            rank = data.getElementsByTagName("rank")[0].childNodes[0].data
            shortname = data.getElementsByTagName("shortname")[0].childNodes[0].data
            volume = data.getElementsByTagName("volume")[0].childNodes[0].data
            varvolume = data.getElementsByTagName("varvolume")[0].childNodes[0].data
            partyid = data.getElementsByTagName("partyid")[0].childNodes[0].data
            productid = data.getElementsByTagName("productid")[0].childNodes[0].data
            utQ = utQHJYTJ()

            # utQ.oid = 0 #主键
            utQ.fsrq = tradingday[0:4]+'/'+str(int(tradingday[4:6]))+'/'+str(int(tradingday[6:8]))
            utQ.jzrq = tradingday[0:4]+'/'+str(int(tradingday[4:6]))+'/'+str(int(tradingday[6:8]))
            utQ.tjfs = 21 if(datatypeid == 0) else (22 if(datatypeid == 1) else 23)
            utQ.bdms = instrumentid
            # utQ.pzid = 0 #关联表查询
            utQ.xh = rank
            utQ.hymc = shortname
            # utQ.hyid = 0 #关联查询
            utQ.cjl = volume if(datatypeid == 0) else None
            utQ.ccl = volume if(datatypeid != 0) else None
            utQ.zjl = varvolume
            utQ.gkbz = 0
            utQ.xgsj = time.strftime("%H:%M:%S", time.localtime())+'.0'
            utQ.fbsj = time.strftime("%H:%M:%S", time.localtime())+'.0'

            self.__dataList.append(utQ)
