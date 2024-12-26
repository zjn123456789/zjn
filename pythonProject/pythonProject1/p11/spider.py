import urllib.request
from http.client import responses

from Tools.scripts.generate_opcode_h import header

url="https://www.baidu.com/"
#伪装网络请求：浏览器请求
header={"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0"}
#网络请求
#response=urllib.request.urlopen(url)
request=urllib.request.Request(url,headers=header)
response=urllib.request.urlopen(request)
html=response.read().decode()
print(html)