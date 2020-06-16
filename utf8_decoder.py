"""
This file conatains only one function with Decode the Hebrew UTF-8  from the hebrew sitmap 
to a URL with can be open by Python.

The function get a UTF8 URL  and return  an encoded URL that can be open by the browser
"""

import webbrowser



def Decode_UTF8_URL(Web_Heb_Url):


    base_Url = "http://www.ask-tal.co.il/"


    #Remove <loc> from the string
    Web_Heb_Url = Web_Heb_Url.replace("<loc>", "")


    #Remove </loc> from the string
    Web_Heb_Url = Web_Heb_Url.replace("</loc>", "")


    #Remove all spaces from a the string
    Web_Heb_Url = Web_Heb_Url.replace(" ", "")


    #Cutting the Base Url to get only the Hebrew Part
    tempHebUrl = Web_Heb_Url.replace('http://www.ask-tal.co.il/','')


    #print("This is the Hebrew format from the url that should be convert: \n\n" + tempHebUrl)


    #encode the Hebrew to Itf-8
    utf8_Url = tempHebUrl.encode()
    #print("The Hebrew after incoding to UTF-8 : \n\n" + str(utf8_Url))


    #Convert bytes to String
    Utf8_end_url = str(utf8_Url)


    #Replaceing \ with %
    new_Url_Utf8 = Utf8_end_url.replace('\\','%')
    #print("\n\n Replaceing \\ with % : \n\n" + new_Url_Utf8)


    #remove first 2 tabs b'   and '
    new_Url_Utf8 = new_Url_Utf8.replace("b'",'')


    #remove the '  at the end of the string
    new_Url_Utf8 = new_Url_Utf8.replace("'",'')

    #remove the 'x' char
    new_Url_Utf8 = new_Url_Utf8.replace("x",'')

    #capitalize the string
    new_Url_Utf8 = new_Url_Utf8.upper() 

    #now i need to join the unicode url to base website url it to a link
    final_Link =  base_Url + str(new_Url_Utf8)
    return final_Link

"""
example_url = "<loc>http://www.ask-tal.co.il/קניית-דירה-התהליך-המשפטי</loc>"

trimmed_url = Decode_UTF8_URL(example_url)

print(trimmed_url)

webbrowser.open(trimmed_url, new=2)
"""

