# Pipelines are used to process scraped items.
# We use AYpiPipeline to process the item and produce a dictionary of dictionaries and then store it to 'a11ypi_dict.json' file.
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html
import json 

class AYpiPipeline(object):
    def __init__(self):
	self.file = open("a11ypi_dict.json","ab+")
	
	
   # this method is called to process an item after it has been scraped.
    

    def process_item(self, item, spider):
	d = {}	
	 
	i = 0
	# Here we are iterating over the scraped items and creating a dictionary of dictionaries.
	try:
	    while i<len(item["foruri"]):
		d.setdefault(item["foruri"][i],{}).setdefault(item["rec"][i],{})[item["foruri_id"][i]] = item['thisurl'] + ":" +item["thisid"][i]
		i+=1
	except IndexError:
	    print "Index out of range"
	
	json.dump(d,self.file)

				
	return item
	
	
