from bs4 import BeautifulSoup
import requests

sample_url = "http://www.ask-tal.co.il/%D7%A7%D7%A0%D7%99%D7%99%D7%AA-%D7%93%D7%99%D7%A8%D7%94"


page = requests.get(sample_url)


#print(page.text)

soup = BeautifulSoup(page.text, 'html.parser')

print(soup.prettify())
print("------------------------\n")
print(soup.title)
print(soup.h1)
print(soup.keywords)
