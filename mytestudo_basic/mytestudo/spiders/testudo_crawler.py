#!/usr/bin/env
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector

class TestudoSpider(BaseSpider):

    name = 'testudo'
    allowed_domains = ['ntst.umd.edu']
    start_urls = ['https://ntst.umd.edu/soc']
    #rules = [Rule(SgmlLinkExtractor(allow=['/tor/\d+']), 'parse_torrent')]

    def parse_torrent(self, response):
        x = HtmlXPathSelector(response)

        torrent = TorrentItem()
        #torrent['dept_link'] = x.select('//a[@href=""]').extract()
        torrent['dept_abbr'] = x.select('//span[@class="prefix-abbrev push_one two columns"]').extract()
        torrent['dept_long'] = x.select('//span[@class="prefix-name nine columns"]').extract()
