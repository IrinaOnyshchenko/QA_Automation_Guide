import requests

response = requests.delete("https://api.restful-api.dev/objects/ff8081819111e7b201911367210b037e")
print(response.json())