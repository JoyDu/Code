---
title: python爬虫知识
date: 2019-04-19 12:20
tags: python,requests,spider,爬虫
---
## Requests模块

### 1.请求方式
    requests.post("http://httpbin.org/post")
    requests.put("http://httpbin.org/put")
    requests.delete("http://httpbin.org/delete")
    requests.get("http://httpbin.org/get")
    requests.options("http://httpbin.org/options")

### 2.Get请求
    # 基本Get请求
    response = requests.get("http://httpbin.org/get?name=lily&age=22")
    print(response.text)

    # 带参数Get请求
    data = {'name': "germey", 'age': 22}
    response = requests.get("http://httpbin.org/get", params=data)
    print(response.text)

    # json解析
    response = requests.get("http://httpbin.org/get")
    print(type(response.text))
    print(response.json())
    print(json.loads(response.text))
    print(type(response.json()))

    # 获取二进制数据
    response = requests.get("https://github.com/favicon.ico")
    print(type(response.text),type(response.content))
    print(response.text)
    print(response.content)
    with open("favicon.ico","wb") as file:
        file.write(response.content)
        file.close()

    # 添加headers
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
    }
    response = requests.get("http://www.zhihu.com/explore",headers=headers)
    print(response.text)

### 3.Post请求
    # 基本Post请求
    data = {'name': 'germey', 'age': '22'}
    headers = {
        'User-Agent':
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
    }
    response = requests.post("http://httpbin.org/post", data=data, headers=headers)
    print(response.json())

    # response属性
    response = requests.get('http://www.jianshu.com')
    print(type(response.status_code), response.status_code)
    print(type(response.headers), response.headers)
    print(type(response.cookies), response.cookies)
    print(type(response.url), response.url)
    print(type(response.history), response.history)

    # 状态码判断
    response = requests.get('http://www.jianshu.com/hello.html')
    exit() if not response.status_code == requests.codes.not_found else print('404 Not Found')

    response = requests.get('http://www.jianshu.com')
    exit() if not response.status_code == 200 else print('Request Successfully')

    # 文件上传
    files = {'file': open('favicon.ico', 'rb')}
    response = requests.post("http://httpbin.org/post", files=files)
    print(response.text)

    # 获取cookie
    response = requests.get("https://www.baidu.com")
    print(response.cookies)
    for key, value in response.cookies.items():
        print(key + " = " + value)

    # 会话维持(模拟登陆)
    requests.get("http://httpbin.org/cookies/set/number/123456789")
    response = requests.get("http://httpbin.org/cookies")
    print(response.text)

    s = requests.Session()
    s.get("http://httpbin.org/cookies/set/number/123456789")
    response = s.get("http://httpbin.org/cookies")
    print(response.text)

    # 代理设置
    proxies = {
    "http": "http://127.0.0.1:9743",
    "https": "https://127.0.0.1:9743",
    }
    response = requests.get("https://www.taobao.com",proxies=proxies)
    print(response.status_code)

    proxies = {
        "http": "http://user:password@127.0.0.1:9743/",
    }
    response = requests.get("https://www.taobao.com", proxies=proxies)
    print(response.status_code)

    # 超时设置
    from requests.exceptions import ReadTimeout
    try:
        response = requests.get("http://httpbin.org/get", timeout = 0.5)
        print(response.status_code)
    except ReadTimeout:
        print('Timeout')

    # 认证设置
    from requests.auth import HTTPBasicAuth

    r = requests.get('http://120.27.34.24:9001', auth=HTTPBasicAuth('user', '123'))
    print(r.status_code)

    r = requests.get('http://120.27.34.24:9001', auth=('user', '123'))
    print(r.status_code)

    # 异常处理
    from requests.exceptions import ReadTimeout, ConnectionError, RequestException
    try:
        response = requests.get("http://httpbin.org/get", timeout = 0.5)
        print(response.status_code)
    except ReadTimeout:
        print('Timeout')
    except ConnectionError:
        print('Connection error')
    except RequestException:
        print('Error')

