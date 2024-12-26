from scrapy import cmdline;
# 生成text文件
# cmdline.execute("scrapy crawl dangdangspider -o books.json".split())
# 生成csv
cmdline.execute("scrapy crawl dangdangspider".split())