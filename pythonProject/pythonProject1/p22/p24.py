import urllib.request

import bs4.element
from bs4 import BeautifulSoup
import lxml

resp=urllib.request.urlopen("http://10.254.115.230:80")
html=resp.read().decode()
soup=BeautifulSoup(html,"lxml")
print("1.查找第一个span标签的父元素")
p=soup.find("span")
print(p)
while p:
    # 打印父节点标签名字
    print(p.name)
    # 再继续往上查找
    p=p.parent

print("2.子节点：<div class=quote下第二个span所有子节点>")
p=soup.find("div",attrs={"class":"quote"}).find_all("span")[1]
for q in p.children:
    print(type(q),q.name)
    if isinstance(q,bs4.element.NavigableString):
        print(q.string)
    else:
        print(q.text)

print("3.")
p=soup.find("div",attrs={"class":"tags"})
for q in p.descendants:
    print(type(q), q.name)
    if isinstance(q,bs4.element.NavigableString):
        s=q.string.strip("\n")
        s=s.strip()
        if s!="":
            print(s)
    else:
        print(q.name,q.text)

print("4.子节点:<div class=tags下所有并列的a元素")
p=soup.find("div",attrs={"class":"tags"}).find("a")
while p:
    if isinstance(p,bs4.element.Tag) and p.name=="a":
        print(p)
    p=p.next_sibling

