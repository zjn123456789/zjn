import csv
import sqlite3
import urllib.request
from bs4 import BeautifulSoup

class MovieSpider:
    def __init__(self):
        # 列表，存放所有电影数据
        self.movies = []
        self.openDB()

    # 把数据存储在text文件中
    def save_file(self, data):
        file = open("movie.txt","wb+")
        file.write(str(data).encode())
        file.close()
    # 把数据写入excel表格中
    def save_csv(self, data):
        with open("movies.csv", "w", encoding="utf-8-sig", newline="") as fp:
            header = ["mTitle", "mNative", "myNickname", "myDirector", "mActors", "mType", "mTime", "mCountry",
                      "mPoint", "mComments", "mImage"]
            w = csv.DictWriter(fp, fieldnames=header)
            w.writeheader()
            w.writerows(data)

    def downloadImg(self,src,imgname):
        header = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0"
        }
        request = urllib.request.Request(src, headers=header)
        response = urllib.request.urlopen(request)
        imgdata = response.read()
        # 保存图片
        file = open("images\\"+imgname, "wb")
        file.write(imgdata)
        file.close()

    # 翻页
    def page(self):
        for page in range(0, 10):
            url = "http://10.65.10.100/movie/1.htm?start=" + str(page*25) + "&filter="
            print(url)
            # 抓取每一页数据
            self.getData(url)
        # 打印所有电影数据
        # print(self.movie)
        # 把数据写入txt文件中
        self.save_file(self.movies)
        # 把数据写入csv文件中
        self.save_csv(self.movies)
        self.closeDB()

    # 抓取网址页面数据
    def getData(self, url):
        header = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0"
        }
        request = urllib.request.Request(url, headers=header)
        response = urllib.request.urlopen(request)
        html = response.read().decode()
        soup = BeautifulSoup(html, "lxml")
        divs = soup.select("div[class='item']")
        for div in divs:
            # 三个电影名文本数据：数组
            titles = div.select("div[class='hd'] a")[0].get_text().replace("\xa0","").replace("\n","").split("/")
            # print(titles)
            # 1.名称
            mTitle = titles[0]
            # print(mTitle)
            # 2.原名
            mNative = titles[1]
            # print(mNative)
            # 3.别名
            myNickname = div.select("span[class='other']")[0].get_text()[2:].replace("\xa0","")
            # print(myNickname)
            # 电影详细信息
            info = div.select("div[class='bd'] p")[0].get_text().replace("\xa0","").replace("\n","")
            # print(info)
            # 4.导演
            myDirector = info.strip().split("导演:")[1].split("主演:")[0]
            # print(myDirector)
            # 5.主演
            try:
                mActors = info.strip().split("主演:")[1].split("...")[0]
                # print(mActors)
            except:
                mActors = "无主演"
                # print(mActors)
            # 6.类型
            mType = info.split("/")[-1].strip()
            # print(mType)
            # 7.时间
            mTime = info.split("/")[-3].strip()[-4:]
            # print(mTime)
            # 8.国家
            mCountry = info.split("/")[-2].strip()
            # print(mCountry)
            # 9.评分
            mPoint = div.select("span[class='rating_num']")[0].get_text()
            # print(mPoint)
            # 10.评价
            try:
                mComments = div.select("span[class='inq']")[0].get_text()
            except:
                mComments = "无评论"
            # print(mComments)
            # 11.图片地址
            mImage = div.select("div[class='pic'] a img")[0].attrs["src"]
            if mImage.startswith('./'):
                # 将相对路径转换为完整的URL
                mImage = 'http://10.65.10.100/movie/' + mImage[2:]
            elif not mImage.startswith('http'):
                # 如果不是以http开头，也转换为完整的URL
                mImage = 'http://10.65.10.100/movie/' + mImage
            # 文件名字
            imgName =mImage.split("/")[-1].replace(".","")
            # 调用方法下载图片downloadImg
            self.downloadImg(mImage, imgName)
            # print(mImage)
            movie={}
            movie["mTitle"] = mTitle
            movie["mNative"] = mNative
            movie["myNickname"] = myNickname
            movie["myDirector"] = myDirector
            movie["mActors"] = mActors
            movie["mType"] = mType
            movie["mTime"] = mTime
            movie["mCountry"] = mCountry
            movie["mPoint"] = mPoint
            movie["mComments"] = mComments
            movie["mImage"] = mImage
            # 把一条电影信息压入列表中
            self.movies.append(movie)
            self.insertDB(mTitle, mNative, myNickname, myDirector, mActors, mType, mTime, mCountry, mPoint, mComments, mImage)

    # 1.创建数据库和数据表
    def openDB(self):
        self.con = sqlite3.connect("douban.db")
        self.cursor = self.con.cursor()
        try:
            self.cursor.execute("DROP TABLE IF EXISTS douban")
        except:
            pass
        sql = ("CREATE TABLE douban (mTitle varchar(50) PRIMARY KEY,mNative varchar(50),myNickname varchar(50),myDirector varchar(50),mActors varchar(50),"
               "mType varchar(50),mTime varchar(10),mCountry varchar(10),mPoint varchar(6),mComments varchar(120),mImage varchar(120))")
        self.cursor.execute(sql)
    # 4.插入一条数据
    def insertDB(self,  mTitle, mNative, myNickname, myDirector, mActors, mType, mTime, mCountry, mPoint, mComments, mImage):
        try:
            sql = "INSERT INTO douban (mTitle, mNative, myNickname, myDirector, mActors, mType, mTime, mCountry, mPoint, mComments, mImage) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
            self.cursor.execute(sql, [ mTitle, mNative, myNickname, myDirector, mActors, mType, mTime, mCountry, mPoint, mComments, mImage])
        except Exception as err:
            print(err)
    # 4.提交并关闭数据库
    def closeDB(self):
        self.con.commit()
        self.cursor.close()
        self.con.close()

spider=MovieSpider()
# spider.getData("http://10.65.10.100/movie/1.htm")
spider.page()