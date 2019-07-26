# coding=utf-8
import requests
import time
from pyquery import PyQuery as pq
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0'
}
downloadHeaders = {
    'Host': 'pic2.avkdimage.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0',
    'Accept': 'text/htmlapplication/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Accept-Encoding': 'gzip, deflate',
    'DNT': 1,
    'Connection': 'keep-alive'
}
global cookies

def main():
    url = 'http://www.qu5000.com/html/part/index16_I.html'
    pageIndex = 9
    while True:
        response = requests.get(url.replace('I', str(pageIndex)), headers=headers)
        global cookies
        cookies = response.cookies
        doc = pq(response.text)
        print(doc)
        contentlist = doc('.box.list.channel').find('a')
        items = contentlist.items()
        for a in items:
            imagesUrl = a.attr('href')
            print(imagesUrl)
            getImageList(imagesUrl,a.text())
            pageIndex += 1
        with open('pageIndex.ini','wb') as file:
            file.writelines(str(pageIndex))
        time.sleep(10)

def getImageList(url,name):
    mainUrl = 'http://www.qu5000.com'
    try:
        response = requests.get(mainUrl + url,headers=headers)
        if response.status_code == 200:
            doc = pq(response.text)
            images = doc('.content').find('img').items()
            imageIndex = 1
            for image in images:
                imageUrl = image.attr('src')
                print(imageUrl)
                savefile(imageUrl,name,str(imageIndex) + '.jpg')
                imageIndex+=1
    except expression:
        print(mainUrl + url + expression)

def savefile(url,filepath, filename):
    try:
        response = requests.get(url, headers=headers, timeout=50,allow_redirects=False)
        res=response.headers['location']
        if response.status_code == 200 or response.status_code==302:
            filePath = 'images/' + filepath + '/' + filename
            with open(filePath, 'wb') as file:
                file.save(response.content)
                file.close()
    except ConnectionError:
        print(ConnectionError.strerror)
    except requests.RequestException as erro:
        print(erro)
if __name__ == "__main__":
    main()