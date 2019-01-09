#coding=utf-8
import urllib.request
import urllib.parse
import http.cookiejar
'''
思路：
1.导入Cookie处理模块http.cookiejar
2.使用http.cookiejar.CookieJar()创建CookieJar对象
3.使用HTTPCookieProcessor创建cookie处理器,并以其未参数构建opener对象
4.创建全局默认的opener
'''
url = "http://u2.qingting.fm/u2/api/v4/user/login"
postdata=urllib.parse.urlencode({
    "account_type":5,
    "device_id":"web",
    "user_id":17345060826,
    "password":"DWG352834867"
}).encode("utf-8")#urlencode编码处理，然后设置为utf-8编码
req=urllib.request.Request(url,postdata)
req.add_header("User-Agent","Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4399.400 QQBrowser/9.7.12777.400")
# 创建cookiejar对象
cookiejar=http.cookiejar.CookieJar()
# 创建cookie处理器，构建opener对象
opener=urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookiejar))
# 将opener安装为全局
urllib.request.install_opener(opener)
data=opener.open(req).read()
with open("qingtingfm.html","wb") as fhandle :
    fhandle.write(data)#内容写入对应文件
res=urllib.request.urlopen("http://www.qingting.fm").read() #登录并爬取对应网页
with open("qingtingfmindex.html","wb") as resfile:
    resfile.write(res)

