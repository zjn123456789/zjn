import urllib.request
import re
import sqlite3

class MySpider:
    # 1.创建数据库和数据表
    def openDB(self):
        self.con=sqlite3.connect("rates.db")
        self.cursor=self.con.cursor()
        try:
            # 删除旧的表
            self.cursor.execute("drop table rates")
        except:
            pass
        # 创建数据表
        sql="create table rates (Currency varchar(256) primary key,TSP float,CSP float,TBP float,CBP float)"
        self.cursor.execute(sql)
    # 4.插入插入一条数据
    def insertDB(self,Currency,TSP,CSP,TBP,CBP):
        # 记录插入数据库
        try:
            sql="insert into rates (Currency,TSP,CSP,TBP,CBP) values (?,?,?,?,?)"
            self.cursor.execute(sql,[Currency,TSP,CSP,TBP,CBP])
        except Exception as err:
            print(err)
    # 5.提交并关闭数据库
    def closeDB(self):
        # 提交
        self.con.commit()
        self.con.close()
    # 6.编写爬虫抓取数据
    def spider(self,url):
        try:
            resp=urllib.request.urlopen(url)
            data=resp.read()
            html=data.decode()
            # 抓取html
            # print(html)
            # 抽取所有包含td标签的html代码
            p=re.search(r"<tr>",html)
            q = re.search(r"<tr>", html)
            # 从第一行数据开始
            i=0
            while p and q:
                a=p.end()
                b=q.start()
                # 一行数据所有td标签
                tds=html[a:b]
                # print(tds)
                # 3.抽取所有td标签内的数据
                m = re.search(r"<td>",tds)
                n = re.search(r"</td>", tds)
                row=[]
                while m and n:
                    u=m.end()
                    v=n.start()
                    row.append(tds[u:v].strip("\n"))
                    print(row)
                    # 下一个td标签数据
                    tds=tds[n.end():]
                    m = re.search(r"<td>", tds)
                    n = re.search(r"</td>", tds)
                # 下一行数
                i=i+1
                if i >= 2 and len(row) == 6:
                    Currency = row[0]
                    TSP=float(row[2])
                    CSP=float(row[3])
                    TBP=float(row[4])
                    CBP=float(row[5])
                    self.insertDB(Currency,TSP,CSP,TBP,CBP)
                html=html[q.end():]
                p=re.search(r"<tr>",html)
                q=re.search(r"</tr>", html)

        except Exception as err:
            print(err)
    # 2.调用方法创建数据库和表，插入数据和读取数据
    def process(self):
        # 2.1调用方法创建数据库数据表
        self.openDB()
        # 调用插入一条数据方法
        # self.insertDB("瑞士法郎",100,697.09,697.09,691.53)
        # 调用抓取数据的爬虫
        self.spider("http://127.0.0.1")
        self.closeDB()
# =======================================
# 3.执行
spider=MySpider()
spider.process()