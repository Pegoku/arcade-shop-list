import requests
import json
from flask import Flask, jsonify

app = Flask(__name__)

nItems = 0
nameItem = {}
priceItem = {}
imgItem = {}



# Example =
# {
#   "pageProps": {
#     "availableItems": [
#       {
#         "Name": "USB-C Charger",
#         "Small Name": "(30W)",
#         "Full Name": "USB-C Charger (30W)",
#         "Description": "Small, uses the latest GaN technology, & charges fast - pretty sweet!",
#         "Fulfillment Description": "Available US only. \n",
#         "Cost Hours": 6,
#         "id": "rec0yAytJaSyye10S",
#         "Image URL": "https://cloud-lit9nkas9-hack-club-bot.vercel.app/051t9lfjeuml._ac_sl1500_.png",
#         "Max Order Quantity": 1,
#         "Stock": 18,
#         "Category": ["Hardware"]
#       }, ...


url = "https://hackclub.com/_next/data/rUhEd7pIikv8meewfnRPN/arcade/shop.json"

response = requests.get(url)

if response.status_code == 200:
    data = json.loads(response.text)
    with open('data.json', 'w') as file:
        file.write(response.text)
    # print(data)
else:
    print("Error fetching data")

# Sort the items by cost
data['pageProps']['availableItems'].sort(key=lambda x: x['Cost Hours'])

# Remove stock = 0
data['pageProps']['availableItems'] = [item for item in data['pageProps']['availableItems'] if item['Stock'] != 0]

# Get the Full name of all the items followed by the cost in hours
for item in data['pageProps']['availableItems']:

    nItems += 1
    
    nameItem[nItems] = item['Full Name']
    priceItem[nItems] = item['Cost Hours']
    imgItem[nItems] = item['Image URL']
    
    # print(f"{item['Full Name']} - {item['Cost Hours']} hours")

for i in range(1, nItems+1):
    print(f"{i} {nameItem[i]} {priceItem[i]} {imgItem[i]}")

# Convert name price and img to json (all in one json)

# nameItem = json.dumps(nameItem)
# priceItem = json.dumps(priceItem)
# imgItem = json.dumps(imgItem)

@app.route('/fetch-name')
def fetch_name():
    return jsonify(nameItem)

@app.route('/fetch-price')
def fetch_price():
    return jsonify(priceItem)

@app.route('/fetch-img')
def fetch_img():
    return jsonify(imgItem)

@app.route('/')
def index():
    return "Hello World"

if __name__ == '__main__':
    app.run(debug=True)



