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
    assert response.status_code==200
    assert data["name"]==payload["name"]
    assert data["data"]==payload["data"]

    print(data)







