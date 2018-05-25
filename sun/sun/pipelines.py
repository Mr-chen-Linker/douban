# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import codecs


class SunPipeline(object):

    def __init__(self):
        self.filename = codecs.open("sun.json", "w", encoding="utf-8")

    def process_item(self, item, spider):
        jsontext = json.dumps(dict(item), ensure_ascii=False)+"\n"

        self.filename.write(jsontext)

        return item

    def close_spider(self):
        self.filename.close()
