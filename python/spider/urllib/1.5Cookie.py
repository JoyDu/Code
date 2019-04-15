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
cookie.load(cookiefile, ignore_discard=True, ignore_expires=True)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
opener.open("http://www.baidu.com")
print(response.read().decode("utf-8"))
