from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class FamSpider(CrawlSpider):
    name = "famspider"
    allowed_domains = ['famproperties.com']
    start_urls = ["https://famproperties.com/blog/"]
    rules = (
        Rule(LinkExtractor(allow="blog",),callback = "parse_blog"),
        # Rule()
    )

    def parse_blog(self, response):
        yield {
            "title" : response.css('#project h1::text').get(),
            "description" : response.css('#R12848563557498805588_report li .t-Comments-body .t-Comments-comment').get()
        }
