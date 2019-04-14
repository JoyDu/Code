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


