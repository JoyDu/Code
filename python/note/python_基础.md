---
title: python基础知识
date: 2018-05-20 19:42
tags: python
---
注释
---
    文件头加：# -*- coding:utf-8 -*-设置编码方式为utf-8支持中文
    #单行注释
    '''多行注释'''
数据类型
---
    值类型：
    Number {int,long(长整型),float,complex(复数)}
    Bool
    String
    Tuple(元组)创建后不能被修改,eg:('physics', 'chemistry', 1997, 2000)

    引用类型:
    List(列表)即数组,eg:['12', '3rr']
    Dictionary(字典)可存储任何数据类型，eg：d = {key1 : value1, key2 : value2 }
格式化输出
---
    格式符号	转换
    %c	       字符
    %s	       通过str() 字符串转换来格式化
    %i	       有符号十进制整数
    %d	       有符号十进制整数
    %u	       无符号十进制整数
    %o	       八进制整数
    %x	       十六进制整数（小写字母）
    %X	       十六进制整数（大写字母）
    %e	       索引符号（小写'e'）
    %E	       索引符号（大写“E”）
    %f	       浮点实数
    %g	       ％f和％e的简写
    %G	       ％f和％E的简写

    eg：
    name="Bob"
    age=12
    print("my name is %s"%name)
    print("my name is %s,I'm %d years old."%(name,age))
输入
---
    python2：
    raw_input("提示信息") 输入的所有内容都被当做字符串处理
    input("提示信息") 只接受输入表达式
    python3:
    无raw_input函数
    input("提示信息")作用同python2的功能
算数运算符
---
    运算符	描述	实例
        +	加	两个对象相加 a + b 输出结果 30
        -	减	得到负数或是一个数减去另一个数 a - b 输出结果 -10
        *	乘	两个数相乘或是返回一个被重复若干次的字符串 a * b 输出结果 200
        /	除	x除以y b / a 输出结果 2
        //	取整除	返回商的整数部分 9//2 输出结果 4 , 9.0//2.0 输出结果 4.0
        %	取余	返回除法的余数 b % a 输出结果 0
        **	幂	返回x的y次幂 a**b 为10的20次方， 输出结果 100000000000000000000
赋值运算符
---
    运算符	描述	实例
    =	赋值运算符	把=号右边的结果给左边的变量 num=1+2*3 结果num的值为7
复合赋值运算符
---
    运算符	    描述	    实例
    +=	加法赋值运算符	c += a 等效于 c = c + a
    -=	减法赋值运算符	c -= a 等效于 c = c - a
    *=	乘法赋值运算符	c *= a 等效于 c = c * a
    /=	除法赋值运算符	c /= a 等效于 c = c / a
    %=	取模赋值运算符	c %= a 等效于 c = c % a
    **=	幂赋值运算符	c **= a 等效于 c = c ** a
    //=	取整除赋值运算符	c //= a 等效于 c = c // a
数据类型转换
---
    函数	说明
    int(x [,base ])	将x转换为一个整数
    long(x [,base ])	将x转换为一个长整数
    float(x )	将x转换到一个浮点数
    complex(real [,imag ])	创建一个复数
    str(x )	将对象 x 转换为字符串
    repr(x )	将对象 x 转换为表达式字符串
    eval(str )	用来计算在字符串中的有效Python表达式,并返回一个对象
    tuple(s )	将序列 s 转换为一个元组
    list(s )	将序列 s 转换为一个列表
    chr(x )	将一个整数转换为一个字符
    unichr(x )	将一个整数转换为Unicode字符
    ord(x )	将一个字符转换为它的整数值
    hex(x )	将一个整数转换为一个十六进制字符串
    oct(x )	将一个整数转换为一个八进制字符串
条件语句
---
    if 条件:

    elif 条件:

    else:
关系运算符
---
    运算符	描述	示例
    ==	检查两个操作数的值是否相等，如果是则条件变为真。	如a=3,b=3则（a == b) 为 true.
    !=	检查两个操作数的值是否相等，如果值不相等，则条件变为真。	如a=1,b=3则(a != b) 为 true.
    <>	检查两个操作数的值是否相等，如果值不相等，则条件变为真。	如a=1,b=3则(a <> b) 为 true。这个类似于 != 运算符
    >	检查左操作数的值是否大于右操作数的值，如果是，则条件成立。	如a=7,b=3则(a > b) 为 true.
    <	检查左操作数的值是否小于右操作数的值，如果是，则条件成立。	如a=7,b=3则(a < b) 为 false.
    >=	检查左操作数的值是否大于或等于右操作数的值，如果是，则条件成立。	如a=3,b=3则(a >= b) 为 true.
    <=	检查左操作数的值是否小于或等于右操作数的值，如果是，则条件成立。	如a=3,b=3则(a <= b) 为 true.
