from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from allConsts import header
from scrapingbee import ScrapingBeeClient
import csv

def gettingCarLinks():
    # Preparing the URL.
    offSetValue = 50
    links = []
    #Connecting Proxy Service
    client = ScrapingBeeClient(
        api_key='W9LUFY03GBFL3G4IYH1C5NF9PC8LBBG1QJECP350H7EZPKNU208915VPIVQ4HMBAMB3AMCNMQ3RG0IK7')
    #Getting 5000 car links.
    while offSetValue <= 200:
        #Preparing the URL. Setting offSet inside the function. Each iteration adds '50' to offSetValue.
        MAIN_URL = "https://www.sahibinden.com/bmw?pagingOffset="+str(offSetValue)+"&pagingSize=50"

        # Sending Request to the main car brand page.
        response = client.get(
            MAIN_URL,
            params={"premium_proxy": True,
                    "country_code": "tr",
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
        advertLinks.append("https://www.sahibinden.com/"+link)

#Removing duplicated elements if there are.
actualCarURLs = list(dict.fromkeys(advertLinks))
print("Len of car urls (removed duplicated elements): " + str(len(actualCarURLs)))
print(actualCarURLs)

