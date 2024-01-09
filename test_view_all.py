
import requests

def test_view_all_employees():
    
    url = "http://127.0.0.1:5000/allemployees"
    
    response = requests.get(url)
    assert response.status_code == 200