逻辑运算符
---
    运算符	逻辑表达式	描述	实例
    and 	x and y	布尔"与" - 如果 x 为 False，x and y 返回 False，否则它返回 y 的计算值。	(a and b) 返回 20。
    or  	x or y	布尔"或" - 如果 x 是 True，它返回 True，否则它返回 y 的计算值。	(a or b) 返回 10。
    not 	not x	布尔"非" - 如果 x 为 True，返回 False 。如果 x 为 False，它返回 True。	not(a and b) 返回 False
循环语句
---
     while 条件:
        条件满足时，做的事情1
        条件满足时，做的事情2
        条件满足时，做的事情3
        ...(省略)...

    for 临时变量 in 列表或者字符串等:
        循环满足条件时执行的代码
    else:
        循环不满足条件时执行的代码

    break/continue只能用在循环中，除此以外不能单独使用
    break/continue在嵌套循环中，只对最近的一层循环起作用
切片
---
    切片的语法：[起始:结束:步长]
    注意：选取的区间属于左闭右开型，即从"起始"位开始，到"结束"位的前一位结束（不包含结束位本身)。
字符串操作
---
    mystr.find(str, start=0, end=len(mystr)) 检测 str 是否包含在 mystr中，如果不包含返回-1
    mystr.index(str, start=0, end=len(mystr)) 检测 str 是否包含在 mystr中，如果不包含报异常ValueError
    mystr.count(str, start=0, end=len(mystr)) 返回 str在start和end之间 在 mystr里面出现的次数
    mystr.replace(str1, str2,  mystr.count(str1)) 把 mystr 中的 str1 替换成 str2,如果 count 指定，则替换不超过 count 次.
    mystr.split(str=" ", 2) 以 str 为分隔符切片 mystr，如果 maxsplit有指定值，则仅分隔 maxsplit 个子字符串
    mystr.capitalize() 字符串第一个字母大写
    mystr.title() 字符串每个单词首字母都大写
    mystr.startswith(obj) 检查字符串是否是以 obj 开头, 是则返回 True，否则返回 False
    mystr.endswith(obj) 检查字符串是否是以 obj 结尾, 是则返回 True，否则返回 False
    mystr.lower() 大写转换成小写
    mystr.upper() 转换 mystr 中的小写字母为大写
    mystr.ljust(width) 返回一个原字符串左对齐,并使用空格填充至长度 width 的新字符串
    mystr.rjust(width) 返回一个原字符串右对齐,并使用空格填充至长度 width 的新字符串
    mystr.center(width) 返回一个原字符串居中,并使用空格填充至长度 width 的新字符串
    mystr.lstrip() 删除 mystr 左边的空白字符
    mystr.rstrip() 删除 mystr 字符串末尾的空白字符
    mystr.strip() 删除mystr字符串两端的空白字符
    mystr.rfind(str, start=0,end=len(mystr)) 从右边开始查找
    mystr.rindex( str, start=0,end=len(mystr)) 类似于 index()，不过是从右边开始.
    mystr.partition(str) 把mystr以str分割成三部分,str前，str和str后
    mystr.rpartition(str) 类似于 partition()函数,不过是从右边开始
    mystr.splitlines()  按照行分隔，返回一个包含各行作为元素的列表
    mystr.isalpha()  如果 mystr 所有字符都是字母 则返回 True,否则返回 False
    mystr.isdigit()  mystr 只包含数字则返回 True 否则返回 False
    mystr.isalnum() mystr 所有字符都是字母或数字则返回 True,否则返回 False
    mystr.isspace() mystr 中只包含空格，则返回 True，否则返回 False.
    mystr.join(str) mystr 中每个字符后面插入str,构造出一个新的字符串

列表的相关操作
---
    demo:['xiaoxiang'，'xiaowang']
    append() 可以向列表添加元素   
    extend() 将另一个集合中的元素逐一添加到列表中
    insert(index, object) 在指定位置index前插入元素object
    通过下表修改元素
    in（存在）,如果存在那么结果为true，否则为false
    not in（不存在），如果不存在那么结果为true，否则false
    index
    count
    del 根据下标进行删除
    pop 删除最后一个元素
    remove 根据元素的值进行删除
    sort方法是将list按特定顺序重新排列，默认为由小到大，参数reverse=True可改为倒序，由大到小。
    reverse方法是将list逆置

