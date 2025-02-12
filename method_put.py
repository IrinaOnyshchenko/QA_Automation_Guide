import requests

payload = {
   "name": "Apple MacBook Pro 20",
   "data": {
      "year": 2019,
      "price": 1849.99,
      "CPU model": "Intel Core i9",
      "Hard disk size": "1 TB"
   }
}

response = requests.post("https://api.restful-api.dev/objects/ff8081819111e7b201911367210b037e", json=payload)
print(response.json())