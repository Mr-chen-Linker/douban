# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ItcastrojectItem(scrapy.Item):
    # define the fields for your item here like:
    # specialty = scrapy.Field()
    name = scrapy.Field()
    title = scrapy.Field()
    info = scrapy.Field()

    # pass
