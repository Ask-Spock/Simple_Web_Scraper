"""
---------------------------------------------

Work-Summery

1.get website maplink

2.run on the links and activating a function that will build an HTML file from each  one.

---------------------------------------------
"""
from bs4 import BeautifulSoup
import os
import urllib
import utf8_decoder as decoder
import webbrowser
import get_heb_url as heb_extractor
import page_builder as builder





"""
open the XML map of a website and  get the releven lines and encode the to handle url and
enter the url to a Data structuer

"""


#Open SiteMap URL File
url = "http://www.ask-tal.co.il/map.asp"
file = urllib.request.urlopen(url)



#Run on sitemap and isolate all the the Links
for line in file:
    decoded_line = line.decode("utf-8")
    if decoded_line.find('loc') != -1:
        #Call the decoder function and ready the links
        browser_url = decoder.Decode_UTF8_URL(decoded_line)
        heb_url = heb_extractor.Extract_Hebrew_Url(browser_url)


        #Page_builder_funcrtion(heb_url,browser_url)
        builder.Page_Builder(heb_url)




        #print(browser_url)
        #print(heb_url)
        #webbrowser.open(trim_url, new=2)

        ###***Calling the Page Builder Function OR Enter the both URLs to a Data Structer***###

###***Decode_UTF8_URL function - There is a Bug with the calularioe URL
### that turn to capitlize / check if its occur in other URLS***


#After the url are in a data structer, script should run on links and build a HTML file with the content
#that is  needed for Google Hugo


