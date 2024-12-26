import urllib.request

import bs4.element
from bs4 import BeautifulSoup
import lxml

resp=urllib.request.urlopen("http://10.254.115.230:80")
html=resp.read().decode()
soup=BeautifulSoup(html,"lxml")
# 1.查找文档中，div标签下的a标签
print(soup.select("div a"))
# 2.查找文档中属性class="quote"的<div>节点下的所有<span>节点
print(soup.select("div[class='quote'] span a"))
# 3.查找文档中具有class属性的<div>节点下的所有<a>节点
print(soup.select("div[class] a"))
# 4.查找<div>下面具有class属性的<span>节点
print(soup.select("div span[class]"))
# 5.查找<html>下面的<head>下面的<title>节点
print(soup.select("html head title"))
# 6.查找<div>下面所有具有class属性的节点
print(soup.select("div[class]"))
# 7.查找<div>下面所有具有class属性的节点下面的第二个<a>节点
print(soup.select("div[class] a:nth-of-type(2)"))

print("2.查找文档中属性class=quote的<div>节点下的所有<span>的a节点")
links=soup.select("div[class='quote'] span a")
for link in links:
    print(link)

print("3.<div class=quote>下第二个span")
spans=soup.select("div[class='quote'] span:nth-of-type(2)")
for span in spans:
    print(span)

print("4.<div class=quote>下的<div class=tags>下第二个a")
elems=soup.select("div[class='quote'] div[class='tags'] a:nth-of-type(2)")
for elem in elems:
    print(elem)