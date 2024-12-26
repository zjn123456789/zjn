import urllib.request
from bs4 import BeautifulSoup
import lxml

url="https://quotes.toscrape.com/"

#伪装网络请求：浏览器请求
header={"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0"}
#网络请求
#response=urllib.request.urlopen(url)
request=urllib.request.Request(url,headers=header)
response=urllib.request.urlopen(request)
html=response.read().decode()
soup=BeautifulSoup(html,"lxml")
spans=soup.select("div[class='quote']")
for span in spans:
    # 名言内容
    content=span.select("span[class='text']")[0].get_text()
    # print(content)
    # 作者
    author=span.select("small[class='author']")[0].get_text()
    # print(author)
    # 作者简介链接
    a=span.select("span a")[0].attrs=["href"]
    print(a)
