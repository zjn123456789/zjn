import urllib.request
from bs4 import BeautifulSoup
import lxml

resp=urllib.request.urlopen("http://10.254.115.230:80")
html=resp.read().decode()
# print(html)
# 把HTML字符串转换成可操作的BeautifulSoup对象
soup=BeautifulSoup(html,"lxml")
# print(soup)
# 1. 查找span标签：find()找到第一个之后，就不再往下找，找全部
print(soup.find("span"))
print(soup.find_all("span"))
# 2.查找a标签
print(soup.find("a"))
# 3.查找h4
print(soup.find("h4"))
# 4.查找指定a标签，<a class="tag">
print(soup.find("a",attrs={"class":"tag"}))
# 5.查找<div class="tags">下第一个a元素
div=(soup.find("div",attrs={"class","tags"}))
print(div.find("a"))
# 6.查找第一个small标签
print(soup.find("small"))

# ======2.3.2查找元素属性与文本
# 7.名言的文本
print(soup.find("span").text)
# 8.查找名言下对应的名人与链接地址
print(soup.find("small").text)
print(soup.find("a")["href"])
# 9.去除<div class="tags">元素文本
print(soup.find("div",attrs={"class":"tags"}).text)

# ======2.3.3使用find_all()查找标签
# 10.查找所有a标签，把数据抽取出来
links=soup.find_all("a")
print(links)
for link in links:
    print(link.text)

print("===11.查找所有名言")
divs=soup.find_all("div",attrs={"class":"quote"})
for div in divs:
    print(div.find("span").text)
print("===12.查找最后一条名言和人名")
divs=soup.find_all("div",attrs={"class":"quote"})[-1]
print(div.find("span").text)
print(div.find("small").text)
print("===13.查找div tags中最后一个a元素")
divs=soup.find_all("div",attrs={"class":"quote"})
for div in divs:
    links=div.find("div",attrs={"class":"tags"}).find_all("a")
    print((links[-1]["href"]))
print("===14.查找所有div tags中链接地址")
for div in divs:
    links=div.find_all("a",attrs={"class":"tag"})
    for link in links:
        print(link["href"])


#======2.3.4 高级查找====
print("=====16.查找文本值为thinking的a标签")
def myFilter(tag):
    if tag.name=="a" and tag.text=="thinking":
        return True
    return False
print(soup.find("div" ,attrs={"class":"quote"}).find(myFilter))
print("=====17.查找所有<a class=tag的文本值")
def myFilter(tag):
    if tag.name=="a" and tag.has_attr("class") and tag["class"]==["tag"]:
        return True
    return False
links=soup.find_all(myFilter)
for link in links:
    print(link)
print("=====18.查找所有a链接地址中包含page的标签")
def myFilter(tag):
    if tag.name=="a" and tag.has_attr("href") and tag["href"].find("deep")>=0:
        return True
    return False
links=soup.find_all(myFilter)
for link in links:
    print(link)


