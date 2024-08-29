import requests
from typing import List
from weather_forecast.models import DailyTemperatureData, RequestFailedError


def fetch_temperature_data(
    lat: float, lng: float, past_days: int = 1, forecast_days: int = 7
) -> List[DailyTemperatureData]:
    """Fetches temperature data of specified location from open-meteo.com

    Args:
        lat (float): latitude of the specified location
        lng (float): longitude of the specified location
        past_days (int, optional): past days to include in data. Defaults to 1.
        forecast_days (int, optional): future days to include in data. Defaults to 7.

    Returns:
        List[DailyTemperatureData]: List of temperature data samples
    """

    try:
        response = requests.get(
            f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lng}&daily=apparent_temperature_max,apparent_temperature_min&timezone=auto&past_days={past_days}&forecast_days={forecast_days}"
        )

        if response.status_code == 200:
            samples = []
            data = response.json()
            for i in range(past_days + forecast_days):
                date = data["daily"]["time"][i]
                min_temp = data["daily"]["apparent_temperature_min"][i]
                max_temp = data["daily"]["apparent_temperature_max"][i]
                samples.append(DailyTemperatureData(max_temp, min_temp, date))

            return samples
        else:
            raise RequestFailedError(f"Request rejected: {response.json()}")
    except BaseException as exc:
        raise RequestFailedError(f"Failed to fetch data: {exc}")
