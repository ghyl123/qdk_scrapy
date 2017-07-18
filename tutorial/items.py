# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class QdkItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # for ImagesPipeline
    image_urls = scrapy.Field()
    images = scrapy.Field()
    id = scrapy.Field()
    cover = scrapy.Field()
    title = scrapy.Field()


class QdkListItem(scrapy.Item):
    id = scrapy.Field()
    list_urls = scrapy.Field()