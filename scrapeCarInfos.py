from bs4 import BeautifulSoup
import re
from urllib.request import Request, urlopen
import requests
from allConsts import header, header1
from scrapingbee import ScrapingBeeClient
#AEM0KAHPRSGVJK68YKMP6I8THC8LWFKWKI1EWSPUJXDJO7S2R2KZMHM5N43N6S0Z8D6I2JIPIBAMUOOU
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


    #car_brand_name, car_series_name, car_model_name, car_year, car_fuel, car_transmission, car_mileage, car_hp, car_engine_size, car_price

client = ScrapingBeeClient(
    api_key='GFOIIZMBUYHIG7EVJ0FULYH5XILPIWC37O1IQ7YC2QK8ORVJKX1IVT71DYZFOEEIEKYXO0B1JNTI8DVG')

getCarDetails(client, "https://www.sahibinden.com/ilan/vasita-otomobil-bmw-2016-executive-msport-hatasiz-carbon-schwarz-hayalt-elktrkli-bgj-1010689689/detay")






