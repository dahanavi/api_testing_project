import pytest
import requests

ENDPOINT = 'https://reqres.in/api/users?page=2'

def test_01_call_list_users_endpoint():
    respons = requests.get(ENDPOINT)
    assert respons.ok
    
    