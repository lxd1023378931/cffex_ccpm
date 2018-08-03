from src.config import Config


class SqlServerJDBC(object):
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
        # pymssql.connect(host=self.__host, user=self.__user, password=self.__pwd, database=self.__db, charset="utf8")
        pass
