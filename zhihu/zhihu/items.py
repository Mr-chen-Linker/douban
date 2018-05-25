# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZhihuItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 帖子
    url = scrapy.Field()
    # 标题
    title = scrapy.Field()
    # 描述
    description = scrapy.Field()
    # 用户
    user = scrapy.Field()
    # 回复
    answer = scrapy.Field()
