import requests
import json
import pandas as pd
import csv


api_base_url = "https://api.nft20.io/pools?nft="
link = "https://nft20.io/asset/0x548aacf79c4ffc8ee263cae103239b1b06fe9025"

# Estimates gas (conservative estimate)
def estimate_gas():
    gas_api = "https://ethgasstation.info/api/ethgasAPI.json?api-key=80a3af92f807f016fd9967ffdadf9dd82ff67b04cdb55b6574ba8f8e3169"
    gas = requests.get(gas_api).json()
    return gas["fastest"]//10


'''
test_collection = "0x134460d32fc66a6d84487c20dcd9fdcf92316017"
api_url = api_base_url + test_collection
response = requests.get(api_url).json()
response_str = json.dumps(response, indent=2)
print(response['data'][0]['nft_locked'])
'''

reader = csv.reader(open('nft_collections.csv', 'r'))
collections = {}
for row in reader:
    name, address, n_items = row
    api_url = api_base_url + address
    response = requests.get(api_url).json()
    #response_str = json.dumps(response, indent=2)
    buy_price = float(response['data'][0]['buy_price_eth']) * 1.11
    sell_price = float(response['data'][0]['sell_price_eth']) * 0.89
    n_items_2 = int(response['data'][0]['nft_locked'])
    collections[name] = {"address": address, "estimated buy price": buy_price, "estimated sell price": sell_price, "items": n_items_2, "items change": n_items_2 - int(n_items)}

df = pd.DataFrame.from_dict(collections, orient="index")
output = df[["address", "items"]]

output.to_csv("nft_collections.csv", sep=',', header=False)





