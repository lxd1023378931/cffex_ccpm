from config import Config
import pymssql


class SqlServerJDBC(object):
    __insertSql = "INSERT INTO utQHJYTJ ([OID],[FSRQ],[XXLY],[JZRQ],[TJFS],[TJQJ],[SC],[BDMS]," \
                  "[PZID],[XH],[HYH],[HYMC],[HYID],[CJL],[CJE],[CCL],[ZJL],[BL],[GKBZ],[XGRY],[XGRY2],[XGSJ],[FBSJ],[SHBZ],[SHRY],[SHSJ],[NID])" \
                  "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

    __host = ''
    __user = ''
    __pwd = ''
    __db = ''
    __conn = None

    def __init__(self):
        self.__config = Config()
        self.__host = self.__config.get(Config.db_section, 'host')
        self.__user = self.__config.get(Config.db_section, 'user')
        self.__pwd = self.__config.get(Config.db_section, 'pwd')
        self.__db = self.__config.get(Config.db_section, 'db')

    def __getConnection(self):
        self.__conn = pymssql.connect(host=self.__host, user=self.__user, password=self.__pwd, database=self.__db,
                                      charset="utf8")
        cur = self.__conn.cursor()
        if not cur:
            return "连接数据库失败"
        else:
            return cur

    def insertUTQ(self, utQList):
        cur = self.__getConnection()
        if (isinstance(cur, str)):
            return cur
        listParams = []
        for utQ in utQList:
            tup = (
                utQ.oid, utQ.fsrq, utQ.xxly, utQ.jzrq, utQ.tjfs, utQ.tjqj, utQ.sc, utQ.bdms, utQ.pzid, utQ.xh, utQ.hyh,
                utQ.hymc, utQ.hyid, utQ.cjl, utQ.cje, utQ.ccl, utQ.zjl, utQ.bl, utQ.gkbz, utQ.xgry, utQ.xgry2, utQ.xgsj,
                utQ.fbsj, utQ.shbz, utQ.shry, utQ.shsj, utQ.nid)
            listParams.append(tup)

        cur.executemany(self.__insertSql, listParams)

        try:
            self.__conn.commit()
        except:
            return "入库失败，请查询日志！"
        self.__conn.close()
        return "采取成功，已入库" + str(len(utQList)) + "条数据！"
