# coding=utf-8
class Animal(object):
    def __init__(self,newName):
        self.__name=newName
        print("初始化Animal对象")
    # def __new__(cls):
    #     print("实例化Animal对象")
    #     return object.__new__(cls)
    def __str__(self):
        msg="打印Animal对象"
        return msg
    def __del__(self):
        print("删除Animal对象")
animal=Animal("zs")
# print(animal.__name)
print("my mark is %s"%animal)
del animal
# res=input("please input enter")
def selfAdd(num):
    num=num+num
    return num 
num=1
print(selfAdd(num))
print(num)
num_list=[1,2]
print(selfAdd(num_list))
print(num_list)    
stus = [
    {"name":"zhangsan", "age":18}, 
    {"name":"lisi", "age":19}, 
    {"name":"wangwu", "age":17}
]
stus.sort(key=lambda x:x['name'])
print(stus)