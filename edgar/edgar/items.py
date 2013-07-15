# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class EdgarItem(Item):
    # define the fields for your item here like:
    #No Compamny Format Form Type Filing Date Size
    no = Field()
    company = Field()
    sec_format = Field()
    form_type = Field()
    filing_date = Field()
    size = Field()

sample_text = '''
    <title>D - 815 Associates, LLC</title>
      <link rel="alternate" type="text/html" href="/Archives/edgar/data/1568379/000156837913000001/0001568379-13-000001-index.htm"/>
      <summary type="html">&lt;b&gt;Filed Date:&lt;/b&gt; 02/08/2013 &lt;b&gt;Accession Number:&lt;/b&gt; 0001568379-13-000001 &lt;b&gt;Size:&lt;/b&gt; 6 KB</summary>
      <updated>02/08/2013</updated>
      <category scheme="http://www.sec.gov/" label="form type" term="4"/>
      <id>urn:tag:sec.gov,2008:accession-number=0001568379-13-000001</id>
'''