元组的相关操作
---
    demo:tuple=('st',12,34)
    元组的元素不能修改
    count
    index
字典的相关操作
---
    demo:dictionary={'name':'zhangsan','age':16}
    dictionary['name']='lisi'修改元素
    del 删除元素  del dictionary['name']
    del dictionary删除字典
    clear() 清空字典
    len(dictionary)键值对的个数
    dictionary.keys()获取包含所有key的列表
    dictionary.values()包含所有value的列表
    dictionary.items()包含所有键值对元组的列表
    dictionary.has_key(key)判断键是否在字典中

公共方法之运算符
---
    运算符	Python 表达式	结果	描述	支持的数据类型
    +	[1, 2] + [3, 4]	[1, 2, 3, 4]	合并	字符串、列表、元组
    *	'Hi!' * 4	['Hi!', 'Hi!', 'Hi!', 'Hi!']	复制	字符串、列表、元组
    in	3 in (1, 2, 3)	True	元素是否存在	字符串、列表、元组、字典
    not in	4 not in (1, 2, 3)	True	元素是否不存在	字符串、列表、元组、字典

公共方法之Python内置函数
---
    序号	    方法	          描述
    1	cmp(item1, item2)	比较两个值
    2	len(item)	计算容器中元素个数
    3	max(item)	返回容器中元素最大值
    4	min(item)	返回容器中元素最小值
    5	del(item)	删除变量
可变类型与不可变类型
---
    可变类型，值可以改变：内容可被修改
    列表 list
    字典 dict
    
    不可变类型，值不可以改变：内容不可被修改，只是改变了引用指向
    数值类型 int, long, bool, float
    字符串 str
    元组 tuple

函数
---
    def 函数名():
        代码
返回值
---
    demo:
    def getRes():
        return 1,2
    a,b=getRes()
    可以返回多个值(本质是利用了元组)

函数参数
---
    缺省参数：参数指定默认值，位于参数列表的最后，相当于C#的可选参数


    不定长参数：
    def functionname([formal_args,] *args, **kwargs):
       "函数_文档字符串"
       function_suite
       return [expression]
    加了星号（*）的变量args会存放所有未命名的变量参数，args为元组；而加**的变量kwargs会存放命名参数，即形如key=value的参数， kwargs为字典
    demo：
    def fun(a, b, *args, **kwargs):
    ...     """可变参数演示示例"""
    ...     print "a =", a
    ...     print "b =", b
    ...     print "args =", args
    ...     print "kwargs: "
    ...     for key, value in kwargs.items():
    ...         print key, "=", value
    ...
    >>> fun(1, 2, 3, 4, 5, m=6, n=7, p=8) 


    引用传参：
    Python中函数参数是引用传递（注意不是值传递）。对于不可变类型，因变量不能修改，所以运算不会影响到变量自身；而对于可变类型来说，函数体中的运算有可能会更改传入的参数变量。

匿名函数
---
    lambda [arg1 [,arg2,.....argn]]:expression
    sum = lambda arg1,arg2:arg1*arg2
    print('sum = %d'%sum(arg1,arg2))

    eg:
    stus = [
        {"name":"zhangsan", "age":18}, 
        {"name":"lisi", "age":19}, 
        {"name":"wangwu", "age":17}
    ]
    stus.sort(key=lambda x:x['name'])
文件操作
---
    访问模式	说明
    r	以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。
    w	打开一个文件只用于写入。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
    a	打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
    rb	以二进制格式打开一个文件用于只读。文件指针将会放在文件的开头。这是默认模式。
    wb	以二进制格式打开一个文件只用于写入。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
    ab	以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
    r+	打开一个文件用于读写。文件指针将会放在文件的开头。
    w+	打开一个文件用于读写。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
    a+	打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。
    rb+	以二进制格式打开一个文件用于读写。文件指针将会放在文件的开头。
    wb+	以二进制格式打开一个文件用于读写。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
    ab+	以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。如果该文件不存在，创建新文件用于读写。

    write()写入数据
    read(num)读数据，num可选参数标识要从文件中读取的字节长度
    readlines()按行读取所有数据
    eg:
    f=open('test.txt','r')#打开文件
    f.close()#关闭文件

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