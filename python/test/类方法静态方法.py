# coding=utf-8
import datetime


def flipStr():
    str = "测试系统"
    print(str[::-1])


class People(object):
    country = "china"

    @classmethod
    def getCountry(cls):
        return cls.country

    @classmethod
    def setCountry(cls, country):
        cls.country = country

    @staticmethod  # 静态方法不需要参数
    def getCountryStatic():
        return People.country  # 通过类对象引用类属性

    @staticmethod
    def getCurrentTime():
        return datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")


p = People()
print(p.country)
print(p.getCountry())  # 静态方法只能
print(People.getCountry())
print(p.getCountryStatic())
print(p.getCurrentTime())
if __name__ == "__main__":
    flipStr()