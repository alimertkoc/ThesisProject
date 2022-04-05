from bs4 import BeautifulSoup
import csv
import re
from urllib.request import Request, urlopen
import requests
from allConsts import header, header1
from scrapingbee import ScrapingBeeClient
import pandas as pd

def getCarDetails(client, MAIN_URL):
    response = client.get(
        MAIN_URL,
        params={"premium_proxy": True,
                "country_code": "tr",
                "render_js": False
                }
    )

    soup = BeautifulSoup(response.text, "html.parser")

    #CAR ADVERT NAME
    car_advert_name = soup.find('h1').get_text()

    #CAR INFO LIST
    car_brand_name = soup.find_all('ul', class_='classifiedInfoList')[0].get_text().strip()
    actualCarBrandNames = []
    car_brand_name_list = car_brand_name.split("\n")
    for item in car_brand_name_list:
        item.split()
        item = item.replace("\xa0","").replace("\t","")
        if item != '':
            actualCarBrandNames.append(item)

    car_brand_name = actualCarBrandNames[6].strip()
    car_series_name = actualCarBrandNames[8].strip()
    car_model_name = actualCarBrandNames[10].strip()
    car_year = actualCarBrandNames[13].strip()
    car_fuel = actualCarBrandNames[16].strip()
    car_transmission = actualCarBrandNames[19].strip()
    car_mileage = actualCarBrandNames[22].strip()
    car_hp = actualCarBrandNames[28].strip()
    car_engine_size = actualCarBrandNames[31].strip()

    #print(car_brand_name, car_series_name, car_model_name, car_year, car_fuel, car_transmission, car_mileage, car_hp, car_engine_size)

    car_price = soup.findAll('h3')[3].get_text().strip()
    actualCarList = []
    car_price_list = car_price.split("\n")
    for item in car_price_list:
        if item != "\n":
            actualCarList.append(item)
    car_price = actualCarList[0].replace(".","").replace(" TL","")

    with open('carInfos.csv', 'a', newline='') as csvfile:
        csv_writer = csv.writer(csvfile, delimiter=',')
        csv_writer.writerow((car_brand_name, car_series_name, car_model_name, car_year, car_fuel, car_transmission, car_mileage, car_hp, car_engine_size, car_price))

    return car_brand_name, car_series_name, car_model_name, car_year, car_fuel, car_transmission, car_mileage, car_hp, car_engine_size, car_price



#Need to add url counter to prevent api limits.
#Start reading from a specific line number.
#Need to change API_KEY at each new 100 requests
#ScrapingBee is giving 1000 credit and each request spends 10 credit
#BMW3 - 956 cars
#BMW5 - 950 cars
#Total credit needed: 20000 credits = 20 accounts
def readAdvertURL(filename):
    client = ScrapingBeeClient(
        api_key='GFOIIZMBUYHIG7EVJ0FULYH5XILPIWC37O1IQ7YC2QK8ORVJKX1IVT71DYZFOEEIEKYXO0B1JNTI8DVG')
    with open(filename, 'r') as read_obj:
        csv_reader = csv.reader(read_obj)
        for row in csv_reader:
            getCarDetails(client, row[1][:-2])

readAdvertURL('bmw3.csv')

#getCarDetails(client, "https://www.sahibinden.com/ilan/vasita-otomobil-bmw-2016-executive-msport-hatasiz-carbon-schwarz-hayalt-elktrkli-bgj-1010689689/detay")


"""

import csv

with open('source.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    rows = list(csv_reader)

    print(rows[8])
    print(rows[22])
    
---------------------------------------------------------------------------

with open('file.csv') as fd:
    reader=csv.reader(fd)
    interestingrows=[row for idx, row in enumerate(reader) if idx in (28,62)]
# now interestingrows contains the 28th and the 62th row after the header

"""


