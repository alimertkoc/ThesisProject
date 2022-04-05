from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from allConsts import header
from scrapingbee import ScrapingBeeClient
import numpy as np
import pandas as pd
import csv

def gettingCarLinks():
    # Preparing the URL.
    offSetValue = 50
    links = []
    #Connecting Proxy Service
    client = ScrapingBeeClient(
        api_key='AEM0KAHPRSGVJK68YKMP6I8THC8LWFKWKI1EWSPUJXDJO7S2R2KZMHM5N43N6S0Z8D6I2JIPIBAMUOOU')
    #Getting 5000 car links.
    while offSetValue <= 4000:
        #Preparing the URL. Setting offSet inside the function. Each iteration adds '50' to offSetValue.
        MAIN_URL = "https://www.sahibinden.com/bmw-3-serisi?pagingOffset="+str(offSetValue)+"&pagingSize=50"

        # Sending Request to the main car brand page.
        response = client.get(
            MAIN_URL,
            params={"premium_proxy": True,
                    "country_code": "tr",
                    "render_js": False
                    }
        )

        #Parsing the response context.
        soup = BeautifulSoup(response.text, "html.parser")

        #Getting all url elements at the page.
        for link in soup.findAll('a'):
            links.append(link.get('href'))

        #There may some NoneType objects, so we need to filter them to next process.
        links = [i for i in links if i is not None]

        print("Current offSetValue: " + str(offSetValue))
        print("Requested URL: " + MAIN_URL)
        offSetValue += 50
    return links

#Returning car URLs to a variable.
carURLs = gettingCarLinks()

#Getting car adverts links by filtering them with starting with '/ilan' or not.
advertLinks = []
for link in carURLs:
    if link.startswith("/ilan"):
        advertLinks.append("https://www.sahibinden.com"+link+"\n")


#Removing duplicated elements if there are.
actualCarURLs = list(dict.fromkeys(advertLinks))
print("Len of car urls (removed duplicated elements): " + str(len(actualCarURLs)))
print(actualCarURLs)


file1 = open('bmw3.txt', 'w')
file1.writelines(actualCarURLs)

df = pd.DataFrame(actualCarURLs)
df.to_csv('bmw3.csv')