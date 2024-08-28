import requests
import json

url = "https://hackclub.com/_next/data/rUhEd7pIikv8meewfnRPN/arcade/shop.json"

response = requests.get(url)

d

if response.status_code == 200:
    data = json.loads(response.text)
    print(data)
else:
    print("Error fetching data")

