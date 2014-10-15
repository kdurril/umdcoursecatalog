#!/usr/bin/env
#Use for extracting course number, title, credit, and descriptions
#Use testudo_crawler_sections to extract section data
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from mytestudo.items import DeptItem, CourseItem, SectionItem

class TestudoSpider(BaseSpider):

    name = 'testudo_courses'
    allowed_domains = ['ntst.umd.edu']
    term = "201501"

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
     
    base_url = 'https://ntst.umd.edu/soc/'
    term_url =  '''{term}/{dept}'''.format(term=term, dept="PUAF")
    start_urls = [base_url+'''{term}/{dept}'''.format(term=term, dept=str(x)) for x in abbrlist]

    def parse(self, response):
        x = HtmlXPathSelector(response)
        
        rows = x.select('//div[@class="course-prefix row"]') #use this selector for main page that list top level dept
        row_list = []

        sites = x.select('//div[@class="course"]') # use this for dept page e.g. PUAF
        items = []

        # Course information 
        # course_container = '<div id="PUAF689Y" class="course">'
        #this section uses relative descendants based on the course container
        
        for site in sites:
            torrent = CourseItem() 
            torrent['semester'] = self.term
            torrent['course_name'] = site.select('descendant::div[@class="course-id"]/text()').extract()
            torrent['course_title'] = site.select('descendant::span[@class="course-title"]/text()').extract()
            torrent['course_credit'] = site.select('descendant::span[@class="course-min-credits"]/text()').extract()
    #       torrent['course_gradetype'] = site.select('descendant::abbr[@title="Regular, Pass-Fail"]/span/text()').extract()
            torrent['course_text'] = site.select('descendant::div[@class="approved-course-text"]/text()').extract()            
            items.append(torrent)

        return items


