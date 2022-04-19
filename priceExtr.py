from bs4 import BeautifulSoup
import csv
import re
from urllib.request import Request, urlopen
import requests
from allConsts import header, header1
from scrapingbee import ScrapingBeeClient

def getCarDetails(client, MAIN_URL):
    response = client.get(
        MAIN_URL,
        params={"premium_proxy": True,
                "country_code": "tr",
                "render_js": False
                }
    )
    #print("Status Code")
    #print(response.status_code)
    soup = BeautifulSoup(response.text, "html.parser")

    carpricelist = soup.findAll('h3')[4].get_text().strip()
    for i in range(len(carpricelist)):
        if(carpricelist[i] == 'T'):
            break
    carpricelist = carpricelist[:i-1]

    print("x"+carpricelist+"x")

    #car_price = soup.findAll('h3')[3].get_text().strip()




    return carpricelist



#Need to add url counter to prevent api limits.
#Start reading from a specific line number.
#Need to change API_KEY at each new 100 requests
#ScrapingBee is giving 1000 credit and each request spends 10 credit
#BMW3 - 956 cars
#BMW5 - 950 cars
#Total credit needed: 20000 credits = 20 accounts


def readAdvertURL(filename):
    client = ScrapingBeeClient(
        api_key='7T7Z1MK5DGTVE0QYKDA99Z34CM8SI8HS9XQN05MB9YG7GZ8X962E1O6CDGBR3G211V6RQXEK6UNKVKG3')
    getCarDetails(client, "https://www.sahibinden.com/ilan/vasita-otomobil-bmw-3.30ci-coupe-manuel-1016871205/detay")


readAdvertURL('bmw3-1.csv')
