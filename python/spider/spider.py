# coding=utf-8
import requests
indexUrl = "http://www.ttyy11.com"


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
        with open("ttyy11.html", "wb") as file:
            file.write(response.content)
            file.close()
