"""
This code reads advert links from a .csv file and
sends them one by one to a function which is scrapes needed
information from website.
After getting needed information, writes into another .csv file
to prepare the dataset.
"""

from bs4 import BeautifulSoup
import csv
from scrapingbee import ScrapingBeeClient


def get_car_details(client, main_url):
    response = client.get(
        main_url,
        params={"premium_proxy": True,
                "country_code": "tr",
                "render_js": False
                }
    )

    soup = BeautifulSoup(response.text, "html.parser")

    # CAR ADVERT NAME
    car_advert_name = soup.find('h1').get_text()

    # CAR INFO LIST
    car_brand_name = soup.find_all('ul', class_='classifiedInfoList')[0].get_text().strip()
    actual_car_brand_names = []
    car_brand_name_list = car_brand_name.split("\n")
    for item in car_brand_name_list:
        item.split()
        item = item.replace("\xa0", "").replace("\t", "")
        if item != '':
            actual_car_brand_names.append(item)

    car_brand_name = actual_car_brand_names[6].strip()
    car_series_name = actual_car_brand_names[8].strip()
    car_model_name = actual_car_brand_names[10].strip()
    car_year = actual_car_brand_names[13].strip()
    car_fuel = actual_car_brand_names[16].strip()
    car_transmission = actual_car_brand_names[19].strip()
    car_mileage = actual_car_brand_names[22].strip()
    car_hp = actual_car_brand_names[28].strip()
    car_engine_size = actual_car_brand_names[31].strip()

    car_price = soup.findAll('h3')[4].get_text().strip()
    for i in range(len(car_price)):
        if car_price[i] == 'T':
            break
    car_price = car_price[:i - 1]
    actual_car_list = []
    car_price_list = car_price.split("\n")
    for item in car_price_list:
        if item != "\n":
            actual_car_list.append(item)
    print(car_price)

    if car_price is not None:
        with open('carInfos.csv', 'a', newline='') as csvfile:
            csv_writer = csv.writer(csvfile, delimiter=',')
            csv_writer.writerow((car_brand_name, car_series_name, car_model_name, car_year, car_fuel, car_transmission,
                                 car_mileage, car_hp, car_engine_size, car_price))


def read_advert_url(filename):
    client = ScrapingBeeClient(
        api_key='TTAIJBHCDX2FTF1SSJTE6ZDNL7C4WC7ZMJFH1MMNWK50KQOVUOYBR716JPKQ2V37822MLPQIJOOW46Q1')

    with open(filename, 'r') as read_obj:
        csv_reader = csv.reader(read_obj)

        start_index = 950
        finish_index = 956
        read_list = [row for row in csv_reader]

        try:
            for i in range(start_index, finish_index):
                get_car_details(client, read_list[i][1][:-1])
        except Exception as e:
            print(e)


read_advert_url('CarURLs.csv')

# get_car_details(client, "https://www.sahibinden.com/ilan/vasita-otomobil-bmw-2016-executive-msport-hatasiz-carbon-schwarz-hayalt-elktrkli-bgj-1010689689/detay")
