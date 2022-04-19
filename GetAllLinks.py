"""
This code provides us to scraping advert links from source website.
Each request returns 50 of links.
Loop iterates 50 by 50 inside 'offset_value'.
The range of while loop decides how many links that you want to scrape.
Scraped advert links have written to a .csv file for the upcoming processes.
The upcoming process is in 'ScrapeCarInfos.py'.
"""

from bs4 import BeautifulSoup
from scrapingbee import ScrapingBeeClient
import pandas as pd


def getting_car_links():

    # Preparing the URL.
    offset_value = 50
    links = []

    # Connecting Proxy Service
    client = ScrapingBeeClient(
        api_key='11E8XBLZ5HWYE713R9ZXH7ILW11A7O13ZT4IHKV3XHGZDVOQW90JIRS7CU9TYMHU74XN9QDNLHV3GB8E')

    # Getting 5000 car links.
    while offset_value <= 4000:

        # Preparing the URL. Setting offSet inside the function. Each iteration adds '50' to offset_value.
        main_url = "https://www.sahibinden.com/bmw-3-serisi?pagingOffset="+str(offset_value)+"&pagingSize=50"

        # Sending Request to the main car brand page.
        response = client.get(
            main_url,
            params={"premium_proxy": True,
                    "country_code": "tr",
                    "render_js": False
                    }
        )

        # Parsing the response context.
        soup = BeautifulSoup(response.text, "html.parser")

        # Getting all url elements at the page.
        for link in soup.findAll('a'):
            links.append(link.get('href'))

        # There may some NoneType objects, so we need to filter them to next process.
        links = [i for i in links if i is not None]

        print("Current offset_value: " + str(offset_value))
        print("Requested URL: " + main_url)
        offset_value += 50
    return links


# Returning car URLs to a variable.
carURLs = getting_car_links()

# Getting car advert links by filtering them with starting with '/ilan' or not.
advertLinks = []
for link in carURLs:
    if link.startswith("/ilan"):
        advertLinks.append("https://www.sahibinden.com"+link+"\n")


# Removing duplicated elements if there are.
actualCarURLs = list(dict.fromkeys(advertLinks))

# Writing into a .csv file
df = pd.DataFrame(actualCarURLs)
df.to_csv('CarURLs.csv')