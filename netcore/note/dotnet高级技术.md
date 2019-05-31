---
title: .Net高级技术
date: 2019-05-07 15:19
tags: .Net高级
---

1.密闭类和静态类
---
1.1 密闭类是修饰为sealed的类， sealed不能有子类。一般只有系统中的一些基本类声明为sealed</br>
1.2 静态类：声明为static的类，不能实例化，只能定义static成员。通常用他定义扩展方法</br>
1.3 C#3.0特性：扩展方法。声明静态类，增加一个静态方法，第一个参数是被扩展类型的标记为this，然后在其他类中可以直接调用，本质上还是对静态方法调用提供的一个“语法糖”，也可以用普通静态方法的方式调用，所以不能访问private和protected成员。</br>
eg:为String扩展一个IsEmail方法

    namespace DotNet高级技术
    {
        class Program
        {
            static void Main(string[] args)
            {
                string email = "352834867@qq.com";
                string msg=email.IsEmail()?"True":"False";
                Console.WriteLine(msg);
                Console.ReadKey();
            }
        }

        #region 扩展方法
        static class StringExt
        {
            public static bool IsEmail(this string a)
            {
                return a.Contains("@");
            }
        } 
        #endregion
    }
2.深拷贝，浅拷贝
---
如果拷贝的时候共享被引用的对象就是浅拷贝，如果被引用的对象也拷贝一份出来就是深拷贝。

3.值类型和引用类型
---
3.1 引用类型派生自System.Object (字符串、数组、类、接口)

3.2 值类型均隐式派生自System.ValueType(ValueType其实也是继承自Object，不过是特立独行的一个分支 (int、long、double、float、char）、bool、结构体、枚举)

3.3 区别：

引用类型变量的赋值只复制对对象的引用；引用类型在堆内存（malloc）

值类型变量赋值会拷贝一个副本；值类型在栈内存；值类型一定是sealed

4.拆箱，装箱
---
4.1 值类型赋值给Object类型变量的时候，会发生装箱

4.2 Object类型变量赋值给值类型赋值的时候会发生拆箱，需要做显式转换

5.==和Equals
---
5.1 对于值类型来说，==和Equals是等价的都是判断变量内容是否一样

5.2 对于除string类型之外的引用类型来说，Equals判断是否对同一个对象的引用（即堆中的内容是否相同），==比较的是栈的内容是否相同（即是否指向同一个堆中地址）

6. 字符串暂存池（缓冲池）
---
字符串是引用类型，程序中会存在大量的字符串对象，如果每次都创建一个字符串对象，会比较浪费内存、性能低，因此CLR做了“暂存池”(拘留池，缓冲池，暂存池）

    string s1 = "rupeng";
    string s2 = "rupeng";
    string s3 = "ru" + "peng";
    string s4 = new string(s1.ToCharArray());
    string s5 = new string(new char[]{'r','u','p','e','n','g'});
    Console.WriteLine(Object.ReferenceEquals(s1,s2));
    Console.WriteLine(Object.ReferenceEquals(s1, s3));
    Console.WriteLine(Object.ReferenceEquals(s1, s4));
    Console.WriteLine(Object.ReferenceEquals(s1, s5));
    Console.WriteLine(Object.ReferenceEquals(s4, s5));

    //三个字符串对象s1、s2、s3是同一个字符串对象，在内容相同的情况下只有new才能产生一个新的字符串对象

7.ref，out
---
普通参数是“值类型传递拷贝，引用类型传递引用”，但是都不能在函数内部修改外部变量的指向，这时候要用ref或者out(相当于把变量都传进去了），他们的作用不同：ref的作用“方法内部修改外部变量的引用”；out的作用“方法内部给外部变量初始化，相当于一个函数多个返回值”。

7.1 使用ref型参数时，传入的参数必须先被初始化，方法中可以不赋值。对out而言，必须在方法中对其完成初始化，方法外部不用初始化，初始化也没用。

7.2 使用ref和out时，在方法的参数和执行方法时，都要加ref或out关键字。以满足匹配。 

7.3 out适合用在需要retrun多个返回值的地方，而ref则用在需要被调用的方法修改调用者的引用的时候。


