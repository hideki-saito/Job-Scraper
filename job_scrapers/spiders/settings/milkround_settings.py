# -*- coding: utf-8 -*-
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor


class MilkroundSettings:
    source = "milkround.com"
    allowed_domains = [source]
    start_urls = ["http://www.milkround.com/jobs/construction-and-property/"]

    rules = (
        Rule(LinkExtractor(allow="jobs/construction-and-property/\d+/"), follow=True, callback='parse_page'),
    )

    job_link = "h3.lister__header > a::attr('href')"

    xpath_job_title = "//h1/text()"
    xpath_job_body = "string(//div[@itemprop='description'])"
    xpath_info = "//div[contains(concat(' ', @class, ' '),' card ')]/dl"

    xpath_company = "//span[@itemprop='name']/text()"
    xpath_deadline = "//div[5]/dd/text()"
    xpath_salary = "//div[3]/dd/text()"
    xpath_location = "//div[2]/dd/text()"

    def parse_company(self, company):
        return company
