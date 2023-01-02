from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class FamSpider(CrawlSpider):
    name = "famspider"
    allowed_domains = ['propertyfinder.ae']
    start_urls = ["https://www.propertyfinder.ae/"]
    rules = (
        # Rule(LinkExtractor(allow="blog",),callback = "parse_blog"),
        Rule(LinkExtractor(allow="buy",deny="properties-for-sale.html"),callback = "parse_buy"),
        Rule(LinkExtractor(), follow=True),

        # Rule()
    )

    def parse_blog(self, response):
        yield {
            "title" : response.css('.entry-title::text').get(),
            "description" : response.css('.entry-content::text').get()
        }

    def parse_buy(self,response):
        yield{
            "title" : response.css(".property-page__title::text").get(),
            "description" : response.css(".property-description__text-trim::text").get()
        }
