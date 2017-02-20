# -*- coding: utf-8 -*-
import datetime
#import sys
#sys.path.append("/Users/Omid/Desktop/MyPyCode/scrapers/job_scrapers/job_scrapers/")
import re
from dateutil.relativedelta import relativedelta
import scrapy
from scrapy.spiders import CrawlSpider
from job_scrapers.items import JobScraperItem
from settings.settings_factory import SettingsFactory


class GenericScraper(CrawlSpider):
    SPEC_REG = u'[\r\n]+'
    name = 'jobs'
    date_format = "%d %b %Y"

    # TODO: Create settings factory and split settings for reed.co and milkround
    def __init__(self, name='reed', *a, **kw):
        super(GenericScraper, self).__init__(*a, **kw)
        global settings
        settings = SettingsFactory.get_settings(name)

        self.source = settings.source

        self.rules = settings.rules
        self.allowed_domains = settings.allowed_domains
        self.start_urls = settings.start_urls
        print '\n\n\n', self.start_urls, "\n\n\n"
        super(GenericScraper, self)._compile_rules()

    def parse_page(self, response):
        print '\n\n\n', response.url, '\n\n\n'
        for link in response.css(settings.job_link):
            url = response.urljoin(link.extract())
            yield scrapy.Request(url, callback=self.parse_vacancy)

    def parse_vacancy(self, response):
        item = JobScraperItem()
        item['title'] = self.remove_spec_chars(
            self.SPEC_REG,
            response.xpath(settings.xpath_job_title).extract()[0]
        )
        body = response.xpath(settings.xpath_job_body).extract()
        body[0] = self.remove_spec_chars(self.SPEC_REG, body[0])
        # des = body[0].encode('utf-8')
        des  ="".join(filter(lambda x: ord(x)<128, body[0]))
        # file = open("/home/omid/jobs/job1.txt","a")
        file = open("/root/a1.txt", "a")
        file.write(des)
        file.write("\n\n")
        file.close()
        item['body'] = body
        item['link'] = response.url
        item['source'] = settings.source
        info = response.xpath(settings.xpath_info)
        #item['company'] = info.xpath(settings.xpath_company).extract()[0]
        item['company'] = ""
        deadline = None
        if settings.xpath_deadline:
            deadline = self.get_date(
                self.remove_spec_chars(
                    self.SPEC_REG,
                    info.xpath(settings.xpath_deadline).extract()[0]
                )
            )

        if deadline:
            item['deadline'] = deadline.strftime(self.date_format)
        else:
            item['deadline'] = (datetime.datetime.now() + relativedelta(months=1)).strftime(self.date_format)
        """
        item['salary'] = self.remove_spec_chars(
            self.SPEC_REG,
            info.xpath(settings.xpath_salary).extract()[0]
        )
        """
        item['salary'] = ""
        """
        item['location'] = self.remove_spec_chars(
            self.SPEC_REG,
            info.xpath(settings.xpath_location).extract()[0]
        )
        """
        item['location'] = ""
        item['scrap_date'] = datetime.datetime.now()
        item['company_description'] = ""
        yield item

    def parse_start_url(self, response):
        return self.parse_page(response)

    def remove_spec_chars(self, regexp, string):
        br_string = re.sub(regexp, u"<br />", string).strip()
        br_string = re.sub("[\s]+", u" ", br_string)
        return re.sub(r"[[<br />][\s]+[<br />]]+", u" ", br_string)

    def get_date(self, date):
        try:
            date = datetime.datetime.strptime(date, settings.deadline_format)
        except:
            date = None
        return date
