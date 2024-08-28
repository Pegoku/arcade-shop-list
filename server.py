from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/fetch-data')
def fetch_data():
    url = "https://hackclub.com/_next/data/rUhEd7pIikv8meewfnRPN/arcade/shop.json"
    response = requests.get(url)
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(debug=True)