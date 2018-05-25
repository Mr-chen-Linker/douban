# -*- coding: utf-8 -*-
from scrapy import signals
from douban.settings import USERAGENTS
from douban.settings import PROXYS
import random
import base64


class RandomUseragentDownloaderMiddleware(object):
    '''随机useragent中间件类'''

    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.
    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        # 随机从随机agent池随机选一个出来
        useragent = random.choice(USERAGENTS)
        print(useragent)
        request.headers.setdefault("User-Agent", useragent)

        return None


class RandomProxyDownloaderMiddleware(object):
    '''随机代理中间件类'''

    def process_request(self, request, spider):
        proxy = random.choice(PROXYS)
        # print(proxy)
        if proxy["user_passwd"] is None:
            # 如果代理不需要验证的话
            request.meta["proxy"] = "http://" + proxy["ip_port"]
        else:
            # # 需要验证的话需要进行Base64编码转换
            # b64_userpass = base64.b64decode(proxy["user_passwd"])
            # request.meta["proxy"] = "http://" +proxy["ip_port"]
            # print(request.meta["proxy"])
            #
            # request.headers["Proxy-Authorization"] = "Basic " + b64_userpass

            # 对账户密码进行base64编码转换
            # base64_userpasswd = base64.b64encode(proxy['user_passwd'],altchars=False)
            # # 对应到代理服务器的信令格式里
            # request.headers['Proxy-Authorization'] = 'Basic ' + base64_userpasswd
            #
            # request.meta['proxy'] = "http://" + proxy['ip_port']
            pass
