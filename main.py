"""
---------------------------------------------

Work-Summery

1.get website maplink

2.decode the links and enter them to a data structuer

3.run on the data structuer and build an HTML file from each unit of the Data strucuer

---------------------------------------------
"""
from bs4 import BeautifulSoup
import os
import urllib
import utf8_decoder as decoder
import webbrowser




"""
open the XML map of a website and  get the releven lines and encode the to handle url and
enter the url to a Data structuer

"""


#Open SiteMap URL File
url = "http://www.ask-tal.co.il/map.asp"
file = urllib.request.urlopen(url)




#Run on file and isolate all the the Links
for line in file:
    decoded_line = line.decode("utf-8")
    if decoded_line.find('loc') != -1:
        #Call the decoder function and ready the links
        url = decoder.Decode_UTF8_URL(decoded_line)
        trim_url = url[:-2]
        print(trim_url)
        #webbrowser.open(trim_url, new=2)
        ###Enter the Trim URL to a Data Structer###




#After the url are in a data structer, script should run on links and build a HTML file with the content
#I need for Google Hugo
