# coding=utf-8
'''
魔法方法：__init__ __str__ __del__(对象被回收时自动调用)
私有方法：方法前加双下划线和私有变量一样
私有方法和属性不会被继承 如果父类私有方法在公有方法被调用 子类继承了此方法，可以在方法中访问父类的私有方法和属性
'''
import sys


class T:
    def eat(self):
        print('=吃=')


class T1:
    def eat(self):
        print('=狂吃=')
        T.eat(self)


# 重写
# 调用被重写的方法 父类.method(self) 或者super().method()
t = T()
t.eat()
t1 = T1()
t1.eat()

# 获取对象的引用个数
print(sys.getrefcount(t))

# 多继承
# 获取调用顺序
# print(t.__mro__)


# 类属性和实例属性 类属性在多个实例之间共享 实例属性单属于实例
class Tool:
    num = 0

    def __init__(self):
        Tool.num += 1

    @classmethod
    def add_num(cls):
        cls.num += 1

    @staticmethod
    def print_menu():
        print('===========')
        print('===start game====')
        print('===========')


t1 = Tool()
t2 = Tool()
t3 = Tool()
print(Tool.num)
t1.add_num()
print(t1.num)
Tool.add_num()
print(t1.num)
t1.print_menu()
Tool.print_menu()

# 类方法 @classmethod 可通过类的实例调用类方法 也可以通过类名调用类方法
# 静态方法 可以没有参数 @staticmethod 可通过类的实例调用类方法 也可以通过类名调用类方法


# __new__创建对象
class Dog(object):
    def __init__(self):  # 初始化对象
        print('---init---')

    def __del__(self):
        print('---del---')

    def __str__(self):
        print('---str---')
        return '对象的描述信息'

    def __new__(cls):  # cls此时是Dog指向的那个对象
        print('---new---')
        return object.__new__(cls)


dog = Dog()


# 单例模式
class Pig(object):
    __instance = None

    def __new__(cls):
        if cls.__instance == None:
            cls.instance = object.__new__(cls)
            return cls.__instance
        else:
            return cls.__instance


pigA = Pig()
print(id(pigA))
pigB = Pig()
print(id(pigB))
'''
异常处理
'''
try:
    # raise
    open('111.txt')
    print(des)
    print('--------')
except (NameError, FileNotFoundError) as ex:  # Exception
    print(ex)
else:
    print('没有异常才会执行的程序')
finally:
    print('始终会执行')


class MyException(Exception):
    '''自定义异常类 继承Exception类'''

    def __init__(self, length, atleast):
        self.length = length
        self.atleast = atleast


def main():
    try:
        s = 5  # input('请输入...')
        if s < 3:
            raise MyException(len(s), 3)
    except MyException as res:
        print('MyException:输入长度是%d长度至少应该是%d' % (res.length, res.atleast))
        raise  # 抛出异常按照默认方式处理
    else:
        print('无异常产生')


main()
'''
模块 调用模块的时候会将模块执行一次__name__模块内执行是__main__被导入的时候执行是模块名
__all__=['方法','方法']在模块前面定义这个 导入的时候只能使用在__all__里面的方法
包 在文件夹下添加文件__init__.py文件 则这个文件夹当成包处理 在文件中用__all__指定能导入的模块
在__init__文件中导入包 py2 import packageName py3 form . import packageName
模块的发布 安装
    建立setup.py
程序传参
import sys
print(sys.argv)
'''
'''
列表推导式
'''
list_test = [i for i in range(20)]
print(list_test)
list_test = [i for i in range(10) for j in range(20, 25)]
print(list_test)
list_test = [(i, j) for i in range(5) for j in range(5, 10)]
print(list_test)
list_test = [(i, j, k) for i in range(5) for j in range(5, 10)
             for k in range(10, 15)]
print(list_test)
'''
集合{} 会自动去重
列表[]
元组()
'''

if __name__ == '__main__':
    print('我不是被导入执行的')
