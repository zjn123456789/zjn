import json
import sqlite3
import urllib.request

from p11.spider import request, response


class MySpider:
    # 1.抓取json数据爬虫方法
    def spider(self,url):
        # 伪装请求
        header={"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0"}
        request=urllib.request.Request(url,headers=header)
        response=urllib.request.urlopen(request)
        # 读取json数据
        html=response.read().decode()
        # print(html)
        #把字符串转换为json对象
        datas=json.loads(html)["body"]
        # print(datas)
        for data in datas:
            # 1.币种
            Currency=data["ccyNbr"];
            TSP=data["rtbBid"];
            CSP=data["rthOfr"];
            TBP=data["rthOfr"];
            CBP=data["rtcBid"];
            Time=data["ratDat"];
            print(Currency,TSP,CSP,TBP,CBP,Time)
            # 调用数据插入方法
            self.insertDB(Currency, TSP, CSP, TBP, CBP,Time)
            # self.con.commit()

    # 2.创建数据库和数据表
    def openDB(self):
        self.con = sqlite3.connect("rates2.db")
        self.cursor = self.con.cursor()
        try:
            # 删除旧的表
            self.cursor.execute("drop table rates2")
        except:
            pass
        # 创建数据表
        sql = "create table rates2 (Currency varchar(256) primary key,TSP float,CSP float,TBP float,CBP float,Time varchar(25))"
        self.cursor.execute(sql)

    # 3.插入一条数据
    def insertDB(self, Currency, TSP, CSP, TBP, CBP,Time):
            # 记录插入数据库
            try:
                sql = "insert into rates2 (Currency,TSP,CSP,TBP,CBP,Time) values (?,?,?,?,?,?)"
                self.cursor.execute(sql, [Currency, TSP, CSP, TBP, CBP,Time])
            except Exception as err:
                print(err)

    # 4.提交并关闭数据库
    def closeDB(self):
        # 提交
        self.con.commit()
        self.con.close()

    # 执行方法
    def process(self):
        # 1.1调用数据库和数据表生成方法
        self.openDB()
        # 1.2调用爬虫获取json数据
        self.spider("https://fx.cmbchina.com/api/v1/fx/rate")
        self.closeDB()

# 调用MySpider
spider=MySpider()
spider.process()