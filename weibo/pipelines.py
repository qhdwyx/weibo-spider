# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import os
import time
from requests import request
from weibo.usersettings import headers, cookies, savepath


class WeiboPipeline(object):
    project_dir = savepath
    cnt = 0
    imagefoldername = 'image'+ str(int(time.time()))

    def process_item(self, item, spider):
        foldername = item['catelog'][0]
        for photo in item['photos']:
            photo = 'http:' + photo
            response = request(url=photo, headers=headers, cookies=cookies, method='GET')
            name = photo.split('/')[-1]
            self.save_image(response, foldername, name)
        return item

    def save_image(self, response, foldername, filename):
        filepath = os.path.join(self.project_dir, self.imagefoldername, foldername)
        if not os.path.exists(filepath):
            os.makedirs(filepath)
        filepath = os.path.join(filepath, filename)
        f = open(filepath, 'wb')
        f.write(response.content)
        f.close()


