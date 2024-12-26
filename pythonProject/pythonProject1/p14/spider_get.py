import urllib.request
import re

key=urllib.parse.quote(input("请输入要查询的外汇："))
print(key)
url="http://127.0.0.1/?currency=" + key
print(url)
response = urllib.request.urlopen(url)
html = response.read().decode()
# print(html)
# 正则表达式抽取数据
s=html
print(s)
m=re.search(r"</tr><tr>",s)
n=re.search(r"</tr></table>",s)
s=s[m.end():n.start()]
print(s)
while s!="":
    m = re.search(r"<td>",s)
    n = re.search(r"</td>", s)
    t = s[m.end():n.start()]
    print(t)
    s=s[n.end():]