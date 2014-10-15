This scrapes the course catalog of the University of Maryland at College Park.
The University has no API for its catalog, so this tool gathers the 
information. The information is useful for aggregate analysis of courses,
departments, and the University.

The tool is structured for output as CSV files with semester and course number
as a composite primary key for sections for an RDBMS.  

This scrapes https://ntst.umd.edu/soc/. This site lists catalogs beginning in 
Spring 2013. For semesters prior to spring 2013, see
https://www.sis.umd.edu/bin/seats?term=201208. This crawler does not cover
the older material.

Using the tool
See http://doc.scrapy.org/en/latest/index.html for official documentation of 
Scrapy.

Set the term prior to using this tool in each spider file. The format for a
term is YearSemester such as 201408 for fall 2014. The semester numbers are 
as follows:
fall = 08
spring = 01
winter = 12 - note that winter term for January 2015 courses is 201412
summerI = 05
summerII = 07

Adjust the spiders to adjust crawling behavior
Adjust items.py to add items to pipeline. 

It has 3 spiders:
testudo_crawler_dept
testudo_crawler_courses
testudo_crawler_section

Output files should be:
departments.csv
courses.csv
sections.csv

From command line:
scrapy crawl testudo_dept -o departments.csv -t csv
scrapy crawl testudo_courses -o courses.csv -t csv
scrapy crawl testudo_sections -o sections.csv -t csv

Know issues:
Undergraduate honors courses are added to the base course records.
Courses that end with letter "h" are honors courses. The final 0101 section of
a standard course with an honors section is usually the honors course. 

