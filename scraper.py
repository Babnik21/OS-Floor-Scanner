import requests
from bs4 import BeautifulSoup
import json
import csv

api_base_url = "https://api.nft20.io/pools?nft="
link = "https://nft20.io/asset/0x548aacf79c4ffc8ee263cae103239b1b06fe9025"



reader = csv.reader(open('nft_collections.csv', 'r'))
collections = {}
for row in reader:
    key, value = row
    api_url = api_base_url + value
    response = requests.get(api_url).json()
    #response_str = json.dumps(response, indent=2)
    buy_price = float(response['data'][0]['buy_price_eth']) * 1.11
    sell_price = float(response['data'][0]['sell_price_eth']) * 0.89
    collections[key] = {"address": value, "estimated buy price": buy_price, "estimated sell price": sell_price}


print(collections)




