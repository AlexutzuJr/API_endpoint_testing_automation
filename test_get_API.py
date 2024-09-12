import requests

endpoint = "https://reqres.in/api/users/2"

def test_get_API_endpoint():
    response = requests.get(endpoint)

    assert response.status_code == 200
    json_response = response.json()
    assert json_response["data"]["id"] == 2
    assert "email" in json_response["data"]
    print(json_response)