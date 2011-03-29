from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from a11ypi.items import AYpiItem

class AYpiSpider(CrawlSpider):
    name = "a11y.in"
    allowed_domains = ["a11y.in"]
    
    # This is the list of seed URLs to begin crawling with.
    start_urls = ["http://rookie-trekker.blogspot.com"]
    
    # This is the callback method, which is used for scraping specific data
    def parse(self,response):
	temp = []
	hxs = HtmlXPathSelector(response)
	item = AYpiItem()
	wholeforuri = hxs.select("//@foruri").extract()            # XPath to extract the foruri, which contains both the URL and id in foruri
	for i in wholeforuri:
		temp.append(i.rpartition(":"))
	
	item["foruri"] = [i[0] for i in temp]     # This contains the URL in foruri
	item["foruri_id"] = [i.split(":")[-1] for i in wholeforuri]  # This contains the id in foruri
	item['thisurl'] = response.url                                  
	item["thisid"] = hxs.select("//@foruri/../@id").extract()
	item["rec"] = hxs.select("//@foruri/../@rec").extract()
	return item    


