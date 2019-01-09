---
title: python之面向对象
date: 2018-05-30 21:42
tags: python
---
类
---
    经典类
    class 类名：
        方法列表
    新式类
    class(object) 类名：
        方法列表
    创建对象
    对象名=类名()

    __init__()方法：
    class student:
        def __init__(self):
            pass

    这里的self类似于this指针

    魔法方法：
    def __str__(self):
        msg="实现我就能在print输出对象的时候打印从我这返回的数据"
        return msg
   
    def __del__(self):
        print("当对象被删除时自动调用")
    注意:当变量保存的对象的引用时，此对象的引用计数就会加一，只有当这个对象的引用计数为零才会执行__del__()
   
    def __init__(self):
        print("这里对属性做处理")

    def __new__(cls):
        print("实例化方法时")
        return object.__new__(cls)
    注意：__new__至少要有一个参数cls，代表要实例化的类，此参数在实例化时由Python解释器自动提供
        __new__必须要有返回值，返回实例化出来的实例，这点在自己实现__new__时要特别注意，可以return父类__new__出来的实例，或者直接是object的__new__出来的实例
        __init__有一个参数self，就是这个__new__返回的实例，__init__在__new__的基础上可以完成一些其它初始化的动作，__init__不需要返回值

__new__()实现单例模式
    # 实例化一个单例
    class Singleton(object):
        __instance = None

        def __new__(cls, age, name):
            #如果类数字能够__instance没有或者没有赋值
            #那么就创建一个对象，并且赋值为这个对象的引用，保证下次调用这个方法时
            #能够知道之前已经创建过对象了，这样就保证了只有1个对象
            if not cls.__instance:
                cls.__instance = object.__new__(cls)
            return cls.__instance

    a = Singleton(18, "dongGe")
    b = Singleton(8, "dongGe")

    print(id(a))
    print(id(b))

    a.age = 19 #给a指向的对象添加一个属性
    print(b.age)#获取b指向的对象的age属性


属性封装
---
    类似__name双下划线的为私有属性否则为公有属性
    class People(object):

        def __init__(self, name):
            self.__name = name

        def getName(self):
            return self.__name

        def setName(self, newName):
            if len(newName) >= 5:
                self.__name = newName
            else:
                print("error:名字长度需要大于或者等于5")

    xiaoming = People("dongGe")
    print(xiaoming.__name)
继承
    单继承：
    class Animal(object):

        def __init__(self, name='动物', color='白色'):
            self.__name = name
            self.color = color

        def __test(self):
            print(self.__name)
            print(self.color)

        def test(self):
            print(self.__name)
            print(self.color)



    class Dog(Animal):
        def dogTest1(self):
            #print(self.__name) #不能访问到父类的私有属性
            print(self.color)


        def dogTest2(self):
            #self.__test() #不能访问父类中的私有方法
            self.test()


    A = Animal()
    #print(A.__name) #程序出现异常，不能访问私有属性
    print(A.color)
    #A.__test() #程序出现异常，不能访问私有方法
    A.test()

    print("------分割线-----")

    D = Dog(name = "小花狗", color = "黄色")
    D.dogTest1()
    D.dogTest2()

    注意：
    私有的属性，不能通过对象直接访问，但是可以通过方法访问
    私有的方法，不能通过对象直接访问
    私有的属性、方法，不会被子类继承，也不能被访问
    一般情况下，私有的属性、方法都是不对外公布的，往往用来做内部的事情，起到安全的作用
        
多继承
---
    # 定义一个父类
    class A:
        def printA(self):
            print('----A----')

    # 定义一个父类
    class B:
        def printB(self):
            print('----B----')

    # 定义一个子类，继承自A、B
    class C(A,B):
        def printC(self):
            print('----C----')

    obj_C = C()
    obj_C.printA()
    #----A----
    obj_C.printB()
    #----B----
    
    #当继承类中存在重名方法
    #coding=utf-8
    class base(object):
        def test(self):
            print('----base test----')
    class A(base):
        def test(self):
            print('----A test----')

    # 定义一个父类
    class B(base):
        def test(self):
            print('----B test----')

    # 定义一个子类，继承自A、B
    class C(A,B):
        pass


    obj_C = C()
    obj_C.test() #----A test----

    print(C.__mro__) #可以查看C类的对象搜索方法时的先后顺序
    #(<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class '__main__.base'>, <class 'object'>)
重写父类方法与调用父类方法
---
    重写父类方法：子类中又一个和父类相同名字的方法，会覆盖掉父类中同名的方法
    调用父类方法：
    #coding=utf-8
    class Cat(object):
        def __init__(self,name):
            self.name = name
            self.color = 'yellow'


    class Bosi(Cat):

        def __init__(self,name):
            # 调用父类的__init__方法1(python2)
            #Cat.__init__(self,name)
            # 调用父类的__init__方法2
            #super(Bosi,self).__init__(name)
            # 调用父类的__init__方法3
            super().__init__(name)

        def getName(self):
            return self.name

    bosi = Bosi('xiaohua')

    print(bosi.name)
    print(bosi.color)
多态
---
    python崇尚"鸭子类型"
    #当看到一只鸟走起来像鸭子、游泳起来像鸭子、叫起来也像鸭子，那么这只鸟就可以被称为鸭子
    class F1(object):
        def show(self):
            print 'F1.show'

    class S1(F1):

        def show(self):
            print 'S1.show'

    class S2(F1):

        def show(self):
            print 'S2.show'

    def Func(obj):
        print obj.show()

    s1_obj = S1()
    Func(s1_obj) 

    s2_obj = S2()
    Func(s2_obj)
