# weather-forecast

A simple CLI app to fetch temperature forecast from [open-meteo](https://open-meteo.com). Can display data as table or plot inside console.

## What does it do?

This CLI app fetches temperature data from [open-meteo](https://open-meteo.com) based on user passed location and presents it as table or plot.

## How to use?

```bash
weather_forecast --lat lat --lng lng --past 1 --future 7 --plot
```

- lat: Float, Required. Latitude of requested location
- lng: Float, Required. Longitude of requested location
- past: Integer, Optional. Past days to include in data forecast
- future: Integer, Optional. Future days to include in data forecast
- plot: Flag, Optional. Draw result as plot in console

### Examples

```bash
>poetry run forecast --lat 35.6944 --lng 51.4215 --past 3 --future 5 --plot

======================================
Date         | Min Temp   | Max Temp
======================================
2024-08-26   | 23.2       | 36.0
-----------------------------------------
2024-08-27   | 24.8       | 37.3
-----------------------------------------
2024-08-28   | 21.9       | 35.0
-----------------------------------------
Today        | 23.3       | 32.5
-----------------------------------------
2024-08-30   | 19.0       | 29.8
-----------------------------------------
2024-08-31   | 16.5       | 30.5
-----------------------------------------
2024-09-01   | 16.6       | 30.9
-----------------------------------------
2024-09-02   | 17.1       | 31.3
-----------------------------------------

──────────── Min and Max Temperature ─────────────
2024-08-26 ▇▇▇▇▇▇▇▇▇▇▇▇ 23.2
           ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 36.0

2024-08-27 ▇▇▇▇▇▇▇▇▇▇▇▇▇ 24.8
           ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 37.300000000000004

2024-08-28 ▇▇▇▇▇▇▇▇▇▇▇▇ 21.900000000000002
           ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 35.0

Today      ▇▇▇▇▇▇▇▇▇▇▇▇ 23.3
           ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 32.5

2024-08-30 ▇▇▇▇▇▇▇▇▇▇ 19.0
           ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 29.8

2024-08-31 ▇▇▇▇▇▇▇▇▇ 16.5
           ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 30.5

2024-09-01 ▇▇▇▇▇▇▇▇▇ 16.6
           ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 30.900000000000002

2024-09-02 ▇▇▇▇▇▇▇▇▇ 17.1
           ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 31.3
─────────── ▇▇▇ Min Temp ▇▇▇ Max Temp ────────────
```

## Installation

```bash
poetry install
poetry run forecast
```
