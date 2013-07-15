# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field


class MytestudoItem(Item):
    # define the fields for your item here like:
    dept_abbr = Field()
    dept_long = Field()

