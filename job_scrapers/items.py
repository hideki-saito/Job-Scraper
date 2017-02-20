# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JobScraperItem(scrapy.Item):
    title = scrapy.Field()
    body = scrapy.Field()
    link = scrapy.Field()
    source = scrapy.Field()
    company = scrapy.Field()
    company_description = scrapy.Field()
    deadline = scrapy.Field()
    salary = scrapy.Field()
    location = scrapy.Field()
    scrap_date = scrapy.Field()
