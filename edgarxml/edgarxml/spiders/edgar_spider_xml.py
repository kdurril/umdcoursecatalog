from scrapy.spider import BaseSpider
from scrapy.selector import XmlXPathSelector
from edgar_xml.items import EdgarxmlItem


class EdgarXMLSpider(BaseSpider):
    name = "edgar_xml"
    allowed_domains = ["www.sec.gov"]
    start_urls = [
        '''http://www.sec.gov/Archives/edgar/data/1568379/000156837913000001/primary_doc.xml'''
        ]


    items = list()
    
    def parse(self, response):
        items = EdgarxmlItem()
        x = XmlXPathSelector(response)
        sites = x.selector('').extract()

        for site in sites:
            item = EdgarItem() 
            item['title'] = site.selector('tr').extract()
            item['link'] = site.selector('tr').extract()
            item['summary'] = site.selector('tr').extract()
            item['updated'] = site.selector('tr').extract()
            item['category'] = site.selector('tr').extract()
            item['sec_id'] = site.selector('tr').extract()
            items.append(item)

        return items

#http://www.sec.gov/Archives/edgar/data/1568379/000156837913000001/0001568379-13-000001-index.htm
#http://www.sec.gov/Archives/edgar/data/1568379/000156837913000001/primary_doc.xml


