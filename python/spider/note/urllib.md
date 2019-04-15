---
title: python爬虫知识
date: 2019-04-19 12:20
tags: python,urllib,spider,爬虫
---
## Urllib模块

1. urllib.request     请求模块
2. urllib.error       异常处理模块
3. urllib.parse       url解析模块 
4. urllib.robotparser robots.txt解析模块

### 1.urllib.request

#### 1.1 urlopen
    # coding=utf-8
    # urllib.request.urlopen(url,data=None,[timeout, ]*,cafile=None,cadefault=False,context=None)
    import urllib.request
    import urllib.parse
    import urllib.error
    import socket

    # get提交数据
    print('get提交数据')
    response = urllib.request.urlopen("http://www.baidu.com")
    print(response.read().decode('utf-8'))
    print('========================================================================')

    # post提交数据
    print('post提交数据')
    data = bytes(urllib.parse.urlencode({'word': 'hello'}), encoding="utf8")
    # 按照utf8编码格式封装需要post的数据
    response = urllib.request.urlopen('http://httpbin.org/post', data=data)
    print(response.read())
    print('========================================================================')

    # 设置超时
    print('设置超时')
    response = urllib.request.urlopen("http://httpbin.org/get", timeout=1)
    print(response.read().decode('utf-8'))
    print('========================================================================')

    # 捕获报错
    print('捕获报错')
    try:
        response = urllib.request.urlopen("http://httpbin.org/get", timeout=0.1)
    except urllib.error.URLError as e:
        print(e)
        if isinstance(e.reason, socket.timeout):
            print('TIME OUT')
    print('========================================================================')
#### 1.2 Response
    # coding = utf-8
    import urllib.request
    response = urllib.request.urlopen('http://www.python.org')

    # 响应类型 http.client.HTTPResponse
    print(type(response))

    print("Status:", response.status)
    print("Headers:", response.getheaders())
    print("Server", response.getheader('Server'))

#### 1.3 Request
    # coding = utf-8
    from urllib import request, parse
    # 添加headers的两种方式
    url = 'http://httpbin.org/post'
    headers = {
        'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
        'Host': 'httpbin.org'
    }
    dict = {'name': 'Germey'}
    data = bytes(parse.urlencode(dict), encoding='utf8')
    req = request.Request(url=url, data=data, headers=headers, method="POST")
    response = request.urlopen(req)
    print(response.read().decode("utf-8"))
    print("===========================================================")

    req=request.Request(url=url,data=data,method="POST")
    req.add_header('User-Agent','Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)')
    response = request.urlopen(req)
    print(response.read().decode("utf-8"))
    print("===========================================================")
#### 1.4 Handler(代理)
    # coding = utf-8
    from urllib import request
    # 下面代理地址不一定存活
    proxy_handle = request.ProxyHandler({
        'https': 'https://110.52.235.68:9999'
    })
    opener = request.build_opener(proxy_handle)
    response = opener.open('http://httpbin.org/get')
    print(response.read().decode("utf-8"))

#### 1.5 Cookie
    # coding = utf-8
    import http.cookiejar
    import urllib.request
    # 获取cookie
    cookie = http.cookiejar.CookieJar()
    handler = urllib.request.HTTPCookieProcessor(cookie)
    opener = urllib.request.build_opener(handler)
    response = opener.open('http://www.baidu.com')
    for item in cookie:
        print(item.name + "=" + item.value)
    print("========================================================")

    # 将cookie写入到文件
    cookiefile = "cookie.txt"
    cookie = http.cookiejar.MozillaCookieJar(cookiefile)
    handler = urllib.request.HTTPCookieProcessor(cookie)
    opener = urllib.request.build_opener(handler)
    response = opener.open("http://www.baidu.com")
    # ignore_discard的意思是即使cookies将被丢弃也将它保存下来
    # ignore_expires的意思是如果cookies已经过期也将它保存并且文件已存在时将覆盖
    cookie.save(ignore_discard=True, ignore_expires=True)

    cookiefile = "cookie.txt"
    cookie = http.cookiejar.LWPCookieJar(cookiefile)
    handler = http.request.HTTPCookieProcessor(cookie)
    opener = urllib.request.build_opener(handler)
    response = opener.open("http://www.baidu.com")
    cookie.save(ignore_discard=True, ignore_expires=True)

    # 从文件加载cookie信息
    cookiefile = "cookie.txt"
    cookie = http.cookiejar.LWPCookieJar()
    cookie.load(cookiefile,ignore_discard=True,ignore_expires=True)
    handler = urllib.request.HTTPCookieProcessor(cookie)
    opener = urllib.request.build_opener(handler)
    opener.open("http://www.baidu.com")
    print(response.read().decode("utf-8"))

#### 2.1 urllib.erro

    # coding=utf-8
    from urllib import request, error
    # urllib.URLErro
    # 没有网络连接
    # 服务器连接失败
    # 找不到指定的服务器
    try:
        response = request.urlopen("http://www.baidu.com", timeout=0.01)
    except error.URLError as e:
        print(e.reason)
    print("=============================================================")

    # urllib.HTTPError
    # HTTPError是URLError的子类，发出请求时，服务器上都会对应一个response应答对象，其中它包含一个数字"响应状态码"。
    # 如果urlopen或opener.open不能处理的，会产生一个HTTPError，对应相应的状态码，HTTP状态码表示HTTP协议所返回的响应的状态。
    # URLError是HTTPErro的父类，所以HTTPErro写在前面，先捕获子类的异常
    try:
        response = request.urlopen("http://cuiqingcai.com/index.html")
    except error.HTTPError as e:
        print(e.reason)
    except error.URLError as e:
        print(e.reason)
    else:
        print("Request Successfully")
    print("=============================================================")

#### 3.1 urlparse
    # coding=utf-8
    from urllib import request, parse

    # 分解url
    # urllib.parse.urlparse(urlstring, scheme='', allow_fragments=True)
    # allow_fragments 是否加载片段参数默认为true
    # scheme='http/https'替换url协议类型，如果url中存在则不替换
    result = parse.urlparse("http://www.baidu.com/index.html;user?id=5#comment")
    print(type(result), result)

    result = parse.urlparse('www.baidu.com/index.html;user?id=5#comment', scheme='https')
    print(result)

    result = parse.urlparse('http://www.baidu.com/index.html;user?id=5#comment', allow_fragments=False)
    print(result)
#### 3.2 urlunparse
    from urllib.parse import urlunparse

    # 拼接url
    data = ['http', 'www.baidu.com', 'index.html', 'user', 'a=6', 'comment']
    print(urlunparse(data))

#### 3.3 urljoin
    from urllib.parse import urljoin
    # 组合url
    print(urljoin('http://www.baidu.com', 'FAQ.html'))
    print(urljoin('http://www.baidu.com', 'https://cuiqingcai.com/FAQ.html'))
    print(urljoin('http://www.baidu.com/about.html', 'https://cuiqingcai.com/FAQ.html'))
    print(urljoin('http://www.baidu.com/about.html', 'https://cuiqingcai.com/FAQ.html?question=2'))
    print(urljoin('http://www.baidu.com?wd=abc', 'https://cuiqingcai.com/index.php'))
    print(urljoin('http://www.baidu.com', '?category=2#comment'))
    print(urljoin('www.baidu.com', '?category=2#comment'))
    print(urljoin('www.baidu.com#comment', '?category=2'))

#### 3.4 urlencode
    from urllib.parse import urlencode

    params = {
        'name': 'germey',
        'age': 22
    }
    base_url = 'http://www.baidu.com?'
    url = base_url + urlencode(params)
    print(url)