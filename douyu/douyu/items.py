# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DouyuItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #主播名字
    nickname=scrapy.Field()
    # 图片的连接地址
    img_urls=scrapy.Field()
    # 地址下载的地址
    img_path=scrapy.Field()
    pass
