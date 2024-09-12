import requests

endpoint = "https://reqres.in/api/users/2"

def test_delete_request():
    response = requests.delete(endpoint)

    assert response.status_code == 204
    assert response.text == '' 
    print("\n\nUser deleted successfully!")