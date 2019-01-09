# coding=utf-8
import re
import urllib.request
import datetime

def createrequest(url):
    req = urllib.request.Request(url)
    req.add_header(
        'User-Agent',
        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4882.400 QQBrowser/9.7.13059.400'
    )
    return req


def craw(url, page):
    req = createrequest(url)
    pagehtml = urllib.request.urlopen(req).read()
    pagehtml = str(pagehtml, 'utf-8')
    # 匹配页面内容模块
    pattpagecontent = '<[Uu][Ll][\s][Cc][Ll][Aa][Ss][Ss]=[\s][Ll][Ii][Ss][Tt]>[\s\S].*?<[Dd][Ii][Vv][\s][Cc][Ll][Aa][Ss][Ss]="[Pp][Aa][Gg][Ee]" style="clear:both">'
    # pagecontent=re.compile(pattpagecontent).findall(pagehtml,re.S)
    pagecontent = re.findall(pattpagecontent, pagehtml, re.S)
    pagecontent=' '
    # 匹配内容明细列表
    pattpagecontentlist = '(<[Ll][Ii]><[Aa][\s\S].*?[Tt][Aa][Rr][Gg][Ee][Tt]=_[Bb][Ll][Aa][Nn][Kk][\s\S].*?</[Aa]></[Ll][Ii]>)'
    if pagecontent is not None:
        pagecontentlist = re.compile(pattpagecontentlist).findall(
            pagehtml)
        pattimagpagelink = '(/.*?[Hh][Tt][Mm][Ll])'
        pattpagetitle = '(title=.*?\[.*?])'
        if pagecontentlist is not None:
            # 页面内容链接明细
            for pagelink in pagecontentlist:
                imagepagelink = re.compile(pattimagpagelink).findall(pagelink)
                foldername = re.compile(pattpagetitle).findall(pagelink)
                if foldername is not None and len(foldername) > 0:
                    foldername = foldername[0].replace('title=', '')
                else:
                    foldername = str(datetime.datetime.timestamp)
                if imagepagelink is not None and len(imagepagelink) > 0:
                    imagepagelink = mainurl + imagepagelink[0]
                req = createrequest(imagepagelink)
                imagepage = urllib.request.urlopen(req).read()
                imagepage = str(imagepage, 'utf-8')
                pattimagelinks = '[Ss][Rr][Cc]=.*?\.jpg'
                imagelinks = re.compile(pattimagelinks).findall(imagepage)
                if imagelinks is not None and len(imagelinks) > 0:
                    imageindex = 0
                    for imagelink in imagelinks:
                        link = imagelink.lower().replace('src=', '').replace('"','')
                        savefilename = foldername + '/' + str(imageindex) + '.jpg'
                        urllib.request.urlretrieve(link, filename=savefilename)
                        imageindex += 1
                with open("1.html", 'w', encoding='utf-8') as file:
                    file.write(imagepage)


for i in range(1, 1000):
    url = "https://www.160ii.com/htm/piclist1"
    if i > 1:
        url = "https://www.160ii.com/htm/piclist1/" + str(i) + ".htm"
    craw(url, i)
