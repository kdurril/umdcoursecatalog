from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from edgar.items import EdgarItem


class EdgarSpider(BaseSpider):
    name = "edgar"
    allowed_domains = ["www.sec.gov"]
    start_urls = [
        '''http://www.sec.gov/cgi-bin/srch-edgar?text=form-type%3Dd+and+state%3DMN&first=2013&last=2013'''
        ]

    
    
    def parse(self, response):
        item = EdgarItem()
        x = HtmlXPathSelector(response)
        items = list()
        sites = x.select('''//table[5]''')

        for site in sites:
            item = EdgarItem() 
            item['no'] = site.select('tr/td[0]/text()').extract()
            item['company'] = site.select('tr/td[1]/text()').extract()
            item['sec_format'] = site.select('tr/td[2]/a').extract()
            item['form_type'] = site.select('tr/td[3]/text()').extract()
            item['filing_date'] = site.select('tr/td[4]/text()').extract()
            item['size'] = site.select('tr/td[5]/text()').extract()
            items.append(item)

        return items

#http://www.sec.gov/Archives/edgar/data/1568379/000156837913000001/0001568379-13-000001-index.htm
#http://www.sec.gov/Archives/edgar/data/1568379/000156837913000001/primary_doc.xml


