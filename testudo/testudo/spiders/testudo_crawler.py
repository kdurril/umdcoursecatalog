#!/usr/bin/env
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector

class TestudoSpider(CrawlSpider):

    name = 'testudo'
    allowed_domains = ['ntst.umd.edu']
    start_urls = ['https://ntst.umd.edu/soc/courses.html']
    #rules = [Rule(SgmlLinkExtractor(allow=['/tor/\d+']), 'parse_torrent')]

    def parse_torrent(self, response):
        x = HtmlXPathSelector(response)

        torrent = TorrentItem()
        torrent['url'] = response.url
        course_container = '<div id="PUAF689Y" class="course">'
        torrent['course_name'] = x.select('//span[@class="course-id"]').extract()
        torrent['course_title'] = x.select('//span[@class="course-title"]').extract()
        torrent['course_credit'] = x.select('//span[@class="course-min-credits"]').extract()
        torrent['course_gradetype'] = x.select('//abbr[@title="Regular, Pass-Fail"]').extract()
        torrent['course_text'] = x.select('//span[@class="approved-course-texts-container"]')
        #torrent['course_gradetype'] = x.select('//span[@class="grading-method"]').extract()
        return torrent
