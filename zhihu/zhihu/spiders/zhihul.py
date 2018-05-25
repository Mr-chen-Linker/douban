# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spider import Rule, CrawlSpider
from scrapy import Selector
from scrapy import Request, FormRequest
from ..items import ZhihuItem

class ZhihulSpider(scrapy.Spider):
    name = 'zhihul'
    allowed_domains = ['zhihu.com']
    start_urls = ['http://www.zhihu.com/signup']

    headers = {"Accept": "*/*", "Accept-Encoding": "gzip,deflate",
        "Accept-Language": "en-US,en;q=0.8,zh-TW;q=0.6,zh;q=0.4", "Connection": "keep-alive",
        "Content-Type": " application/x-www-form-urlencoded; charset=UTF-8",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36",
        "Referer": "http://www.zhihu.com/"}

    # 重写start_requests方法，意味着第一次访问需要自己控制，
    # 这里是相当于浏览器访问知乎网的登录界面，生成访问请求到的响应交给post_login()处理
    # def start_requests(self):
    #     return [Request(url="http://www.zhihu.com/signup", callback=self.after_login, meta={'cookiejar': 1})]

    def parse(self, response):

        return [scrapy.FormRequest.from_response(
            response,
            formdata={"username":"+8616602124256","password":"chienjianlin1"},
            headers=self.headers,
            callback=self.after_login
        )]

    # 访问登录界面拿到的响应处理方法
    def after_login(self, response):
        print("Preparing login zhihu.com......")

        print(response.code)
        print(response.body)

