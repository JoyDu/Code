---
title: .NetCore输出乱码
date: 2019-03-18 23:09
tags: .NetCore 乱码 问题
---
.NetCore输出乱码
---
1.控制台乱码的原因是因为中文windows命令行默认编码页是gb2312，想输出中文只要把控制台的编码页修改成Unicode就可以了。
在cmd里输入chcp 65001再运行程序或者在程序里加一行</br>

Console.OutputEncoding = Encoding.Unicode;</br>

2.网页乱码的原因也是因为程序没有指定编码默认使用Unicode，而中文环境浏览器默认使用gbk。可以通过设置ContentType来告诉浏览器使用utf8.</br>

在await context.Response.WriteAsync("您好，北京欢迎你");前面加上:context.Response.ContentType = "text/plain;charset=utf-8";</br>

只是显示中文的话没有特殊需求的情况下并不需要引用System.Text.Encoding.CodePages</br>
