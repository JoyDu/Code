---
title: Razor语法
date: 2019-05-29 15:19
tags: Razor
---

1.1 @符号之后的是C#代码，@{}里面可以是C#代码块，html标签会自动识别为html代码

    @model WebApp.Models.EmployeeModel
    @{
        ViewData["Title"] = "Index";
    }
    @{
        string[] strs = {"zs", "zb", "za"};
        foreach (var s in strs)
        {
            <p>@s</p>
        }
    }
    <h2>@Model.CompanyName</h2>
    <h3>@Model.Name</h3>

1.2 @:被识别为文本，但是不推荐这种写法，可以使用text标签实现并且生成的html代码不会产生任何标签

    @:hello
    <text>hello</text>

1.3 强制识别为C#代码，可用小括号将表达式包裹，但是生成的结果包含括号，表达式的@符号在小括号外面的时候，生成的结果不包含括号

    @{string email="1131416702@qq.com";}

    @*<span>@email.com</span> 编译不通过@*

    <span>无括号@(email).com</span>

    <span>有括号(@email).com</span>

1.4 辅助方法

    变量输出html代码

    @{
        string encodeStr = "<a href='1131416702@qq.com'>Email</a>";
    }
    @encodeStr 输出的是字符串
    @Html.Raw(encodeStr) 输出的是html代码

    

1.5
