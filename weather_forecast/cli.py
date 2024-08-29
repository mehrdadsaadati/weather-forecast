import click
from weather_forecast.api_caller import fetch_temperature_data
from typing import List
from weather_forecast.models import DailyTemperatureData
import plotext as plt


def _print_samples(samples: List[DailyTemperatureData], past: int):
    print()
    print((12 + 3 + 10 + 3 + 10) * "=")
    print(f"{'Date':<12} | {'Min Temp':<10} | {'Max Temp':<10}")
    print((12 + 3 + 10 + 3 + 10) * "=")
    for i in range(len(samples)):
        s = samples[i]
        if i == past:
            print(f"{'Today':<12} | {s.temperature_min:<10} | {s.temperature_max:<10}")
        else:
            print(f"{s.date:<12} | {s.temperature_min:<10} | {s.temperature_max:<10}")
        print((15 + 3 + 10 + 3 + 10) * "-")
    print()


def _plot_samples(samples: List[DailyTemperatureData], past: int):
    dates = [sample.date for sample in samples]
    dates[past] = "Today"
    max_temps = [sample.temperature_max for sample in samples]
    min_temps = [sample.temperature_min for sample in samples]

    plt.simple_multiple_bar(
        dates,
        [min_temps, max_temps],
        width=100,
        labels=["Min Temp", "Max Temp"],
        title="Min and Max Temperature",
    )
    plt.show()


@click.command()
@click.option("--lat", type=float, required=True, help="Latitude of requested location")
@click.option(
    "--lng", type=float, required=True, help="Longitude of requested location"
)
@click.option(
    "--past", type=int, default=1, help="Past days in forecast (e.g., 3 for 3 days ago)"
)
@click.option(
    "--future",
    type=int,
    default=7,
    help="Future days in forecast (e.g., 3 for 3 days ahead)",
)
@click.option("--plot", is_flag=True, help="Draw the plot of forecast")
def get_temperature(lat, lng, past, future, plot):
    """CLI app to get temperature forecast of specified zone"""
    if past < 0 or future < 0:
        click.echo("Past and future days must be non-negative.")
        return

    try:
        samples = fetch_temperature_data(lat, lng, past, future)
        _print_samples(samples, past)
        if plot:
            _plot_samples(samples, past)

    except Exception as exc:
        print(f"Error: {exc}")


if __name__ == "__main__":
    get_temperature()
