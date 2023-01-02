from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class FamSpider(CrawlSpider):
    name = "famspider"
    allowed_domains = ['propertyfinder.ae']
    start_urls = ["https://www.propertyfinder.ae/blog/"]
    rules = (
        Rule(LinkExtractor(allow="blog",),callback = "parse_blog"),
        Rule(LinkExtractor(), follow=True),
        # Rule()
    )

    def parse_blog(self, response):
        yield {
            "title" : response.css('.entry-title::text').get(),
            "description" : response.css('.entry-content::text').get()
        }
