import pytest

from conftest import get_test_data, get_config_data
from utils.api_client import APIClient

@pytest.fixture(scope="module")
def api_client():
    return APIClient()

BASE_URL = get_config_data("users")["base_url"]

def test_get_users(api_client):
    response = api_client.get(BASE_URL,"/users")
    assert response.status_code == 200
    assert len(response.json())>0

@pytest.mark.parametrize("user_data",get_test_data("user_test_cases"))
def test_create_users(api_client,user_data):
    response = api_client.post(BASE_URL,"users",user_data)
    print(response.json())
    assert response.status_code == 201
    assert response.json()['name'] == user_data["name"]

@pytest.mark.parametrize("user_data",get_test_data("user_test_cases"))
def test_update_users(api_client,user_data):
    response = api_client.put(BASE_URL,"users/1",user_data)
    print(response.json())
    assert response.status_code == 200
    assert response.json()['name'] == user_data["name"]

@pytest.mark.parametrize("user_id",[1])
def test_delete_users(api_client,user_id):
    response = api_client.delete(BASE_URL,f"users/{user_id}")
    print(response.json())
    assert response.status_code == 200
