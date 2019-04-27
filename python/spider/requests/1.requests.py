# coding=utf-8
import requests
# Respones
response = requests.get("https://www.baidu.com")
print(type(response))
print(type(response.text))
print(response.text)
print(response.content)
print(response.status_code)
print(response.cookies)


response = requests.get("http://httpbin.org/get?name=lily&age=22")

print()


