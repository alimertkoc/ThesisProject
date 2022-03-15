# from bs4 import BeautifulSoup
# import requests
from scrapingbee import ScrapingBeeClient

MAIN_URL = "https://whatismyipaddress.com/"

payload = {"country_code": "tr",
          "premium_proxy": "True",
          "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.109 Safari/537.36"}


client = ScrapingBeeClient(api_key='W9LUFY03GBFL3G4IYH1C5NF9PC8LBBG1QJECP350H7EZPKNU208915VPIVQ4HMBAMB3AMCNMQ3RG0IK7')
response = client.get(
    MAIN_URL,
    headers=payload
)

print(response.content)
