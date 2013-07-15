# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class TutorialItem(Item):
    # define the fields for your item here like:
    # name = Field()
    pass


class TestudoItem(Item):
    # define the fields for your item here like:
    course_name = Field()
    course_number = Field()
    course_credit = Field()
    course_gradetype = Field()
    course_text = Field()
    course_prerequisite = Field()
    # the next values are by sections
    course_section = Field()
    course_instructor = Field()
    course_seats = Field()
    course_remain = Field()
    course_day = Field()
    course_time = Field()
    course_room = Field()
    
    pass