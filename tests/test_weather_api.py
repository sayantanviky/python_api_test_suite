import logging

import pytest

from conftest import get_test_data, get_config_data
from utils.api_client import APIClient

@pytest.fixture(scope="module")
def api_client():
    return APIClient()

BASE_URL = get_config_data("weather")["base_url"]
endpoint = "/data/2.5/onecall?lat=40.7143&lon=-74.006&units=metric&appid=5796abbde9106b7da4febfae8c44c232"

@pytest.mark.parametrize("weather_data",get_test_data("weather_test_cases"))
def test_get_weather_status(api_client,weather_data):
    response = api_client.get(BASE_URL, endpoint)

    logging.info("Testing the weather status...")
    logging.info(f"Expected status: {weather_data['expected_status']}, Actual status: {response.status_code}")

    assert response.status_code==weather_data["expected_status"], \
        f"Expected status{weather_data['expected_status']} but found {response.status_code}"

@pytest.mark.parametrize("weather_data",get_test_data("weather_test_cases"))
def test_time_zone_if_new_york(api_client,weather_data):
    response = api_client.get(BASE_URL,endpoint)

    logging.info("Timezone checking...")
    logging.info(f"Expected {weather_data["timezone"]} and Actual timezone {response.json()["timezone"]}")

    try:
        assert response.json()["timezone"] == weather_data["timezone"],\
        (f"Incorrect timezone is selected or incorrect response found."
         f"expected {weather_data["timezone"]} but found {response.json()["timezone"]}")
    except AssertionError as e:
        pytest.xfail(str(e))

@pytest.mark.dependency(name="current_weather_presence")
def test_get_current_weather(api_client):
    response = api_client.get(BASE_URL,endpoint)

    logging.info("Checking if this is a real time weather data...")

    assert "current" in response.json(), "'current' key not found in response"

@pytest.mark.dependency(depends=["current_weather_presence"])
def test_get_weather_not_empty(api_client):
    response = api_client.get(BASE_URL, endpoint)

    logging.info("Checking if JSON response is not empty...")

    assert len(response.json())>0, f"Length of JSON is {response.json()}"

@pytest.mark.dependency(depends=["current_weather_presence"])
@pytest.mark.parametrize("weather_data",get_test_data("weather_test_cases"))
def test_get_weather_temperature(api_client,weather_data):
    response=api_client.get(BASE_URL,endpoint)

    logging.info("Checking for weather temperature is under permissible limit...")

    temp=response.json()["current"].get("temp")
    logging.info(f"Current temperature found is :{temp}")
    assert weather_data["min_temp"]<=temp<=weather_data["max_temp"],\
    f"Generated temperature {temp} is not coming under the range of {weather_data["min_temp"]} - {weather_data["max_temp"]}"
