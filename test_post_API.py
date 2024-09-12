import requests

endpoint = "https://reqres.in/api/users"

payload = {
    "name": "Suresh",
    "job": "Tester"
}

def test_post_request():
    response = requests.post(endpoint, json=payload)

    assert response.status_code == 201
    json_response = response.json()

    assert json_response.get("name") == "Suresh"
    assert "id" in json_response
    print(json_response)