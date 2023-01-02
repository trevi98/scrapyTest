from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class FamSpider(CrawlSpider):
    name = "famspider"
    allowed_domains = ['famproperties.com']
    start_urls = ["https://famproperties.com"]
    rules = (
        Rule(LinkExtractor(allow="/")),
    )