# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
import os.path
from scrapy.conf import settings


def clean_path(path):
    path = path.replace('/', '-')
    path = path.replace('\\', '-')
    path = path.replace(':', '-')
    path = path.replace('?', '-')
    path = path.replace('<', '-')
    path = path.replace('>', '-')
    path = path.replace('\'', '-')
    path = path.replace('\"', '-')
    path = path.replace('*', '-')
    path = path.replace('|"', '-')
    return path


class RenamePipeline(object):
    def process_item(self, item, spider):
        if (spider.name == 'qdklist'):
            return item
        elif not item['images']:
            return item

        imgpath = settings.get('IMAGES_STORE')
        dirname = clean_path(item['title'])
        dirpath = os.path.join(imgpath, dirname)
        os.makedirs(dirpath, exist_ok=True)

        for id, img in zip(item['id'], item['images']):
            src = os.path.join(imgpath, img['path'])
            dst = os.path.join(dirpath, id)
            if os.path.exists(dst):
                os.remove(src)
            else:
                os.rename(src, dst)
            # try:
            #     os.rename('./' + img['path'], os.path.join(dirpath, id))
            # except OSError:
            #     print('can not rename file: ', img['path'])
            #     print(OSError)

        return item
