# -*- coding: utf-8 -*-
import scrapy
from tutorial.items import QdkItem
from tutorial.items import QdkListItem
import math
import re


class QDKSpider(scrapy.Spider):
    name = 'qdk'
    start_urls = [
        'http://www.aisinei.com/thread-12140-1-4.html',
    ]

    def parse(self, response):
        item = QdkItem()
        item['title'] = response.css('#thread_subject::text').extract_first()
        item['image_urls'] = []
        item['id'] = []

        secret_num = response.css('td.t_f::attr(id)').extract_first()[-5:]

        item['cover'] = response.css(
            'td.t_f ignore_js_op img::attr(zoomfile)').extract_first()
        item['image_urls'].append(item['cover'])
        item['id'].append('cover.jpg')

        secret_css = '#imagelist_' + secret_num + ' ignore_js_op'

        for img in response.css(secret_css):
            item['id'].append(img.css('dl dd p.mbn a::text').extract_first())
            item['image_urls'].append(
                img.css('dl dd div.mbn.savephotop img::attr(zoomfile)')
                .extract_first())

        yield item


class QDKListSpider(scrapy.Spider):
    name = 'qdklist'
    start_urls = [
        'http://www.aisinei.com/forum-qingdouke-1.html',
    ]

    def parse(self, response):
        item = QdkListItem()
        item['list_urls'] = []
        for li in response.css('#moderate > div.bus_w100.bu_fl.pt20 ul li'):
            item['list_urls'].append(
                li.css('div.bus_vtem a::attr(href)').extract_first())
        yield item

        # look for next link
        list_num = int(response.css('em.bus_num::text').extract_first())
        page_max_num = math.ceil(list_num / 20)
        url_pattern = re.compile(r'(?<=-)\d{1,3}(?=\.html)')
        page_num = url_pattern.search(response.url)
        if not page_num:
            print('cannot find page_num in url: ', response.url)
        else:
            page_num = int(page_num.group())
            if (page_max_num > page_num):
                page_num = str(page_num + 1)
                next_url = url_pattern.sub(page_num, response.url)
                yield response.follow(next_url, callback=self.parse)


class QSpider(scrapy.Spider):

    name = 'q'

    start_urls = [
        'http://www.aisinei.com/forum-qingdouke-1.html',
    ]

    def parse(self, response):
        item = QdkListItem()
        item['list_urls'] = []
        for li in response.css('#moderate > div.bus_w100.bu_fl.pt20 ul li'):
            new_url = li.css('div.bus_vtem a::attr(href)').extract_first()
            item['list_urls'].append(new_url)
            yield response.follow(new_url, callback=self.parse_content)
        yield item

        # look for next link
        list_num = int(response.css('em.bus_num::text').extract_first())
        page_max_num = math.ceil(list_num / 20)
        url_pattern = re.compile(r'(?<=-)\d{1,3}(?=\.html)')
        page_num = url_pattern.search(response.url)
        if not page_num:
            print('cannot find page_num in url: ', response.url)
        else:
            page_num = int(page_num.group())
            if (page_max_num > page_num):
                page_num = str(page_num + 1)
                next_url = url_pattern.sub(page_num, response.url)
                yield response.follow(next_url, callback=self.parse)

    def parse_content(self, response):
        item = QdkItem()
        item['title'] = response.css('#thread_subject::text').extract_first()
        item['image_urls'] = []
        item['id'] = []

        secret_num = response.css('td.t_f::attr(id)').extract_first()[-5:]

        item['cover'] = response.css(
            'td.t_f ignore_js_op img::attr(zoomfile)').extract_first()
        item['image_urls'].append(item['cover'])
        item['id'].append('cover.jpg')

        secret_css = '#imagelist_' + secret_num + ' ignore_js_op'

        for img in response.css(secret_css):
            item['id'].append(img.css('dl dd p.mbn a::text').extract_first())
            item['image_urls'].append(
                img.css('dl dd div.mbn.savephotop img::attr(zoomfile)')
                .extract_first())

        yield item
