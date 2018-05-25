import scrapy
from ..items import ItcastrojectItem


# 创建一个爬虫类
class ItcastSpiser(scrapy.Spider):
    # 爬虫名
    name = "itcast"

    # 指定爬虫爬取的作用于，必须是列表格式 可以有很多个
    allowd_domains = ["http://www.itcast.cn/"]

    # 首次请求的地址 必须是列表格式，可以包括很多个
    start_urls = ["http://www.itcast.cn/channel/teacher.shtml#"]

    def parse(self, response):
        # 解析老师信息用scrapy自带的xpath()
        teache_list = response.xpath('//div[@class="li_txt"]')
        # 创建一个列表保存每次爬出来的老师信息
        # teacherItems = []
        # 实例化一个item对象
        item = ItcastrojectItem()

        for each in teache_list:
            # 姓名
            name = each.xpath(".//h3/text()").extract()
            # title
            title = each.xpath("./h4/text()").extract()
            # 简介
            info = each.xpath(".//p/text()").extract()

            item["name"] = name[0]
            item["title"] = title[0]
            item["info"] = info[0]

            yield item
            #列表保存包含所有老师的实例化的item对象
            # teacherItems.append(item)

        # return teacherItems
