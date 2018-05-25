# -*- coding: utf-8 -*-
import scrapy
from ..items import DouyuItem
import json


class DouyudownphtoSpider(scrapy.Spider):
    # 爬虫名
    name = 'douyu'
    # 作用域
    allowed_domains = ['capi.douyucdn.cn']
    # 首次请求地址
    url = "http://capi.douyucdn.cn/api/v1/getVerticalRoom?limit=20&offset="
    # 请求页码偏移量
    offset = 0
    start_urls = [url + str(offset)]

    def parse(self, response):
        # 实例化模型对象
        item = DouyuItem()
        # 将返回的JSON格式字符串 转换为python的字典类型
        data = json.loads(response.text)["data"]

        for each in data:
            item["nickname"] = each["nickname"]
            item["img_urls"] = each["vertical_src"]

            yield item

        # 控制请求第二页的判断

        self.offset += 20
        #发送下一个页面请求给调度器去请求下载响应
        yield scrapy.Request(self.url + str(self.offset), callback=self.parse)
