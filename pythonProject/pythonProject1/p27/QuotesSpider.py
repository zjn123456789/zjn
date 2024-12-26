import csv
import sqlite3
import urllib.request
from bs4 import BeautifulSoup

class QuotesSpider:
    def __init__(self):
        self.items = []
        self.id_counter = 1  # 初始化id计数器

    # 翻页
    def page(self):
        for page in range(1, 11):
            url = "https://quotes.toscrape.com/page/" + str(page) + "/"
            print(url)
            # 通过网址抓取数据
            self.getData(url)

    # 抓取网址页面数据
    def getData(self, url):
        header = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0"
        }
        request = urllib.request.Request(url, headers=header)
        response = urllib.request.urlopen(request)
        html = response.read().decode()

        soup = BeautifulSoup(html, "lxml")
        divs = soup.select("div[class='quote']")
        for div in divs:
            content = div.select("span[class='text']")[0].get_text()
            author = div.select("small[class='author']")[0].get_text()
            link = div.select("span a")[0].attrs["href"]
            item = {
                "id": self.id_counter,  # 为每条数据分配一个唯一的id
                "content": content.replace("“", "").replace("”", ""),
                "author": author,
                "link": "https://quotes.toscrape.com" + link
            }
            self.items.append(item)
            self.insertDB(item["id"], item["content"], item["author"], item["link"])
            self.id_counter += 1  # 每次插入后增加id计数器

        # 打印列表中所有数据
        print(self.items)
        # 把数据写入文件
        self.save_file(self.items)
        # 把数据写入excel表格文件中
        self.save_csv(self.items)

    # 把数据存储在text文件中
    def save_file(self, data):
        with open("quotes.json", "w", encoding="utf-8") as file:
            file.write(str(data))

    # 把数据写入excel表格中
    def save_csv(self, data):
        with open("quotes.csv", "w", encoding="utf-8-sig",newline="") as fp:
            header = ["id", "content", "author", "link"]
            writer = csv.DictWriter(fp, fieldnames=header)
            writer.writeheader()
            writer.writerows(data)

    # 1.创建数据库和数据表
    def openDB(self):
        self.con = sqlite3.connect("quotes.db")  # 修改数据库文件名为quotes.db
        self.cursor = self.con.cursor()
        try:
            self.cursor.execute("DROP TABLE IF EXISTS quotes")  # 修改表名为quotes
        except:
            pass
        sql = "CREATE TABLE quotes (id INTEGER PRIMARY KEY, content TEXT, author TEXT, link TEXT)"
        self.cursor.execute(sql)

    # 4.插入一条数据
    def insertDB(self, id, content, author, link):
        try:
            sql = "INSERT INTO quotes (id, content, author, link) VALUES (?, ?, ?, ?)"
            self.cursor.execute(sql, (id, content, author, link))
        except Exception as err:
            print(err)

    # 4.提交并关闭数据库
    def closeDB(self):
        self.con.commit()
        self.cursor.close()
        self.con.close()

    # 2.调用方法创建数据库和表，插入数据和读取数据
    def process(self):
        self.openDB()
        self.page()  # 调用抓取数据的爬虫
        self.closeDB()

# 运行
spider = QuotesSpider()
spider.process()