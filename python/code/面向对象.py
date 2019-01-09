#coding=utf-8
'''
类
对象：类变量 实例变量 方法
类变量：定义在类中且在函数体之外
实例变量：定义在方法中的变量，只作用于当前实例的类
self：代指自己所在的class
'''


class Student:
    def __init__(self, name):
        #self.__school="WangCangMiddleSchool"
        self.name = name

    def hello(self):
        #print("My name is %s from %s"%(self.name,self.__school))
        print('\n')


Bob = Student("Bob")
Bob.hello()
Bob.name = 'Bob2'
#Bob.__school='TestSchool'#不会生效
Bob.hello()

#访问限制 内部属性不被外部访问，在属性的名称前加上两个下划线 变成私有变量 只有内部可以访问


#Getter Setter
#封装 继承 多态
class PrimaryStudent(Student):
    home = 'sichuan'

    def __init__(self, girlfriend, name):
        #super(PrimaryStudent,self).__init__(name)
        self.__school = 'Social'
        self.name = name
        self.girlfriend = girlfriend

    def lol(self):
        print("sala")

    def ShowMe(self):
        print('My name is %s from %s ,%s is my girlfriend' %
              (self.name, self.__school, self.girlfriend))


Tim = PrimaryStudent('Mini', 'Tim')
print(Tim._PrimaryStudent__school)
Tim.hello()
Tim.lol()
Tim.ShowMe()
#多类继承
#当本身的类是经典类的时候，就按照深度优先方式查找继承的方法 （即，找到一个爸爸，继续找这个爸爸的爸爸，爸爸的爸爸的爸爸。。。）
#当本身的类是新式类的时候，就按照广度优先的方式查找 （即，找到一个爸爸，再找下一个爸爸，再找下一个爸爸，平辈之间查找）

#多态 鸭子类型 只要是能“不报错运行”的类型，都可以塞进参数中去
#type(obj)获取对象类型
#isinstance(object,type)判断对象是否是type类型 包含继承关系
#dir(object)获取对象所有属性和方法
#setattr(obj,attribute,value)设置属性和值
#getattr(obj,attribute，defaultValue)判断是否包含指定属性，传递默认值不存在指定属性时返回
print(type(Tim))  #获取对象的类型
print(isinstance(Tim, Student))
print(dir(Tim))
print(setattr(Tim, 'age', 20))
print(getattr(Tim, 'age', 404))
print(Tim.age)
#实例属性比类属性优先级高 会屏蔽掉类属性 但是类属性一样的可以访问
Tim.home = 'chengdu'
print(Tim.home)
print(PrimaryStudent.home)
del (Tim.home)
print(Tim.home)
'''
模块和包
    包是由一系列模块组成的集合。模块是处理某一类问题的函数和类的集合。
    包必须至少含有一个__int__.py文件，该文件的内容可以为空。__int__.py用于标识当前文件夹是一个包。
使用from-import语句导入模块的属性
单行导入
from module import name1,name2,name3
多行导入
from module import name1,name2,name3
'''
