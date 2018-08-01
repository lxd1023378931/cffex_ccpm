import configparser


class Config(object):

    __cf = configparser.ConfigParser()
    req_section = "setting"
    db_section = "db"

    # 初始化文件
    def __init__(self):
        self.__cf.read("../config.ini")

    # 通过section和option获取值
    def get(self, section, option):
        return self.__cf.get(section, option)
