import requests
import pytest


def obj_id():
    payload = {
       "name": "Apple MacBook Pro 24",
       "data": {
           'year': 2024,
           'price': 1849.99,
           'CPU model': "Intel Core i9",
           'Hard disk size': "1 TB"
       }
    }

    response = requests.post('https://api.restful-api.dev/objects/',json=payload)
    assert response.status_code==200



