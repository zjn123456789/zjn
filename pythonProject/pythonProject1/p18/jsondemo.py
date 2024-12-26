import json
import jsonpath
# 加载json文件数据
books=json.load(open("bookJson.json"))
print(books)
# 1.读取bicycle下color值
url1="$.store.bicycle.color"
print(jsonpath.jsonpath(books,url1))
# 2.输出book节点中包含的所有对象
url2="$.store.book[*]"
print(jsonpath.jsonpath(books,url2))
# 3.输出book节点的第一个对象
url3="$.store.book[0]"
print(jsonpath.jsonpath(books,url3))
# 4.输出book节点中所有对象对应的属性title值
url4="$.store.book[*].title"
print(jsonpath.jsonpath(books,url4))
# 5.输出book节点中category为fiction的所有对象
url5="$.store.book[?(@.category=='fiction')]"
print(jsonpath.jsonpath(books,url5))
# 6.输出book节点中所有价格小于10的对象
url6="$.store.book[?(@.price<10)]"
print(jsonpath.jsonpath(books,url6))
# 7.输出book节点中所有含有isbn的对象
url7="$.store.book[?(@.isbn)]"
print(jsonpath.jsonpath(books,url7))