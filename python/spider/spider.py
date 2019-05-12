# coding=utf-8
import requests
from bs4 import BeautifulSoup
indexUrl = "http://www.ttyy11.com/ee44/7/1.html"
rootPath = "ttyy11/"


def main():
    response = requestGet(indexUrl)
    if response is not False:
        writeToFile(response)
        soup = BeautifulSoup(response.text, "lxml")
        print(soup.title)
        #pagelist=


def requestGet(url):
    headers = {
        "User-Agent":
        "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Mobile Safari/537.36"
    }
    try:
        response = requests.get(url, headers=headers)
        return response
    except requests.ReadTimeout:
        print("Time Out")
        return False
    except ConnectionError:
        print("ConnectionError")
        return False
    except requests.RequestException:
        print("Error")
        return False
    print(response.text)


def writeToFile(response):
    if response is False:
        return False
    else:
        filepath = rootPath+"ttyy11.html"
        with open(filepath, "wb") as file:
            file.write(response.content)
            file.close()


main()
