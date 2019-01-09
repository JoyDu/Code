# coding=utf-8
# 交换值
a = 5
b = 8
a, b = b, a
print("a:%d,b:%d" % (a, b))
'''
斐波拉契数列
'''


def fibla(num):
    a, b = 0, 1
    for i in range(num):
        yield b
        a, b = b, a + b


# fibla(10)
li = fibla(10)
for x in li:
    print(x)
