# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import TencentrItem


class TencentrSpider(CrawlSpider):
    name = 'tencentr'
    allowed_domains = ['hr.tencent.com']
    start_urls = ['https://hr.tencent.com/position.php?&start=0']

    # 通过LinkExtractor（）实例化一个匹配规则对象
    # 通过请求的第一页中的页码各个请求url中存在start= 的字样来设置一个规则
    pageLink = LinkExtractor(allow="start=\d+")

    # 保存各个规则对象的列表
    rules = [# 上面定义的获取下一页url的规则
        Rule(pageLink,

             # 根据上述规则取得url调度器去下载后，拿到的响应交给一个回调函数去处理，这里不能条用parse()函数，需要自行写一个解析响应的函数
             callback='parseTencent',

             # 是否深度爬取，默认为True
             follow=True), ]

    def parseTencent(self, response):
        for each in response.xpath('//tr[@class="even"] | //tr[@class="odd"]'):
            # 实例化一个模型对象
            item = TencentrItem()

            item['postionName'] = each.xpath('./td[1]/a/text()').extract()[0]
            item['postionLink'] = "http://hr.tencent.com/" + each.xpath('./td[1]/a/@href').extract()[0]
            item['postionType'] = each.xpath('.//td[2]/text()').extract()[0]
            item['postionNum'] = each.xpath('.//td[3]/text()').extract()[0]
            item['postionAddr'] = each.xpath('.//td[4]/text()').extract()[0]
            item['time'] = each.xpath('./td[5]/text()').extract()[0]

            # 将每页拿到的职位信息的item模型对象返回个管道
            yield item
