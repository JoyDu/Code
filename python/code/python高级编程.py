# coding=utf-8
'''
    添加模块导入路径
'''
import sys
print(sys.path)
sys.path.append("C:\\Users\\duwan\\AppData\\Local\\Programs\\Python\\Python36")
'''
    如果被导入的模块在导入之后做了修改，重新加载模块
'''
from imp import *
reload(sys)  # sys 模块名
'''
    == 和 is
'''
a = [1, 2, 3]
b = [1, 2, 3]
c = a
print(a == b)
print(c == a)
print(a is b)
print(c is b)
print(id(a))
print(id(b))
print(id(c))
'''
    深拷贝和浅拷贝
    copy.copy()如果目标里面有引用的值 则cope_e只是自己重新开辟内存 里面指向被拷贝目标指向的引用地址
    copy.deepcope()内部引用数据一样重新开辟内存
'''
import copy
cope_a = 10
cope_b = copy.deepcopy(a)
cope_c = cope_a
print("cope_a:%d" % id(cope_a))
print("cope_b:%d" % id(cope_b))
print("cope_c:%d" % id(cope_c))

copy_e = copy.copy(cope_a)
'''
    进制 位运算 直接操作二进制省内存，高效率
    <<向左位移 数值翻倍
    >>向右位移 数值减半
'''
print("8>>1=%d" % (8 >> 1))
print("8<<1=%d" % (8 << 1))
'''
    作用域 LEGB规则
    locals -> enclosing function -> globals -> builtins
    locals:当前所在命名空间(函数模块等)，函数参数也属于命名空间内的变量
    enclosing:外部嵌套函数的命名空间（闭包等）
    globals:全局变量，函数定义所在模块命名空间
    builtins:内建模块命名空间
'''
A = 10
B = 20


def test():
    a = 1
    b = 2
    print("locals:")
    print(locals())
    print("globals:")
    print(globals())


test()
'''
    进制、位运算
'''
'''
    私有化
    xx: 公有变量
    _x: 单前置下划线,私有化属性或⽅法，from somemodule import *禁⽌导⼊,类对象和⼦类可以访问
    __xx：双前置下划线,避免与⼦类中的属性命名冲突，⽆法在外部直接访问(名字重整所以访问不到)
    __xx__:双前后下划线,⽤户名字空间的魔法对象或属性。例如: __init__ , __ 不要⾃⼰发明这样的名字
    xx_:单后置下划线,⽤于避免与Python关键词的冲突
'''
'''
    属性property 封装属性
'''

#封装方式1
print("属性封装方式一")


class Test(object):
    def __init__(self):
        self.__num = 100

    def setNum(self, newNum):
        print("----setter----")
        self.__num = newNum

    def getNum(self):
        print("----getter----")
        return self.__num

    num = property(getNum, setNum)


t = Test()
t.num = 50
print(t.num)

#使用装饰器property封装属性
print("属性封装方式二")


class Test_f(object):
    def __init__(self):
        self.__num = 100

    @property
    def num(self):
        print("----getter----")
        return self.__num

    @num.setter
    def num(self, newNum):
        print("----setter----")
        self.__num = newNum


tf = Test_f()
tf.num = 50
print(tf.num)
'''
迭代器 可用next()取值的都是迭代器
'''
# 判断是否可迭代
from collections import Iterable
print(isinstance("abc", Iterable))
print(isinstance([], Iterable))
from collections import Iterator
# 判断是否是可迭代对象
print(isinstance([], Iterator))
#转换成可迭代对象
a = [1, 2, 3, 4]
a = iter(a)
print(next(a))
print(next(a))
'''
    闭包
'''


def bibao(number):
    print("*******1******")

    def bibao_in(number1):
        print("*****2******")
        print(number + number1)

    print("******3******")
    return bibao_in


bibao_res = bibao(100)
bibao_res(10)
bibao_res(20)
'''
    装饰器
    装饰器原理
    多个装饰器
    装饰带参函数
    装饰带返回值函数
    带参装饰器
'''


def checkPermission():
    pass


'''
    动态添加属性及types.MethodType动态添加方法
'''

import types


class Person(object):
    # __slots__限制能动态添加的属性
    __slots__ = ("name", "age", "addr", "sleep")

    def __init__(self, new_Name, new_Age):
        self.name = new_Name
        self.age = new_Age


laowang = Person("laowang", 30)
# 动态添加属性
laowang.addr = "成都"
print("name:%s,age:%d,addr:%s" % (laowang.name, laowang.age, laowang.addr))


# 动态添加方法
def sleep(self):
    print("%s正在睡觉！！！" % self.name)


laowang.sleep = types.MethodType(sleep, laowang)
laowang.sleep()


# 动态添加静态方法
@staticmethod
def getTeche(tecName):
    print("我会%s技能" % tecName)


Person.teche = getTeche
Person.teche("开车")


# 动态添加类方法
@classmethod
def home(cls):
    print("Home Address:%s" % "春熙路")


Person.address = home
Person.address()
'''
生成器
'''
# 交换值
a = 5
b = 8
a, b = b, a
print("a:%d,b:%d" % (a, b))
