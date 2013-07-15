# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class T2Item(Item):
    # define the fields for your item here like:
    # name = Field()
    # define department fields
    dept_link = Field()
    dept_short = Field()
    dept_long = Field()
