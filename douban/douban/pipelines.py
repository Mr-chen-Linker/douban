# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import codecs
import json
from scrapy.conf import settings
import pymongo


class DoubanPipeline(object):

    def __init__(self):
        # self.filename = codecs.open("doubanmovie.json", "w", encoding="utf-8")
        # 从设置文件中按到mongo的设置信息
        host = settings["MONGODB_HOST"]
        port = settings["MONGODB_PORT"]
        dbname = settings["MONGODB_DBNAME"]
        sheetname = settings["MONGODB_SHEETNAME"]

        # 创建一个连接mongo的客户端
        client = pymongo.MongoClient(host, port)

        # 得到一个数据库对象
        mydb = client[dbname]
        # 得到一个数据库的表 对象
        self.post = mydb[sheetname]

    def process_item(self, item, spider):
        # jsontext = json.dumps(dict(item), ensure_ascii=False)
        #
        # self.filename.write(jsontext)

        data = dict(item)

        self.post.insert(data)

        return item

    def close_spider(self, spider):
        # self.filename.close()
        pass
