using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Builder;
using Microsoft.AspNetCore.Hosting;
using Microsoft.AspNetCore.Http;
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Configuration;
using Microsoft.AspNetCore.Diagnostics;

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
                app.UseDefaultFiles();
                app.UseDeveloperExceptionPage();
            }
            app.UseStaticFiles();
            // app.Run(async (context) =>
            // {
            //     var msg=Configuration["message"];
            //     //设置响应类型
            //     context.Response.ContentType = "text/plain;charset=utf-8";
            //     await context.Response.WriteAsync(msg);
            // });
        }
    }
}
