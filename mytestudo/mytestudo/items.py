# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field


class DeptItem(Item):
# define department fields
    dept = Field()
    dept_link = Field()
    dept_short = Field()
    dept_long = Field()
    course = Field()


class CourseItem(Item):
# define course
    course_name = Field()
    course_title = Field()
    course_credit = Field()
    course_gradetype = Field()
    course_text = Field()
    section = Field()

class SectionItem(Item):
    # the next values are by sections
    semester = Field()
    course_number = Field()
    section_num = Field()
    section_instructor = Field()
    section_seats = Field()
    section_remain = Field()
    section_waitlist = Field()
    section_day = Field()
    section_time_start = Field()
    section_time_end = Field()
    section_building = Field()
    section_type = Field()

