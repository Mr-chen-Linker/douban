# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TencentrItem(scrapy.Item):
    # 职位名称
    postionName = scrapy.Field()
    # 详细信息链接
    postionLink = scrapy.Field()
    # 职位类别
    postionType = scrapy.Field()
    # 职位招聘人数
    postionNum = scrapy.Field()
    # 职位工作地址
    postionAddr = scrapy.Field()
    # 发布时间
    time = scrapy.Field()