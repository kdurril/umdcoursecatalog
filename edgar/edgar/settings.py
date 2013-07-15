# Scrapy settings for edgar project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'edgar'

SPIDER_MODULES = ['edgar.spiders']
NEWSPIDER_MODULE = 'edgar.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'edgar (+http://www.yourdomain.com)'
