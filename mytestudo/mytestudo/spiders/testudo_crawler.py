#!/usr/bin/env
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from mytestudo.items import DeptItem, CourseItem, SectionItem

class TestudoSpider(BaseSpider):

    name = 'testudo'
    allowed_domains = ['ntst.umd.edu']

    abbrlist = ['AASP', 'AAST', 'AGNR', 'AMSC', 'AMST', 'ANSC', 'ANTH', 'AOSC', 'ARAB', 'ARCH', 'AREC', 'ARHU', 'ARMY', 'ARSC', 'ARTH', 'ARTT', 'ASTR', 'BCHM', 'BEES', 'BIOE', 'BIOL', 'BIOM', 'BIPH', 'BISI', 'BMGT', 'BSCI', 'BSCV', 'BSGC', 'BSOS', 'BSST', 'BUAC', 'BUDT', 'BUFN', 'BULM', 'BUMK', 'BUMO', 'BUSI', 'CBMG', 'CCJS', 'CHBE', 'CHEM', 'CHIN', 'CHPH', 'CLAS', 'CLFS', 'CMLT', 'CMSC', 'COMM', 'CONS', 'CPSP', 'DANC', 'EALL', 'ECON', 'EDCI', 'EDCP', 'EDHD', 'EDHI', 'EDMS', 'EDPS', 'EDSP', 'EDUC', 'EMBA', 'ENAE', 'ENBE', 'ENCE', 'ENCH', 'ENCO', 'ENEE', 'ENES', 'ENFP', 'ENGL', 'ENMA', 'ENME', 'ENNU', 'ENPM', 'ENPP', 'ENRE', 'ENSE', 'ENSP', 'ENST', 'ENTM', 'ENTS', 'EPIB', 'FILM', 'FMSC', 'FOLA', 'FREN', 'GEMS', 'GEOG', 'GEOL', 'GERM', 'GREK', 'GVPT', 'HACS', 'HDCC', 'HEBR', 'HEIP', 'HESP', 'HHUM', 'HISP', 'HIST', 'HLSA', 'HLSC', 'HLTH', 'HONR', 'INAG', 'INFM', 'INST', 'ISRL', 'ITAL', 'IVSP', 'JAPN', 'JOUR', 'JWST', 'KNES', 'KORA', 'LARC', 'LASC', 'LATN', 'LBSC', 'LGBT', 'LING', 'MAIT', 'MATH', 'MEES', 'MIEH', 'MOCB', 'MUED', 'MUSC', 'MUSP', 'NACS', 'NFSC', 'NIAP', 'NIAS', 'PERS', 'PHIL', 'PHYS', 'PLSC', 'PORT', 'PSYC', 'PUAF', 'RDEV', 'RELS', 'RUSS', 'SLAA', 'SLAV', 'SLLC', 'SOCY', 'SPAN', 'SPHL', 'STAT', 'SURV', 'TDPS', 'THET', 'TOXI', 'UMEI', 'UNIV', 'URSP', 'USLT', 'VMSC', 'WMST']
     


    start_urls = ['''https://ntst.umd.edu/soc/''', '''https://ntst.umd.edu/soc/courses.html?term=201308&prefix=PUAF''']
    base_url = 'https://ntst.umd.edu/soc/'
    term_url =  '''courses.html?term={term}&prefix={dept}'''.format(term="201308", dept="PUAF")
    
    #start_urls = [base_url+'''courses.html?term={term}&prefix={dept}'''.format(term="201308", dept=str(x)) for x in abbrlist]


    #rules = [Rule(SgmlLinkExtractor(allow=['/tor/\d+']), 'parse_torrent')]

    def parse(self, response):
        x = HtmlXPathSelector(response)
        
        rows = x.select('//div[@class="course-prefix row"]') #use this selector for main page that list top level dept
        row_list = []

        sites = x.select('//div[@class="course"]') # use this for dept page e.g. PUAF
        items = []
        

        # Department information
        for row in rows:
            deptlist = DeptItem()
            name = row.select('descendant::span/text()').extract()
            deptlist['dept_short'] = name[0]
            deptlist['dept_long'] = name[1]
            row_list.append(deptlist)

        # Course information 
        # course_container = '<div id="PUAF689Y" class="course">'
        #this section uses relative descendants based on the course container
        
        for site in sites:
            torrent = CourseItem() 
            torrent['course_name'] = site.select('descendant::div[@class="course-id"]/text()').extract()
            torrent['course_title'] = site.select('descendant::span[@class="course-title"]/text()').extract()
            torrent['course_credit'] = site.select('descendant::span[@class="course-min-credits"]/text()').extract()
    #       torrent['course_gradetype'] = site.select('descendant::abbr[@title="Regular, Pass-Fail"]/span/text()').extract()
            torrent['course_text'] = site.select('descendant::div[@class="approved-course-text"]/text()').extract()            
            items.append(torrent)



        #torrent['course_gradetype'] = x.select('//span[@class="grading-method"]').extract()
        #'a[@class="toggle-sections-link"]
        #function(a){return typeof p!="undefined"&&(!a||p.event.triggered!==a.type)?p.event.dispatch.apply(h.elem,arguments):b}
        
        #Quick and dirty grab all text from courses and then remove items with tabs
        #site = hxs.select('//div[@class="course"]')
        #alltext = site.select('descendant::text()').extract()
        #cleaner = [x for x in alltext if "\t" not in x]

        # Section Information
        # sectionlist = SectionItem()
        #sectionlist['section_num'] = x.select('''//span[@class='section-id']/text()''').extract()
        #torrent['section_instructor'] = x.select('''//span[@class='section-instructor']/text()''').extract()
        #torrent['section_seats'] = x.select('''//span[@class='total-seats']/text()''').extract()
        #torrent['section_remain'] = x.select('''//span[@class='open-seats']/text()''').extract()
        #torrent['section_waitlist'] = x.select('''//span[@class='waitlist']/text()''').extract()
        #torrent['section_day'] = x.select('''//span[@class='section-days']/text()''').extract()
        #torrent['section_time_start'] = x.select('''//span[@class='class-start-time']/text()''').extract()
        #torrent['section_time_end'] = x.select('''//span[@class='class-end-time']/text()''').extract()
        #torrent['section_building'] = x.select('''//span[@class='building-code']/text()''').extract()
        #torrent['section_class_type'] = x.select('''//span[@class='clas-type']/text()''').extract()
        yield row_list, items


