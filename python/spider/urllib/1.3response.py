# coding = utf-8
import urllib.request
response = urllib.request.urlopen('http://www.python.org')
# 响应类型 http.client.HTTPResponse
print(type(response))
print("Status:", response.status)
print("Headers:", response.getheaders())
print("Server", response.getheader('Server'))
