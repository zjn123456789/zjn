import urllib.request

while True:
    key="currency="+urllib.parse.quote(input("请输入要查询的外汇："))
    url="http://127.0.0.1"
    response = urllib.request.urlopen(url,data=key.encode())
    html = response.read().decode()
    print(html)