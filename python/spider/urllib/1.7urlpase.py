# coding=utf-8
from urllib import request, parse

# urllib.parse.urlparse(urlstring, scheme='', allow_fragments=True)
# allow_fragments 是否加载片段参数默认为true
# scheme='http/https'替换url协议类型，如果url中存在则不替换
result = parse.urlparse("http://www.baidu.com/index.html;user?id=5#comment")
print(type(result), result)

result = parse.urlparse('www.baidu.com/index.html;user?id=5#comment', scheme='https')
print(result)

result = parse.urlparse('http://www.baidu.com/index.html;user?id=5#comment', allow_fragments=False)
print(result)

# 拼接url
data = ['http', 'www.baidu.com', 'index.html', 'user', 'a=6', 'comment']
print(parse.urlunparse(data))

# 组合url
print(parse.urljoin('http://www.baidu.com', 'FAQ.html'))
print(parse.urljoin('http://www.baidu.com', 'https://cuiqingcai.com/FAQ.html'))
print(parse.urljoin('http://www.baidu.com/about.html', 'https://cuiqingcai.com/FAQ.html'))
print(parse.urljoin('http://www.baidu.com/about.html', 'https://cuiqingcai.com/FAQ.html?question=2'))
print(parse.urljoin('http://www.baidu.com?wd=abc', 'https://cuiqingcai.com/index.php'))
print(parse.urljoin('http://www.baidu.com', '?category=2#comment'))
print(parse.urljoin('www.baidu.com', '?category=2#comment'))
print(parse.urljoin('www.baidu.com#comment', '?category=2'))


params = {
    'name': 'germey',
    'age': 22
}
base_url = 'http://www.baidu.com?'
url = base_url + parse.urlencode(params)
print(url)
