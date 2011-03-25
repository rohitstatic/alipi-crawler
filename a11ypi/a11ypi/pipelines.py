# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html
import json 

class AYpiPipeline(object):
    def __init__(self):
	self.f = open("../a11ypi_dict.json","ab")
	
   
    def process_item(self, item, spider):
	d = {}
	i=0
	try:
	    while i<=len(item["foruri"]):
		d.setdefault(item["foruri"][i],{}).setdefault(item["rec"][i],{})[item["foruri_id"][i]] = item['thisurl'] + ":" + item["thisid"][i]
		i+=1
	except IndexError:
	    print ""
	print d	
	json.dump(d,self.f)
	try:
	    #self.f.write(s)
	    self.f.close()
	except:
	    print "some error"     
	return item
