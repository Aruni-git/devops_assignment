
import requests

def test_departments():
    
    url = "http://127.0.0.1:5000/"
    
    response = requests.get(url)
    assert response.status_code == 200