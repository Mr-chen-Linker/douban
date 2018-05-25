# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SunItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 标题
    title = scrapy.Field()
    # 标号
    numberNo = scrapy.Field()
    # 内容
    content = scrapy.Field()
    # 帖子链接
    url = scrapy.Field()
