# coding=utf-8
from bs4 import BeautifulSoup

html = """<title>This Documents</title>
<li class="spacer"></li>
                <li class="dropdown">
                    <a href=""></a>
                    <i>导航</i>
                    网站导航
                </li>
                <li class="spacer">spacer</li>
                <li style="position:relative">
                    <a name="sjjd" href="">手机京东</a>
                    <div class="erweima">
                        <img src="./images/erweima.png" alt="">
                    </div>
                </li>"""
soup = BeautifulSoup(html, "html.parser")
print(soup.prettify())  # 格式化代码
print(soup.title.string)
lis = soup.find_all("li")
for li in lis:
    print(li.string)
js = soup.find_all(attrs={"name": "sjjd"})
print(js)
