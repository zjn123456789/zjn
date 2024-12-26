import scrapy

from DangdangSpider.items import DangdangspiderItem


class DangdangspiderSpider(scrapy.Spider):
    name = "dangdangspider"
    allowed_domains = ["search.dangdang.com"]
    url = "https://search.dangdang.com/?key=%B4%F3%CA%FD%BE%DD%BC%BC%CA%F5&act=input&page_index="
    page = 1
    # 程序入口网址
    start_urls = [url+str(page)]
    # 打印当前爬取的网址
    print(start_urls)
    def parse(self, response):
        # 打印爬取到的html
        # print(response.text)
        # 限制爬取页数
        lis = response.xpath("//ul[@class='bigimg']/li")
        for li in lis:
            # 1.图示标题
            bTitle = li.xpath("a/@title").extract_first()
            # 2.作者
            bAuthor = li.xpath("p[@class='search_book_author']/span[1]/a[1]/@title").extract_first()
            # 3.出版社
            bPublisher = li.xpath("p[@class='search_book_author']/span[3]/a[1]/@title").extract_first()
            # 4.出版时间
            bDate = li.xpath("p[@class='search_book_author']/span[2]/text()").extract_first()
            # 5.价格
            bPrice = li.xpath("p[@class='price']/span[1]/text()").extract_first()
            # 6.简介
            bDetail = li.xpath("p[@class='detail']/text()").extract_first()
            # 7.图片地址
            bImage = li.xpath("a[@class='pic']/img/data-original").extract_first()
            # print(bImage)
            # print("图书标题:"+bTitle+",作者:"+bAuthor+",出版社:"+bPubisher+",出版时间:"+bDate+"")
            item=DangdangspiderItem()
            item["bTitle"] = bTitle
            item["bAuthor"] = bAuthor
            item["bPublisher"] = bPublisher
            item["bDate"] = bDate.replace(" /","")
            item["bPrice"] = bPrice
            item["bDetail"] = bDetail
            item["bImage"] = "https:"+str(bImage)
            #  提交
            yield item
        if(self.page<5):
            self.page+=1
        pageurl = self.url + str(self.page)
        # 打印当前爬取的页码
        print(pageurl)
        # 实现翻页
        yield scrapy.Request(pageurl,callback=self.parse)