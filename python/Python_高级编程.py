# coding=utf-8
'''
生成器
'''
# 一边循环一边计算的机制称为生成器：generator
li = (x*2 for x in range(10))
for x in li:
    print(x)
#print(next(li))
# 没有更多的元素时，抛出 StopIteration 的异常
'''
yield关键字
'''
# 类似return关键字，但是返回的是生成器
# 调用这个函数时不会立马执行，被迭代时才会执行
'''
send方法
'''
# 参数指定的是上一次被挂起的yield语句的返回值
# send方法和next方法唯一的区别是在执行send方法会首先把上一次挂起的yield语句的返回值通过参数设定
# 在一个生成器对象没有执行next方法之前，由于没有yield语句被挂起，所以执行send方法会报错
print("******************Send***********************")
def testSend():
    value=yield 1
    value=yield value
m=testSend()
print(m.send(None))
print(m.send(2))
'''
生成器应用(斐波拉契数列)
'''
def fibla(num):
    a,b=0,1
    i=0
    while i<num:
        yield b
        a,b=b,a+b
        i+=1
fiblas = fibla(10)
print("*************斐波拉契数列***************")
for x in fiblas:
    print(x)















































    