from urllib.parse import urljoin

#Build a Web Scraper
#1.Use the API
#2.HTML WEB Scraping usin some tool like bs4
#And import 1.pip install requests
#pip install bs4
#pip install html5lip

import requests
from bs4 import BeautifulSoup

url = "https://www.amazon.in/?&tag=googhydrabk1-21&ref=pd_sl_7hz2t19t5c_e&adgrpid=155259815513&hvpone=&hvptwo=&hvadid=678802104188&hvpos=&hvnetw=g&hvrand=7310610524548693580&hvqmt=e&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=1007788&hvtargid=kwd-10573980&hydadcr=14453_2371562&gad_source=1"

# 1 = Get the HTML
r = requests.get(url)
htmlContent = r.content
# print(htmlContent)

# 2 = Parse the HTML
soup = BeautifulSoup(htmlContent, 'html.parser')
# print(soup.prettify)

# 3 = HTML Tree traversal (TITLE)
title = soup.title
print(type(title))

#Commonly used type of Object:
print(type(title)) # 1. Tag
print(type(title.string)) # 2.Navigablestring
print(type(soup))# 3.BeatifulSoup
markup = "<p><!-- this is a comment --></p>"# 4.Comment
soup2 = BeautifulSoup(markup)
print(type(soup2.p.string))


#Get the title of HTML page
title = soup.title

#Get all the paragraphs from the page
paras = soup.find_all('p')
print(paras)

#Get first element in the HTML page
print(soup.find('p'))

# #Get Classes of any element in the HTML page
# print(soup.find('p')['class'])

#find all the elements with class lead
print(soup.find_all("p",class_="lead"))

#Get the text form the tags/soup
print(soup.get_text())

#Get all anchor tages from the page
anchors = soup.find_all('a')
all_links = set()

    

all_links = set()  # Initialize an empty set to store unique links

# Get all the links on the page
for link in anchors:
    href = link.get('href')
    if href and href != '#':
        # Construct the full URL by appending the base URL to the relative link
        full_link = urljoin("https://www.amazon.in/?&tag=googhydrabk1-21&ref=pd_sl_7hz2t19t5c_e&adgrpid=155259815513&hvpone=&hvptwo=&hvadid=678802104188&hvpos=&hvnetw=g&hvrand=7310610524548693580&hvqmt=e&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=1007788&hvtargid=kwd-10573980&hydadcr=14453_2371562&gad_source=1",href)
        all_links.add(full_link)
        print(full_link)







