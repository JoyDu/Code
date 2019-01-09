---
title: java基础
date: 2018-11-11 13:16
tags: java
---
java环境配置
---
        jre:java运行环境
        jdk:java开发包和jre 
        系统变量中：添加Java_Home  C:\Program Files\Java\jdk1.8.0_131(取相对实际安装目录的路径)
                   添加CLASSPATH  .;%Java_Home%\bin;%Java_Home%\lib\dt.jar;%Java_Home%\lib\tools.jar
                   path中添加     %Java_Home%\bin;%Java_Home%\jre\bin;
数据类型
---
        四类八种
        
		*四类	八种	字节数	数据表示范围
		*整型   byte	1	-128～127
		        short	2	-32768～32767			
                    int	4	-2147483648～2147483648			
                    long	8	-263～263-1
		*浮点型	float	4	-3.403E38～3.403E38
		        double	8	-1.798E308～1.798E308
		*字符型	char	2	表示一个字符，如('a'，'A'，'0'，'家')
		*布尔型	boolean	1	只有两个值true与false
        <b>注意：java中String是对象,是引用类型不属于基础数据类型,且没有string</b>
数据类型转换
---
        自动转换：小转大
        强制转换：大转小，会丢失精度 
        double p = 3.1415926;
        int i = (int)p;
        System.out.println(i)/*输出结果：3*/
运算符
---
        * A: 常见操作
		运算符	运算规则	        范例		结果
		+	正号		+3		3
		+	加		2+3		5
		+	连接字符串	“中”+“国”	“中国”
		-	负号		int a=3;-a	-3
		-	减		3-1		2
		*	乘		2*3		6
		/	除		5/2		2
		%	取模		5/2		1
		++	自增		int a=1;a++/++a	2
		--	自减		int b=3;a--/--a	2
	    * B: 注意事项
		*a:加法运算符在连接字符串时要注意，只有直接与字符串相加才会转成字符串。
		*b:除法“/”当两边为整数时，取整数部分，舍余数。当其中一边为浮点型时，按正常规则相除。 
		*c:“%”为整除取余符号，小数取余没有意义。结果符号与被取余符号相同。
		*d:整数做被除数，0不能做除数，否则报错。
		*e:小数做被除数，整除0结果为Infinity，对0取模结果为NaN
        *INFINITY为无限 NaN为非数字
赋值运算符
---
		运算符	运算规则	范例		结果
		=	赋值		int a=2	    2
		+=	加后赋值	int a=2，a+=2	4
		-=	减后赋值	int a=2，a-=2	0
		*=	乘后赋值	int a=2，a*=2	4
		/=	整除后赋值	int a=2，a/=2	1
		%=	取模后赋值	int a=2，a%=2	0
比较运算符
---
        比较运算符的使用
		运算符	运算规则	范例	结果
		==	相等于		4==3	False
		!=	不等于		4!=3	True
		<	小于		4<3	False
		>	大于		4>3	True
		<=	小于等于	4<=3	False
		>=	大于等于	4>=3	True
逻辑运算符
---
        运算符	运算规则	范例		结果
		&	与		false&true	False
		|	或		false|true	True
		^	异或		true^flase	True
		!	非		!true		Flase
		&&	短路与		false&&true	False
		||	短路或		false||true	True
        <b>&& ||只要其中有一边为false就不会继续执行</b>
三元运算符
---
        (条件表达式)？表达式1：表达式2；/*同C#*/
用户录入
---
        /*
        导入工具类util中的Scanner
        接收用户录入信息
        sc.nextInt()只接收整数数据
        sc.next()只接收字符串数据
        */
        import java.util.Scanner;
        public class ScannerDemo{
            public static void main(String[] args){
                Scanner sc=new Scanner(System.in);
                System.out.println("请录入一个整数：");
                int i=sc.nextInt();
                System.out.println(i);
                System.out.println("请录入一个字符串：");
                String s=sc.next();
                System.out.println(s);
            }
        }
生成随机数
---
        /*
        Random 工具类之随机生成
        nextInt(取值范围)
        nextDouble()不支持设置取值范围，只能取[0.0,1.0)
        */
        import java./.Random;
        public class RandomDemo{
            public static void main(String[] args){
                Random rd=new Random();
                int i = rd.nextInt(100);
                System.out.println(i);
                double d=rd.nextDouble();
                System.out.println(d);
            }
        }
结构语句
---
        条件结构
        if(条件表达式) {}；
        if(条件表达式){} else {};
        if(条件表达式){} else if(条件表达式) {} else if(条件表达式){} ...... else{}

        switch结构
        switch(需要进行比较的元素) {
                        case 条件:
                            语句;
                            break;
                        case 条件:
                            语句;
                            break;
                        ......
                    default:
                        语句;
                        break;
                    };
循环语句
---
        循环结构for语句的格式：      
    　　for(初始化表达式;条件表达式;循环后的操作表达式) {
    　　　　　循环体;   
    　　    }
        while(判断条件语句) {
    　　　　　　循环体语句;
    　　　　　　控制条件语句;
    　　　}
        do {
    　　　　　　循环体语句;
    　　　　　　控制条件语句;
    　　　　}while(判断条件语句);
        /*1.do...while循环至少执行一次循环体.
    　　2.而for,while循环必须先判断条件是否成立，然后决定是否执行循环体语句.*/
数组
---
        数据类型[] 变量名=new 数据类型[length];
        数据类型[] 变量名=new 数据类型[]{元素,元素....};
        数据类型[] 变量名={元素,元素......}
        
        