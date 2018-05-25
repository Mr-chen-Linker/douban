# -*- coding: utf-8 -*-

from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import SunItem


class SundgSpider(CrawlSpider):
    name = 'sundg'
    allowed_domains = ['wz.sun0769.com']
    start_urls = ['http://wz.sun0769.com/index.php/question/questionType?type=4&page=']

    # 创建规则对象
    # 1.页码爬取规则
    pageRule = LinkExtractor(allow=r"type=4&page=\d+")

    tieziRule = LinkExtractor(allow=r"/question/\d+/\d+.shtml")

    rules = (Rule(pageRule, follow=True), Rule(tieziRule, callback="parseDongguan", follow=False))

    def parseDongguan(self, response):
        # print(response.url)

        item = SunItem()

        # 标题
        item["title"] = response.xpath('//div[@class="pagecenter p3"]//strong/text()').extract()[0]
        # 编号
        item['numberNo'] = item["title"].split(" ")[-1].split(":")[-1]
        # 内容
        # 这里存在问题，因为有的帖子是存在图片的，对于有图片的帖子，内容就不再是//div[@class="c1 text14_2"]/text()采集了
        # 而是要用// div[ @class ="contentext"] / text()

        content = response.xpath('//div[@class="contentext"]/text()').extract()
        # 页面是没有图片的
        if len(content) == 0:
            item["content"] = "".join(response.xpath('//div[@class="c1 text14_2"]/text()').extract())
        else:
            item["content"] = "".join(content)
        # 链接
        item["url"] = response.url

        yield item
