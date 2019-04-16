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
<p>1.可以选择是否将请求传递到管道中的下一个组件。</p>
<p>2.可在调用管道中的下一个组件前后执行工作。</p>
<p><b>Microsoft.AspNetCore.Diagnostics</b> 异常处理包可以用于异常处理，异常显示页面和诊断信息的 ASP.NET Core 中间件</p>
    using System;
    using System.Collections.Generic;
    using System.Linq;
    using System.Threading.Tasks;
    using Microsoft.AspNetCore.Builder;
    using Microsoft.AspNetCore.Hosting;
    using Microsoft.AspNetCore.Http;
    using Microsoft.Extensions.DependencyInjection;
    using Microsoft.Extensions.Configuration;
    using Microsoft.AspNetCore.Diagnostics;//引用异常处理

    namespace test
    {
        public class Startup
        {
            public IConfiguration Configuration{get;set;}
            public Startup()
            {
                var builder=new ConfigurationBuilder().AddJsonFile("AppSettings.json");
                Configuration=builder.Build();
            }
            // This method gets called by the runtime. Use this method to add services to the container.
            // For more information on how to configure your application, visit https://go.microsoft.com/fwlink/?LinkID=398940
            public void ConfigureServices(IServiceCollection services)
            {
            }

            // This method gets called by the runtime. Use this method to configure the HTTP request pipeline.
            public void Configure(IApplicationBuilder app, IHostingEnvironment env)
            {
                if (env.IsDevelopment())
                {
                    app.UseDeveloperExceptionPage();
                }
                //使用欢迎页面
                app.UseWelcomePage();
                app.Run(async (context) =>
                {
                    var msg=Configuration["message"];
                    //设置响应类型
                    context.Response.ContentType = "text/plain;charset=utf-8";
                    await context.Response.WriteAsync(msg);
                });
            }
        }
    }

ASP.NET Core异常和错误处理
---
    public void Configure(IApplicationBuilder app, IHostingEnvironment env)
    {
        //开发环境下捕获报错，会显示详细报错信息，正式环境下则隐藏了相关文件和报错明细
        if (env.IsDevelopment())
        {
            app.UseDeveloperExceptionPage();
        }
        //使用欢迎页面
        app.UseWelcomePage();
        app.Run(async (context) =>
        {
            new Exception("Throw Exception")
            var msg=Configuration["message"];
            //设置响应类型
            context.Response.ContentType = "text/plain;charset=utf-8";
            await context.Response.WriteAsync(msg);
        });
    }

ASP.NET Core 静态文件
---
<p>JavaScript 文件、图像图形、CSS 样式表文件等,一般存放在wwwroot目录下</p>
<p>UseStaticFiles中间件机制：</p>
<p>1.如果静态文件是一个可以使用的文件，它将返回该文件，而不会尝试调用下一个中间件</p>
<p>2.如果它没有找到匹配的文件，那么将继续调用下一个中间件</p>
<p>UseDefaultFiles中间件在开发环境使用，获取默认起始页，例如Index.html不区分大小写</p>
<p><b>UseDefaultFiles中间件必须在UseStaticFiles中间件的前面</b></p>

    public void Configure(IApplicationBuilder app, IHostingEnvironment env)
    {
        if (env.IsDevelopment())
        {
            app.UseDefaultFiles();
            app.UseDeveloperExceptionPage();
        }
        app.UseStaticFiles();
        //ap.Run(async (context) =>
        //{
        //    var msg=Configuration["message"];
        //    //设置响应类型
        //    context.Response.ContentType = "text/plain;charset=utf-8";
        //    await context.Response.WriteAsync(msg);
        //});
    }

