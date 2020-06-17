
import urllib.parse
import webbrowser


def Extract_Hebrew_Url(Web_Heb_Url):

    base_Url = "http://www.ask-tal.co.il/"



    #Remove <loc> from the string
    Web_Heb_Url = Web_Heb_Url.replace("<loc>", "")


    #Remove </loc> from the string
    Web_Heb_Url = Web_Heb_Url.replace("</loc>", "")


    #Remove all spaces from a the string
    Web_Heb_Url = Web_Heb_Url.replace(" ", "")

    #Cutting the Base Url to get only the Hebrew Part
    tempHebUrl = Web_Heb_Url.replace(base_Url,'')

    #Remove the unexplainable %B
    trim_url = tempHebUrl[:-2]

    #Change the Url back to Hebrew
    heb_url = urllib.parse.unquote(trim_url)

    #oin the unicode url to base website url it to a link
    final_Link =  base_Url + str(heb_url)



    #print(final_Link)

    #webbrowser.open(sample_url, new=2)


    return final_Link


""" Internal Testing
sample_url = "http://www.ask-tal.co.il/%D7%9E%D7%A1-%D7%A8%D7%9B%D7%99%D7%A9%D7%94%N"
Extract_Hebrew_Url(sample_url)
"""