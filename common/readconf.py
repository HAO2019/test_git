#测试一下
import configparser
class  DoConf():
    def doconf(self,section,option):
        con=configparser.ConfigParser()
        hao=con.get(section,option)
        return hao