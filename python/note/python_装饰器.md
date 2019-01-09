---
title: python装饰器
date: 2018-06-20 19:42
tags: python
---
装饰器原理
---
    # 闭包解释装饰器原理
    def decoratorFun(func):
        def checkPermissions():
            print("执行权限检测")
            func()
        return checkPermissions
    def proc1():
        print("逻辑处理1")

    def proc2():
        print("逻辑处理2")

    proc_ret = decoratorFun(proc1)
    proc_ret()
装饰器实例
---
    def decoratorFun(func):
        def checkPermissions():
            print("执行权限检测")
            func()
        return checkPermissions
    @decoratorFun
    def proc3():
        print("逻辑处理3")

多个装饰器
---
    # 代码执行到装饰器的时候就进行装饰，并不是调用方法的时候才进行装饰
    def makeBold(func):
        print("---makebold---")
        def wrapped():
            return "<b>" + func() + "</b>"

        return wrapped


    def makeItalic(func):
        print("---makeItalic---")
        def wrapped():
            return "<i>" + func() + "</i>"

        return wrapped


    @makeBold
    @makeItalic
    def getNode():
        print("---getNode---")
        return "Hello World"


    nodeRet = getNode()
    print(nodeRet)

装饰器装饰无参函数
---
    def func_NoParam(functionName):
        print("---func_NoParam---1---")
        def func_in():
            print("---func_NoParam_in---1---")
            functionName()
            print("---func_NoParam_in---2---")

        print("---func_NoParam---2---")
        return func_in

    @func_NoParam
    def decorator_NoParam():
        print("----decorator_NoParam----")
    decorator_NoParam()

装饰器装饰有参函数
---
    def decorator_Param(func):
        print("---decorator_Param1---")

        def decorator_Param_In(a, b):
            print("---decorator_Param_in1---")
            func(a, b)
            print("---decorator_Param_in2---")

        print("---decorator_Param2---")
        return decorator_Param_In


    @decorator_Param
    def func_Param(a, b):
        print("---func_Param---")
        print("a：%d，b：%d" % (a, b))


    func_Param(8, 9)

装饰器装饰有返回值的函数
---
    def decorator_return(func):
        def dec_return():
            print("---decorator_return_in_1---")
            ret = func()
            print("---decorator_return_in_2---")
            return ret

        return dec_return


    @decorator_return
    def func_return():
        print("---func_return---")
        return "func_return已执行"


    ret_dec_return = func_return()
    print(ret_dec_return)

通用装饰器
---
    def decorator_general(func):
        def dec_general(*args, **kwargs):
            print("---decorator_general_in_1---")
            ret = func(*args, **kwargs)
            print("---decorator_general_in_2---")
            return ret

        return dec_general


    @decorator_general
    def func_general(a, b, c):
        print("---a:%d,b:%d,c%d---" % (a, b, c))
        return a + b + c


    general_ret = func_general(1, 2, 3)
    print("通用装饰器返回值：%d" % general_ret)

带有参数的装饰器
---
    def decorator_arg(arg):
        def decorator_arg_func(func):
            def dec_arg_in():
                print("带参装饰器arg:%d" % arg)
                if (arg > 0):
                    func()
                else:
                    print("arg必须大于零")

            return dec_arg_in

        return decorator_arg_func


    @decorator_arg(3)
    def func_dec_arg():
        print("带参装饰器已执行")