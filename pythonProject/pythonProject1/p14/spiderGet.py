import urllib.request
while True:
    key=urllib.parse.quote(input("请输入要查询的外汇："))
    print(key)
    url="http://127.0.0.1/?currency=" + key
    print(url)
    response = urllib.request.urlopen(url)
    html = response.read().decode()
    print(html)