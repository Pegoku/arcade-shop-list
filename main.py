import requests
import json
from flask import Flask, jsonify, send_from_directory

app = Flask(__name__)

def fetch_and_process_data():
    url = "https://hackclub.com/_next/data/rUhEd7pIikv8meewfnRPN/arcade/shop.json"
    response = requests.get(url)

    if response.status_code == 200:
        data = json.loads(response.text)
    else:
        print("Error fetching data")
        return None

    # Sort the items by cost
    data['pageProps']['availableItems'].sort(key=lambda x: x['Cost Hours'])

    # Remove stock = 0
    data['pageProps']['availableItems'] = [item for item in data['pageProps']['availableItems'] if item['Stock'] != 0]

    # Get the Full name of all the items followed by the cost in hours
    nItems = 0
    nameItem = {}
    priceItem = {}
    imgItem = {}

    for item in data['pageProps']['availableItems']:
        nItems += 1
        nameItem[nItems] = item['Full Name']
        priceItem[nItems] = item['Cost Hours']
        imgItem[nItems] = item['Image URL']

    return {
        "nameItem": nameItem,
        "priceItem": priceItem,
        "imgItem": imgItem
    }

@app.route('/fetch-data')
def fetch_data():
    data = fetch_and_process_data()
    if data:
        return jsonify(data)
    else:
        return jsonify({"error": "Error fetching data"}), 500


# @app.route('/fetch-name')
# def fetch_name():
#     return jsonify(nameItem)

# @app.route('/fetch-price')
# def fetch_price():
#     return jsonify(priceItem)

# @app.route('/fetch-img')
# def fetch_img():
#     return jsonify(imgItem)

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')


if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')



