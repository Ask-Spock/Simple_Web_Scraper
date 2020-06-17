"""
What the builder should do :

0.Create a website folder.

1. Get a ready to parse url.
1.1 Create the file name 

2.Using beautiful soap open the html page.

3.Extrat the following Data:

3.1 The page Title.

3.2 The page Contet.

3.3 The page Images.

4.Create am Html Static File with a name of the URL in Hebrew.

5.Enter all the Data to the Html file.

6.Close the file.


###Testing###

webbrowser.open(sampleUrl, new=2)


"""




import webbrowser
import os
import sys
import shutil


sampleUrl = "http://www.ask-tal.co.il/%D7%94%D7%90%D7%9D-%D7%94%D7%A4%D7%A7%D7%A2%D7%94-%D7%A0%D7%97%D7%A9%D7%91%D7%AA-%D7%90%D7%99%D7%A8%D7%95%D7%A2-%D7%9E%D7%A1"

#Directory Name
dirName = 'Ask-Tal'


#Create a folder for the website files
def createFolder():
    try:
        # Create target Directory
        os.mkdir(dirName)
        print("Directory " , dirName ,  " Created ")
    except FileExistsError:
        print("Directory " , dirName ,  " already exists")


#Delete a folder for the website files
def deleteFolder():
    # Try to remove tree; if failed show an error using try...except on screen
    try:
        shutil.rmtree(dirName)
    except OSError as e:
        print ("Error: %s - %s." % (e.filename, e.strerror))






def main():

    #The script need a new working folder every time its run so i delete the previes
    #and create a new one.
    deleteFolder()
    createFolder()

    #Create  file name from the URL
    print(sampleUrl.encode())


if __name__ == '__main__':
    main()