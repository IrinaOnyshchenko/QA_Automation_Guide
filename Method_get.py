import requests

payload = {
   "name": "Apple MacBook Pro 16",
   "data": {
      "year": 2023,
      "price": 2049.99,
      "CPU model": "Intel Core i9",
      "Hard disk size": "1 TB",
      "color": "silver"
   }
}

response = requests.get("https://api.restful-api.dev/objects/ff808181913b3faf01913d271fa701de", json=payload)
print(response.json())