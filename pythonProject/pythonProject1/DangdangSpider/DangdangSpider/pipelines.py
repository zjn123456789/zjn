# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from urllib.request import Request

# useful for handling different item types with a single interface
import scrapy
from itemadapter import ItemAdapter
from scrapy.pipelines.images import ImagesPipeline


class DangdangspiderPipeline(ImagesPipeline):
    # 发送下载图片请求
    def get_media_requests(self, item, info):
        yield scrapy.Request( item["bImage"])
        # 图片保存的名称
    def file_path(self, request, response=None, info=None, *, item=None):
        imgname=item["bImage"].split("/")[-1]
        return imgname

    def item_completed(self, results, item, info):
        return item
