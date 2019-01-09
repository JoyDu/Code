# coding=utf-8
import urllib.request
import bs4
import os


class IP(object):
    def __init__(self, address, port, service_address, anonymous, types,
                 islife, checktime):
        self.address = address
        self.port = port
        self.service_address = service_address
        self.anonymous = anonymous
        self.types = types
        self.islife = islife
        self.checktime = checktime

    def __str__(self):
        printInfo = ("ip地址:%s 端口:%s 服务器地址:%s 是否匿名:%s 类型:%s 存活:%s 验证时间:%s" %
                     (self.address, self.port, self.service_address,
                      self.anonymous, self.types, self.islife, self.checktime))
        return printInfo


def request_get(url):
    # url=urllib.request.quote(url)
    request = urllib.request.Request(url)
    request.add_header(
        "User-Agent",
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4399.400 QQBrowser/9.7.12777.400"
    )
    try:
        data = urllib.request.urlopen(request).read()
    except urllib.error.HTTPError as httpError:
        return "error:" + httpError.args[0].strerror
    else:
        return data


def Main():
    if os.path.exists("xicidaili.html"):
        file = open("xicidaili.html", "r", encoding="utf-8")
        req_data = file.read()
        file.close()
    else:
        url = "http://www.xicidaili.com/"
        req_data = request_get(url)
        with open("xicidaili.html", "wb") as xici_file:
            xici_file.write(req_data)
    if req_data is not None:
        http_IpList = deal_data(req_data)
        #if len(http_IpList)>0:
    else:
        print("req_data is None")


def check_HttpIpUseful(htt):
    pass


def deal_data(data):
    html = bs4.BeautifulSoup(data, "html.parser")
    print(html.title)
    tr_iplist = html.find_all("tr")
    http_IpList = []
    # print(tr_iplist.contents)
    if tr_iplist is not None:
        for iplist in tr_iplist:
            if len(list(iplist.children)) < 6 or (
                    iplist.attrs["class"][0] == "subtitle"):
                continue
            # print(len(list(iplist.stripped_strings)))
            ip_info = list(iplist.stripped_strings)
            if len(ip_info) == 7:
                ip_object = IP(ip_info[0], ip_info[1], ip_info[2], ip_info[3],
                               ip_info[4], ip_info[5], ip_info[6])
                print(ip_object)
                if ip_object.types == "HTTP":
                    http_IpList.append(ip_object)
            # for ip in iplist.stripped_strings:
            #     print(repr(ip).replace("'",""))
    return http_IpList


if __name__ == "__main__":
    Main()