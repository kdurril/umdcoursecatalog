#!/usr/bin/env
#use to extraction section information
#This is dependent on course info from testudo_crawler.py
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from mytestudo.items import DeptItem, CourseItem, SectionItem

import csv
import codecs
from os import path

def get_course_list():
    "get list of course numbers for list to directly access pages"
    with codecs.open("C:/Users/kdurril/Documents/scrapy/mytestudo/courses.csv","r", "utf-8") as f:
        courses_file = csv.DictReader(f, delimiter=',', quotechar='"')
        courselist = [x['course_name'] for x in courses_file]
        courselist.sort()
    return courselist

class TestudoSpider(BaseSpider):

    name = 'testudo_sections'
    allowed_domains = ['ntst.umd.edu']
    term = "201501"
    
    if path.exists("C:/Users/kdurril/Documents/scrapy/mytestudo/courses.csv"):
        courselist = get_course_list()
    else:
        c = codecs.open("C:/Users/kdurril/Documents/scrapy/mytestudo/courses.csv","w", "utf-8")
        c.close()
        courselist = get_course_list()

    base_url = 'https://ntst.umd.edu/soc/'
    term_url =  '''{term}/{dept}/{course}'''
    start_urls = [base_url+term_url.format(term=term, dept=course[:4],\
                  course=course) for course in courselist]

    #start_urls = ['https://ntst.umd.edu/soc/201408/PUAF/PUAF610',\
    #              'https://ntst.umd.edu/soc/201408/PUAF/PUAF650']

    def parse(self, response):
        x = HtmlXPathSelector(response)
        
        rows = x.select('//div[@class="course-prefix row"]') #use this selector for main page that list top level dept
        row_list = []

        sites = x.select('//div[@class="course"]') # use this for dept page e.g. PUAF
        items = []
        
        sections = x.select('//div[@class="section"]')

        # Department information

        item_section = list()
        for section in sections:

            # Section Information
            sectionlist = SectionItem()
            sectionlist['semester'] = self.term
            sectionlist['course_number'] = x.select('descendant::div[@class="course-id"]/text()').extract()
            sectionlist['section_num'] = section.select('''descendant::span[@class='section-id']/text()''').extract()
            sectionlist['section_num'] = sectionlist['section_num'][0].strip()            
            sectionlist['section_instructor'] = section.select('''descendant::span[@class='section-instructor']/text()''').extract()
            sectionlist['section_seats'] = section.select('''descendant::span[@class='total-seats-count']/text()''').extract()
            sectionlist['section_remain'] = section.select('''descendant::span[@class='open-seats-count']/text()''').extract()
            sectionlist['section_waitlist'] = section.select('''descendant::span[@class='waitlist-count']/text()''').extract()
            sectionlist['section_day'] = section.select('''descendant::span[@class='section-days']/text()''').extract()
            sectionlist['section_time_start'] = section.select('''descendant::span[@class='class-start-time']/text()''').extract()
            sectionlist['section_time_end'] = section.select('''descendant::span[@class='class-end-time']/text()''').extract()
            sectionlist['section_building'] = section.select('''descendant::span[@class='building-code']/text()''').extract()
            #sectionlist['section_class_type'] = section.select('''//span[@class='class-type']/text()''').extract()
            item_section.append(sectionlist)

        #torrent['section'] = item_section
        #items.append(item_section)
        return item_section


