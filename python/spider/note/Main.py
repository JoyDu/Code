# coding=utf-8
import urllib.request
import urllib.error
'''
抓取页面存到本地，方式一
'''
file = urllib.request.urlopen("https://zhuanlan.zhihu.com/dianyinglieshou")
# 环境信息
info = file.info()
print(info)

# 获取当前爬取的url
url = file.geturl()
print(url)

# 状态码
statuscode = file.getcode()
print(statuscode)
# data = file.read()# 读取文件所有数据返回字符串
data = file.readlines()  # 读取所有，返回列表
# data = file.readline()# 逐行读取
for x in data:
    print(data)
data = file.read()
wtfile = open("zhihu.html", "wb")
wtfile.write(data)
wtfile.close()
'''
抓取页面存到本地，方式二
'''
file = urllib.request.urlretrieve("https://zhuanlan.zhihu.com/dianyinglieshou",
                                  "zhihu2.html")

# 清除缓存
urllib.request.urlcleanup()
'''
url编码 解码
'''
encodeUrl = urllib.request.quote("https://zhuanlan.zhihu.com/dianyinglieshou")
print("Encode Url:%s" % encodeUrl)
decodeUrl = urllib.request.unquote(encodeUrl)
print("Decode Url:%s" % decodeUrl)
'''
浏览器模拟 Headers属性
'''
print("***************浏览器模拟-Headers属性_Start******************")
moni_url = "https://blog.csdn.net/weiwei_pig/article/details/51178226"
moni_file = urllib.request.urlopen(moni_url)
print(moni_file.getcode())

# build_opener()修改报头
build_url = moni_url
headers = {
    "User-Agent",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1"
}
opener = urllib.request.build_opener()
opener.addheaders = [headers]
data = opener.open(build_url).read()
with open("weiwei_android_route.html", "wb") as opener_file:
    opener_file.write(data)
# print(data)
# add_header()添加报头
req = urllib.request.Request(build_url)
req.add_header(
    "User-Agent",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1"
)
# timeout设置超时时间 单位s
data = urllib.request.urlopen(req, timeout=10).read()
print(data)
print("***************浏览器模拟-Headers属性_End******************")
'''
Post请求
'''


def request_Post(url, postdata, filename):
    if postdata is not None:
        postdata = urllib.parse.urlencode(postdata).encode("utf-8")
    else:
        postdata = {}
    post_request = urllib.request.Request(url, postdata)
    post_request.add_header(
        "User-Agent",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1"
    )
    post_resdata = urllib.urlopen(post_request).read()
    with open(filename, "wb") as wfile:
        wfile.write(post_resdata)


'''
代理设置
'''


def use_proxy(proxy_addr, url):
    proxy = urllib.request.ProxyHandler(proxy_addr)
    opener = urllib.request.build_opener(proxy, urllib.request.HTTPHandler)
    urllib.request.install_opener(opener)
    proxy_data = urllib.request.urlopen(url).read().decode("utf-8")
    return proxy_data


#proxy_addr="221.224.49.237:3128"
try:
    proxy_addr = {"http": "202.75.210.45:7777"}
    proxy_resdata = use_proxy(proxy_addr, "http://www.baidu.com")
    print("proxy_baidu:", len(proxy_resdata))
except urllib.request.URLError as erro:
    print(erro.reason)


def use_proxy_https(proxy_addr, url):
    proxy = urllib.request.ProxyHandler({"https": proxy_addr})
    opener = urllib.request.build_opener(proxy, urllib.request.HTTPSHandler)
    urllib.request.install_opener(opener)
    proxy_resdata = urllib.request.urlopen(url).read().decode("utf-8")
    return proxy_resdata


'''
DebugLog
'''
debug_httphand = urllib.request.HTTPHandler(debuglevel=1)
debug_httpshand = urllib.request.HTTPSHandler(debuglevel=1)
debug_opener = urllib.request.build_opener(debug_httphand, debug_httpshand)
urllib.request.install_opener(debug_opener)
debug_data = urllib.request.urlopen("http://edu.51cto.com")
'''
URLError
'''
try:
    urllib.request.urlopen("http://www.google.com.hk")
except urllib.error.URLError as e:
    print(e.reason)
'''
正则表达式
'''
#原子
#普通字符
import re
pattern = "yue"
string = "http://yum.iqianyue.com"
result = re.search(pattern, string)
print(result)


#非打印字符
class test_des(object):
    '''
    测试描述
    '''


print(help(test_des))
#通用字符

#原子表
