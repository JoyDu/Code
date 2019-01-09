# coding=utf-8
class Singleton(object):
    __instance = None
    __first_init = False

    def __new__(cls, age, name):
        if not cls.__instance:
            cls.__instance = object.__new__(cls)
        return cls.__instance

    def __init__(self, age, name):
        if not self.__first_init:
            self.age = age
            self.name = name
            Singleton.__first_init = True

    def __str__(self):
        return self.name


zs = Singleton(18, "张三")
print(zs)
ls = Singleton(28, "李四")
print(ls)
try:
    if ls.__str__() == "张三":
        raise Exception("Singleton是单例模式类")
except Exception as ex:
    print(ex)
