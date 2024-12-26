import urllib.request
from bs4 import BeautifulSoup
import lxml

resp=urllib.request.urlopen("https://www.zhcpt.edu.cn/")
html=resp.read().decode()
soup=BeautifulSoup(html,"lxml")
divs=soup.find_all("div",attrs={"class":"bottom-box"})
for div in divs:
    links = div.find_all("div", attrs={"class": "desc"})
    for link in links:
        print(link.text)
print("====================")
divs=soup.select("li[class='item'] a div[class='desc']")
for div in divs:
    print(div.text)