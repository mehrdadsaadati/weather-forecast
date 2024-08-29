import pytest
import requests
from weather_forecast.api_caller import fetch_temperature_data
from weather_forecast.models import DailyTemperatureData, RequestFailedError


def test_fetch_temperature_data(mocker):
    """Test fetch temperature result"""

    mock_get = mocker.patch("weather_forecast.api_caller.requests.get")
    mock_response = mock_get.return_value
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "daily": {
            "time": ["2024-08-20", "2024-08-21", "2024-08-22"],
            "apparent_temperature_max": [20, 30, 40],
            "apparent_temperature_min": [10, 20, 30],
        }
    }

    result = fetch_temperature_data(0, 0, 1, 2)

    assert result == [
        DailyTemperatureData(20, 10, "2024-08-20"),
        DailyTemperatureData(30, 20, "2024-08-21"),
        DailyTemperatureData(40, 30, "2024-08-22"),
    ]


def test_fetch_temperature_data_failure(mocker):
    """Test fetch temperature failure"""

    mock_get = mocker.patch("weather_forecast.api_caller.requests.get")
    mock_response = mock_get.return_value
    mock_response.status_code = 400

    with pytest.raises(RequestFailedError):
        fetch_temperature_data(0, 0, 1, 2)
