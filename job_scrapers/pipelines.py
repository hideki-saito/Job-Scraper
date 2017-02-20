# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from vacancies_scrap.models import Vacancy

class JobScraperPipeline(object):
    def process_item(self, item, spider):
        Vacancy.save_vacancy(item)
        return item
