# -*- coding: utf-8 -*-
import scrapy
from ..items import TencentItem


class TencentpostionSpider(scrapy.Spider):
    # 爬虫名称
    name = 'tencent'
    # 允许爬去的域名范围
    allowed_domains = ['hr.tencent.com']

    # 用于控制请求url中的页码
    offset = 0

    url = "https://hr.tencent.com/position.php?&start="
    # 首次爬去的url地址
    start_urls = [url + str(offset)]

    def parse(self, response):
        # "//tr[@class='even'] | //tr[@class='odd']"
        for each in response.xpath('//tr[@class="even"] | //tr[@class="odd"]'):
            # 实例化一个模型对象
            item = TencentItem()

            item['postionName'] = each.xpath('./td[1]/a/text()').extract()[0]
            item['postionLink'] = "http://hr.tencent.com/" + each.xpath('./td[1]/a/@href').extract()[0]
            item['postionType'] = each.xpath('.//td[2]/text()').extract()[0]
            item['postionNum'] = each.xpath('.//td[3]/text()').extract()[0]
            item['postionAddr'] = each.xpath('.//td[4]/text()').extract()[0]
            item['time'] = each.xpath('./td[5]/text()').extract()[0]

            # 将每页拿到的职位信息的item模型对象返回个管道
            yield item

        if self.offset < 20:
            self.offset += 10  # 重新发请求给引擎，引擎给调度器，然后去下载响应，回调函数必须写parse即将响应交给它处理
        yield scrapy.Request(self.url + str(self.offset), callback=self.parse)
