---
title: .NetCore教程
date: 2019-02-15 11:45
tags: .NetCore
---

vscode开发.netcore常用命令
---
1.dotnet-new 初始化应用程序项目</br>
2.dotnet-restore 还原应用程序的依赖项</br>
3.dotnet-build 生成.netcore应用程序</br>
4.dotnet-publish 发布.netcore应用程序</br>
5.dotnet-run 从源码运行.netcore应用程序</br>
6.dotnet-test 使用project.json中指定的测试工具执行测试</br>
7.dotnet-pack 使用你的代码创建NuGet包</br>

优点
---
1.不再基于System.Web.dll，而是基于一组精细且充分考虑的 NuGet 包</br>
2.内置依赖注入(实现IOC即控制反转的一种方式，<a href="https://www.cnblogs.com/alltime/p/6729295.html">构造方式注入,属性方式注入</a>)

ASP.NET Core 项目配置 ( Startup )
---
Startup类必须是公开的，并且包含以下两个方法</br>
    
    public Class Startup{
        //用于定义应用程序需要的服务，例如ASP.NET Core MVC EF Core和Identity等
        public void ConfigureServices(IServiceCollection services){

        }
    }
    //定义请求管道的中间件，即定义如何响应请求
    public void Configure(IApplicationBuilder app,IHostingEnvironment env){
        if(env.IsDevelopment())
        {
            app.UseDeveloperExceptionPage();
        }
        app.Run(async(context)=>
        {
            await context.Response.WriteAsync("Hello World");
        });
    }

ASP.NET Core中间件
---
<p>一种装配到应用程序管道以处理请求和响应的组件</p>
<p>每个组件：</p>
<p>1.可以选择是否将请求传递到管道中的下一个组件。</br>
2.可在调用管道中的下一个组件前后执行工作。</p>

    


