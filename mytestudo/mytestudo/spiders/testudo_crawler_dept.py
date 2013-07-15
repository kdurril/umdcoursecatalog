#!/usr/bin/env
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from mytestudo.items import DeptItem

class TestudoSpider(BaseSpider):

    name = 'testudo_dept'
    allowed_domains = ['ntst.umd.edu']
    start_urls = ['''https://ntst.umd.edu/soc/''']
    #rules = [Rule(SgmlLinkExtractor(allow=['/tor/\d+']), 'parse_torrent')]

    def parse(self, response):
        x = HtmlXPathSelector(response)
        
        rows = x.select('//div[@class="course-prefix row"]') #use this selector for main page that list top level dept
        row_list = []
        
        # Department information
        for row in rows:
            deptlist = DeptItem()
            name = row.select('descendant::span/text()').extract()
            deptlist['dept_short'] = name[0]
            deptlist['dept_long'] = name[1]
            row_list.append(deptlist)

        return row_list


