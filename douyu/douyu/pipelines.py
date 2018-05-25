# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
from scrapy.pipelines.images import ImagesPipeline
from scrapy.utils.project import get_project_settings
import os


class DouyuPipeline(ImagesPipeline):

    #从setting配置中得到配置好的 保存路径
    IMAGES_STORE=get_project_settings().get("IMAGES_STORE")


    def get_media_requests(self, item, info):
        # 将获取的图片http链接再次构成请求发给调度器
        yield scrapy.Request(item["img_urls"])

    def item_completed(self, results, item, info):

        image_path = [x['path'] for ok, x in results if ok]

        #保存文件夹重命名
        os.rename(self.IMAGES_STORE + "/" + image_path[0], self.IMAGES_STORE + "/" + item["nickname"] + ".jpg")

        item["img_path"] =self.IMAGES_STORE + "/" + item["nickname"]


        return item
