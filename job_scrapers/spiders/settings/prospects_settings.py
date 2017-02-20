from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule

class ProspectsSettings:
    '''Setting file for parsing 'prospects.ac.uk '''

    # vacancy source
    source = "prospects.ac.uk"

    # Allowed domains for prospects
    allowed_domains = [source]

    # Starting url
    start_urls = ["https://www.prospects.ac.uk/graduate-jobs-results?sortBy=dp&careers=69&size=50&page=0"]

    # Rule to search next page
    rules = (
        Rule(LinkExtractor(allow="\.*?p=\d+\.*"), follow=True, callback="parse_page"),
    )

    # CSS selector of vacancy link
    job_link = "tr.titlerow > td > a::attr('href')"

    # XPATH Selector of title, body, company, info block,
    # salary, deadline location respectively
    xpath_job_title = "//h1/text()"
    xpath_job_body = "string(//div[@class='simplefullwidth'])"
    xpath_company = "//h1/span/text()"
    xpath_info = "//dl[@class='simpledefinitionlist']"
    xpath_salary = "dd[1]/text()"
    xpath_deadline = "dt[contains(text(),'Closing date')]/following-sibling::dd[1]/text()"
    xpath_location = "dt[contains(text(),'Location')]/following-sibling::dd[1]/text()"

    # Deadline date format specific for 'prospects'
    # used to convert deadline to format specified in GenericScraper
    deadline_format = "%d/%m/%Y"

    def parse_company(self, company):
        return company
