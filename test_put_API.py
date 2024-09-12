import requests

endpoint = "https://reqres.in/api"

payload = {
    "name": "morpheus",
    "job": "zion resident"
}

def test_put_request():
    response = requests.put(endpoint + "/api/users/2", json=payload)

    assert response.status_code == 200
    json_response = response.json()

    assert json_response.get("name") == "morpheus"
    assert json_response.get("job") == "zion resident"
    print(json_response)