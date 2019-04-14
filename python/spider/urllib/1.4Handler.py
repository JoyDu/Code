# coding = utf-8
from urllib import request
# 下面代理地址不一定存活
proxy_handle = request.ProxyHandler({
    'https': 'https://110.52.235.68:9999'
})
opener = request.build_opener(proxy_handle)
response = opener.open('http://httpbin.org/get')
print(response.read().decode("utf-8"))