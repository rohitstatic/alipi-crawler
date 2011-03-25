from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector

from a11ypi.items import AYpiItem

class AYpiSpider(BaseSpider):
    name = "a11y.in"
    allowed_domains = ["a11y.in"]
    start_urls = ["http://a11y.in/a11ypi/idea/a11y_firesafety.html", "http://localhost/a11y/renarr.html"]
    
    def parse(self,response):
	#filename = response.url.split("/")[-1]
	#open(filename,'wb').write(response.body)
	#testing codes ^ (the above)
	#items= []
	hxs = HtmlXPathSelector(response)
	item = AYpiItem()
	wholeforuri = hxs.select("//@foruri").extract()
	item["foruri"] = [i.split(":")[-2] for i in wholeforuri]
	item["foruri_id"] = [i.split(":")[-1] for i in wholeforuri]
	item['thisurl'] = response.url
	item["thisid"] = hxs.select("//@foruri/../@id").extract()
	item["rec"] = hxs.select("//@foruri/../@rec").extract()
	#items.append(item)
	return item    


