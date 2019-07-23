# coding=utf-8
import requests
from pyquery import PyQuery as pq
headers = {
    'User-Agent':
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
}
url = 'http://www.gn47.com/avhhf/7/I.html'
pageIndex = 1


def main():
    while True:
        response = requests.get(
            url.replace('I', str(pageIndex)), headers=headers)
        doc = pq(response.text)
        print(doc.text())
        pageIndex += 1
        break


def savefile(url, filename):
    try:
        response = requests.get(url, headers=headers, timeout=5)
        if response.status_code == 200:
            with open('gn47/' + filename, 'wb') as file:
                file.save(response.content)
                file.close()
    except expression as identifier:
        print(url + identifier)
