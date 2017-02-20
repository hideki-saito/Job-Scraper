import requests
from bs4 import BeautifulSoup
from urlparse import urljoin

from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor


def get_field_urls():
    base_url1 = "https://www.reed.co.uk/jobs/it-jobs/"
    base_url2 = "https://www.reed.co.uk/jobs/sales/"

    r = requests.get(base_url1)
    soup = BeautifulSoup(r.content, 'lxml')
    urls1 = [urljoin(base_url1, item.get('href')) for item in soup.find("ul", attrs={"class": "facets sectors"}).find_all('a')]

    r = requests.get(base_url2)
    soup = BeautifulSoup(r.content, 'lxml')
    urls2 = [urljoin(base_url2, item.get('href')) for item in
             soup.find("ul", attrs={"class": "facets sectors"}).find_all('a')]

    urls = urls1 + urls2

    return urls

class ReedCoUkSettings:
    source = "reed.co.uk"
    allowed_domains = [source]
    # start_urls = ["http://www.reed.co.uk/jobs/it-jobs/"]
    # start_urls =["http://www.reed.co.uk/jobs/systems-senior-analyst-bi/31680227#/jobs/it-jobs/"]
    start_urls = get_field_urls()

    rules = (
        Rule(LinkExtractor(restrict_xpaths='//a[@title="Go to next page"]'), follow=True, callback="parse_page"),
    )
    #job_link = "ul.unstyled-list > li > a::attr('href')"
    job_link = "h3.title > a::attr('href')"
    xpath_job_title = "//h1[@itemprop='title']/text()"
    xpath_job_body = "string(//div[@class='description'])"
    xpath_info = "//div[contains(concat(' ', @class, ' '),' detailLists ')]"
    xpath_company = "substring(//div[@class='logoProfile']/a/img/@alt | " \
                    "//div[@class='logoProfile']/span/text()[preceding-sibling::br], 11)"
    xpath_salary = "ul[1]/li[2]/text()"
    xpath_location = "string(ul[1]/li[1])"
    xpath_deadline = None

    def parse_company(self, company):
        return company

