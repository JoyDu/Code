# coding=utf-8
import requests

response = requests.get("http://www.baidu.com")
print('type(response):  ')
print(type(response))
print("status_code:    ")
print(response.status_code)
print("type(response.text):    ")
print(type(response.text))
print("response.text:    ")
print(response.text)
print("response.cookies:    ")
print(response.cookies)
if __name__ == "__main__":
    print(__name__)
