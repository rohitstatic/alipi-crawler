# We define here the model for our scraped items.
# We use the AYpiItem to store the scraped data and to process them later.
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class AYpiItem(Item):
     
    foruri = Field()     # this is to store the URL part of the foruri attrib
    foruri_id = Field()  # this is to store the id part of the foruri attrib
    thisid = Field()     # this stores the id of the element containing the foruri
    rec = Field()	 # this stores the rec attrib
    thisurl = Field()    # this stores the URL of the page containg the renarration, the page it is crawling
    
    
