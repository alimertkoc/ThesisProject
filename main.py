# from bs4 import BeautifulSoup
# import requests
from scrapingbee import ScrapingBeeClient


URL = "https://www.sahibinden.com/ilan/vasita-otomobil-bmw-degisensiz-bmw-dizel-m-paket-19-jant-cobra-f1-istma-hafiza-kltk-996619222/detay"
MAIN_URL = "https://www.sahibinden.com/bmw?pagingOffset=50&pagingSize=50"

payload = {"country_code": "tr",
          "premium_proxy": "True",
          "sec-gpc": "?1",
          "sec-fetch-site": "same-origin",
          "sec-fetch-mode": "navigate",
          "sec-fetch-dest": "document",
          "sec-fetch-user": "?1",
          "upgrade-insecure-requests": "1",
          "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.109 Safari/537.36"}


client = ScrapingBeeClient(api_key='W9LUFY03GBFL3G4IYH1C5NF9PC8LBBG1QJECP350H7EZPKNU208915VPIVQ4HMBAMB3AMCNMQ3RG0IK7')
response = client.get(
    MAIN_URL,
    params={"premium_proxy": True,
            "country_code": "tr",
          }
)

print('Response HTTP Status Code: ', response.status_code)
print('Response HTTP Response Body: ', response.content)



