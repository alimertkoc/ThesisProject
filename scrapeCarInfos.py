from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import requests
from allConsts import header, header1
from scrapingbee import ScrapingBeeClient
#W9LUFY03GBFL3G4IYH1C5NF9PC8LBBG1QJECP350H7EZPKNU208915VPIVQ4HMBAMB3AMCNMQ3RG0IK7
def getCarDetails(URL):
    client = ScrapingBeeClient(
        api_key='W9LUFY03GBFL3G4IYH1C5NF9PC8LBBG1QJECP350H7EZPKNU208915VPIVQ4HMBAMB3AMCNMQ3RG0IK7')
    response = client.get(URL, headers=header)

    send_request()
    # page = requests.get(URL, headers=header1)
    # soup = BeautifulSoup(page.content, 'html.parser')
    # print(soup)


getCarDetails("https://www.sahibinden.com/ilan/vasita-otomobil-bmw-2015-model-bmw-520i-premium-hayalet-m-direksiyon-harmon-cardon-1001212247/detay")





