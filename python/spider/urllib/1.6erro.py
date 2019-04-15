# coding=utf-8
from urllib import request, error
try:
    response = request.urlopen("http://www.baidu.com", timeout=0.01)
except error.URLError as e:
    print(e.reason)
print("=============================================================")

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
