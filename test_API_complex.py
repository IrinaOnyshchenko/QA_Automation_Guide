import requests
import pytest


def test_post():
    payload = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    }
    response = requests.post("https://api.restful-api.dev/objects", json=payload)
    data = response.json()
    assert response.status_code == 200
    assert data["name"] == payload["name"]
    assert data["data"] == payload["data"]

    print(data)

def test_put_change_data():
    payload = {
   "name": "Apple MacBook Pro 16",
   "data": {
      "year": 2019,
      "price": 2049.99,
      "CPU model": "Intel Core i9",
      "Hard disk size": "1 TB",
      "color": "pink"
   }
}
    data_change = requests.put("https://api.restful-api.dev/objects/ff808181914f0eee0191519eaa5706f4", json=payload)
    new_data = data_change.json()
    assert data_change.status_code==200
    assert new_data ["data"]==payload["data"]
    print(new_data)

def test_get_data():
    receive = requests.get("https://api.restful-api.dev/objects/ff808181914f0eee0191519eaa5706f4")
    assert receive.status_code==200
    rec = receive.json()
    print(rec)




