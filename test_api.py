import requests
import pytest

# Тест на GET запит
def test_get_request():
    url = "https://jsonplaceholder.typicode.com/posts/1"
    response = requests.get(url)
    assert response.status_code == 200

    json_data = response.json()
    assert "id" in json_data
    assert json_data["id"] == 1

#Тест на POST запит
def test_post_request():
    url = "https://jsonplaceholder.typicode.com/posts"
    payload = {
        "title":"updated title",
        "body":"updated body",
        "userId":"1"
    }
    response = requests.post(url, payload)
    assert response.status_code == 201
    json_data = response.json()
    assert json_data ["title"] == payload ["title"]
    print(json_data)

#Тест на PUT запит

def test_put_request():
    url = "https://jsonplaceholder.typicode.com/post/1"
    payload = {
        "id":"1",
        "title":"updated title",
        "body":"updated body",
        "userId":"1"
    }
    response = requests.get(url)
    print(response.status_code)
   # json_data = response.json()
   # assert json_data["title"] == payload["title"]
    #print(json_data["title"])

