#!/usr/bin/env
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from mytestudo.items import DeptItem, CourseItem, SectionItem

import csv
import codecs

def get_course_list():
    "get list of course numbers for list to directly access pages"
    with codecs.open("C:/Users/kdurril/Documents/student_directory/evaluation/courseplan/courses.csv","r", "utf-8") as f:
        courses_file = csv.reader(f, delimiter='\t')
        courselist = [x[1] for x in courses_file]
    return courselist

class TestudoSpider(BaseSpider):

    name = 'testudo_sections'
    allowed_domains = ['ntst.umd.edu']

    abbrlist = ['AASP', 'AAST', 'AGNR', 'AMSC', 'AMST', 'ANSC', 'ANTH', 'AOSC',\
                'ARAB', 'ARCH', 'AREC', 'ARHU', 'ARMY', 'ARSC', 'ARTH', 'ARTT',\
                'ASTR', 'BCHM', 'BEES', 'BIOE', 'BIOL', 'BIOM', 'BIPH', 'BISI',\
                'BMGT', 'BSCI', 'BSCV', 'BSGC', 'BSOS', 'BSST', 'BUAC', 'BUDT',\
                'BUFN', 'BULM', 'BUMK', 'BUMO', 'BUSI', 'CBMG', 'CCJS', 'CHBE',\
                'CHEM', 'CHIN', 'CHPH', 'CLAS', 'CLFS', 'CMLT', 'CMSC', 'COMM',\
                'CONS', 'CPSP', 'DANC', 'EALL', 'ECON', 'EDCI', 'EDCP', 'EDHD',\
                'EDHI', 'EDMS', 'EDPS', 'EDSP', 'EDUC', 'EMBA', 'ENAE', 'ENBE',\
                'ENCE', 'ENCH', 'ENCO', 'ENEE', 'ENES', 'ENFP', 'ENGL', 'ENMA',\
                'ENME', 'ENNU', 'ENPM', 'ENPP', 'ENRE', 'ENSE', 'ENSP', 'ENST',\
                'ENTM', 'ENTS', 'EPIB', 'FILM', 'FMSC', 'FOLA', 'FREN', 'GEMS',\
                'GEOG', 'GEOL', 'GERM', 'GREK', 'GVPT', 'HACS', 'HDCC', 'HEBR',\
                'HEIP', 'HESP', 'HHUM', 'HISP', 'HIST', 'HLSA', 'HLSC', 'HLTH',\
                'HONR', 'INAG', 'INFM', 'INST', 'ISRL', 'ITAL', 'IVSP', 'JAPN',\
                'JOUR', 'JWST', 'KNES', 'KORA', 'LARC', 'LASC', 'LATN', 'LBSC',\
                'LGBT', 'LING', 'MAIT', 'MATH', 'MEES', 'MIEH', 'MOCB', 'MUED',\
                'MUSC', 'MUSP', 'NACS', 'NFSC', 'NIAP', 'NIAS', 'PERS', 'PHIL',\
                'PHYS', 'PLSC', 'PORT', 'PSYC', 'PUAF', 'RDEV', 'RELS', 'RUSS',\
                'SLAA', 'SLAV', 'SLLC', 'SOCY', 'SPAN', 'SPHL', 'STAT', 'SURV',\
                'TDPS', 'THET', 'TOXI', 'UMEI', 'UNIV', 'URSP', 'USLT', 'VMSC',\
                'WMST']
    
    courselist = get_course_list()

    base_url = 'https://ntst.umd.edu/soc/'
    term_url =  '''{term}/{dept}/{course}'''
    start_urls = [base_url+term_url.format(term="201408", dept=course[:4],\
                  course=course) for course in courselist]

    #start_urls = ['https://ntst.umd.edu/soc/201408/PUAF/PUAF610', 'https://ntst.umd.edu/soc/201408/PUAF/PUAF650']

    #rules = [Rule(SgmlLinkExtractor(allow=['/tor/\d+']), 'parse_torrent')]

    def parse(self, response):
        x = HtmlXPathSelector(response)
        
        rows = x.select('//div[@class="course-prefix row"]') #use this selector for main page that list top level dept
        row_list = []

        sites = x.select('//div[@class="course"]') # use this for dept page e.g. PUAF
        items = []
        
        sections = x.select('//div[@class="section"]')

        # Department information
        '''
        for row in rows:
            deptlist = DeptItem()
            name = row.select('descendant::span/text()').extract()
            deptlist['dept_short'] = name[0]
            deptlist['dept_long'] = name[1]
            row_list.append(deptlist)
        '''
        # Course information 
        # course_container = '<div id="PUAF689Y" class="course">'
        #this section uses relative descendants based on the course container
        '''
        for site in sites:
            torrent = CourseItem() 
            torrent['course_name'] = site.select('descendant::div[@class="course-id"]/text()').extract()
            torrent['course_title'] = site.select('descendant::span[@class="course-title"]/text()').extract()
            torrent['course_credit'] = site.select('descendant::span[@class="course-min-credits"]/text()').extract()
    #       torrent['course_gradetype'] = site.select('descendant::abbr[@title="Regular, Pass-Fail"]/span/text()').extract()
            torrent['course_text'] = site.select('descendant::div[@class="approved-course-text"]/text()').extract()            
        '''   

        item_section = list()
        for section in sections:
        #torrent['course_gradetype'] = x.select('//span[@class="grading-method"]').extract()
        #'a[@class="toggle-sections-link"]
        #function(a){return typeof p!="undefined"&&(!a||p.event.triggered!==a.type)?p.event.dispatch.apply(h.elem,arguments):b}
        
        #Quick and dirty grab all text from courses and then remove items with tabs
        #site = hxs.select('//div[@class="course"]')
        #alltext = site.select('descendant::text()').extract()
        #cleaner = [x for x in alltext if "\t" not in x]

            # Section Information
            sectionlist = SectionItem()
            sectionlist['semester'] = "1408"
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


