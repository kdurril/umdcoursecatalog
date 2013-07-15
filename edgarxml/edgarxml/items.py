# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class EdgarxmlItem(Item):
    # define the fields for your item here like:
    # name = Field()
        # define the fields for your item here like:
    
    title = Field()
    link = Field()
    summary = Field()
    updated = Field()
    category = Field()
    sec_id = Field()

sample_text = '''
    <title>D - 815 Associates, LLC</title>
      <link rel="alternate" type="text/html" href="/Archives/edgar/data/1568379/000156837913000001/0001568379-13-000001-index.htm"/>
      <summary type="html">&lt;b&gt;Filed Date:&lt;/b&gt; 02/08/2013 &lt;b&gt;Accession Number:&lt;/b&gt; 0001568379-13-000001 &lt;b&gt;Size:&lt;/b&gt; 6 KB</summary>
      <updated>02/08/2013</updated>
      <category scheme="http://www.sec.gov/" label="form type" term="4"/>
      <id>urn:tag:sec.gov,2008:accession-number=0001568379-13-000001</id>
'''
