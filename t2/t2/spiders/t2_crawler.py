#!/usr/bin/env
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector

from t2.items import T2Item

class TestudoSpider(BaseSpider):

    name = 't2'
    allowed_domains = ['ntst.umd.edu']
    start_urls = ['''https://ntst.umd.edu/soc/''']


    def parse(self, response):
        x = HtmlXPathSelector(response)
        sites = x.select('//div[@"left-course-prefix-column"]')
        items = list()

        #Department information
        for site in sites:
        #torrent['dept_link'] = site.select('//a[@href=""]').extract()
        #torrent['dept_short'] = site.select('//span[@class="prefix-abbrev push_one two columns"]/text()').extract()
        #torrent['dept_long'] = site.select('//span[@class=""]/text()').extract()
            item = T2Item()
            dept_link = site.select('//a[@class="clearfix"]').extract()
            dept_short = site.select('//a[@class="clearfix"]//span[@class="prefix-abbrev push_one two columns"]/text()').extract()
            dept_long = site.select('//a[@class="clearfix"]//span[@class="prefix-name nine columns"]/text()').extract()
            
            #item['dept_link'] = site.select('//a[@class="clearfix"]').extract()
            item['dept_short'] = site.select('span[@class="prefix-abbrev push_one two columns"]/text()').extract()
            item['dept_long'] = site.select('span[@class="prefix-name nine columns"]/text()').extract()
            items.append(item)
            print dept_link, dept_short, dept_long
        return items

