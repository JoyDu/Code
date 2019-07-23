# coding=utf-8
import re
# re.match(pattern,string,flags)
content = 'Hello 123 4567 World_This is a Regex Demo'
print('len(content):')
print(len(content))
# 最常规得匹配
result = re.match('^Hello\s\d\d\d\s\d{4}\s\w{10}.*Demo$', content)
print(result)
print(result.group())
print(result.span())
# 泛匹配

