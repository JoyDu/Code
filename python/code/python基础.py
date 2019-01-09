# coding=utf-8
import keyword
# 查看python关键字
print(keyword.kwlist)
# 输出
print("my name is %s,age %d" % ("joydu", 12))
# 换行输出
print("姓名：joydu\n年龄：18")
# 输入
# python2中raw_input()用户的任何输入都当成字符串处理 input()接受的输入必须是表达式
# python3中只有input()用户的任何输入都当成字符串处理
name = input("请输入姓名：")
print(type(name))
print("name:%s" % name)

# if语句
if_age = 18
if if_age >= 18:
    print("我已经成年了")
elif if_age < 18:
    print("我还未成年")
else:
    print("我不告诉你")
# 逻辑运算符 and or not

# 切片[起始:结束:步长]
strings = "abcdef"
print("strings[5:1]%s" % strings[5:1])
print("strings[::-1]%s" % strings[::-1])

# 字符串的常见操作
print('e index %d' % strings.find('e'))

print("b index %d" % strings.index('b'))