类属性
    类属性
    类属性就是类对象所拥有的属性，它被所有类对象的实例对象所共有，在内存中只存在一个副本，这个和C++中类的静态成员变量有点类似。对于公有的类属性，在类外可以通过类对象和实例对象访问

    class People(object):
        name = 'Tom'  #公有的类属性
        __age = 12     #私有的类属性

    p = People()

    print(p.name)           #正确
    print(People.name)      #正确
    print(p.__age)            #错误，不能在类外通过实例对象访问私有的类属性
    print(People.__age)        #错误，不能在类外通过类对象访问私有的类属性

实例属性
    class People(object):
        address = '山东' #类属性
        def __init__(self):
            self.name = 'xiaowang' #实例属性
            self.age = 20 #实例属性

    p = People()
    p.age =12 #实例属性
    print(p.address) #正确
    print(p.name)    #正确
    print(p.age)     #正确

    print(People.address) #正确
    print(People.name)    #错误
    print(People.age)     #错误 实例属性不能通过类对象直接访问

    通过实例(对象)去修改类属性
    class People(object):
        country = 'china' #类属性


    print(People.country)#china
    p = People()
    print(p.country)#china
    p.country = 'japan' 
    print(p.country)  #japan    #实例属性会屏蔽掉同名的类属性
    print(People.country)#china
    del p.country    #删除实例属性
    print(p.country)#china
    注意：
    如果需要在类外修改类属性，必须通过类对象去引用然后进行修改。如果通过实例对象去引用，会产生一个同名的实例属性，这种方式修改的是实例属性，不会影响到类属性，并且之后如果通过实例对象去引用该名称的属性，实例属性会强制屏蔽掉类属性，即引用的是实例属性，除非删除了该实例属性

类方法
    是类对象所拥有的方法，需要用修饰器@classmethod来标识其为类方法，对于类方法，第一个参数必须是类对象，一般以cls作为第一个参数（当然可以用其他名称的变量作为其第一个参数，但是大部分人都习惯以'cls'作为第一个参数的名字，就最好用'cls'了），能够通过实例对象和类对象去访问。
    可以访问类属性
    class People(object):
        country = 'china'

        #类方法，用classmethod来进行修饰
        @classmethod
        def getCountry(cls):
            return cls.country

    p = People()
    print p.getCountry()    #可以用过实例对象引用
    print People.getCountry()    #可以通过类对象引用

静态方法
    需要通过修饰器@staticmethod来进行修饰，静态方法不需要多定义参数
    class People(object):
        country = 'china'

        @staticmethod
        #静态方法
        def getCountry():
            return People.country
    print People.getCountry()

类方法 普通方法 静态方法对比
    class Tst:
    name = 'tst'

    data = 'this is data'

    # 普通方法
    def normalMethod(self, name):
        print self.data, name

    # 类方法,可以访问类属性
    @classmethod
    def classMethod(cls, name):
        print cls.data, name

    # 静态方法,不可以访问类属性
    @staticmethod
    def staticMethod(name):
        print name
    
    # error普通方法必须通过实例调用
    # Tst.normalMethod('name')
    Tst.classMethod('name')
    Tst.staticMethod('name')

    总结
        普通方法,可以通过self访问实例属性
        类方法,可以通过cls访问类属性
        静态方法,不可以访问,通过传值的方式，要访问类属性的话必须通过类对象来引用

异常
    捕获异常try...except...
    eg:
    try:
        print('-----test--1---')
        open('123.txt','r')
        print('-----test--2---')
    except IOError:
        pass#产生错误时处理的代码
    else:
        pass#如果没有捕获到异常就执行此处代码
    finally:
        pass#无论是否有异常都会执行的代码

    捕获多个异常
    try:
        print('-----test--1---')
        open('123.txt','r') # 如果123.txt文件不存在，那么会产生 IOError 异常
        print('-----test--2---')
        print(num)# 如果num变量没有定义，那么会产生 NameError 异常

    except (IOError,NameError) as result: 
        #如果想通过一次except捕获到多个异常可以用一个元组的方式

        # errorMsg里会保存捕获到的错误信息
        print(result)

模块
---
    在Python中有一个概念叫做模块（module），这个和C语言中的头文件以及Java中的包很类似，比如在Python中要调用sqrt函数，必须用import关键字引入math这个模块，下面就来了解一下Python中的模块。
    说的通俗点：模块就好比是工具包，要想使用这个工具包中的工具(就好比函数)，就需要导入这个模块

    Import
    import module as newmoduleName #通过as将模块重命名
    eg：
    import math
    print(math.sqrt(2))


    from modname import name1[, name2[, ... nameN]]#只导入模块中指定的函数
    eg:
    from fib import fibonacci
    注意：两个模块中含有相同名称函数的时候，后面一次引入会覆盖前一次引入。


    from … import *导入模块中所有函数


    当你导入一个模块，Python解析器对模块位置的搜索顺序是：
    当前目录
    如果不在当前目录，Python则搜索在shell变量PYTHONPATH下的每个目录。
    如果都找不到，Python会察看默认路径。UNIX下，默认路径一般为/usr/local/lib/python/
    模块搜索路径存储在system模块的sys.path变量中。变量里包含当前目录，PYTHONPATH和由安装过程决定的默认目录。

模块制作
---
    模块的名字就是文件的名字
    为了保证模块在被导入的时候不会执行测试的调用代码，根据__name__变量判断脚本是被引入执行还是直接执行
    if __name__=='main':
        #执行测试代码

    模块中的__all__,类似下面的例子如果文件中有__all__变量则只有变量中的元素可以被from xx import *时导入
    eg:
    __all__=["test1","test2"]
    class Test(object):
        pass
    def test1():
        pass
    def test2():
        pass

Python中的包
---
    __init__.py控制包的导入行为，__init__.py为空仅仅把这个包导入不会导入包中的模块
    __all__定义在__init__中控制着from包名import *时导入的模块
