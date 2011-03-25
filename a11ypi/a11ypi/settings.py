# Scrapy settings for a11ypi project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'a11ypi'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['a11ypi.spiders']
NEWSPIDER_MODULE = 'a11ypi.spiders'
DEFAULT_ITEM_CLASS = 'a11ypi.items.AYpiItem'
ITEM_PIPELINES = ['a11ypi.pipelines.AYpiPipeline']
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)

