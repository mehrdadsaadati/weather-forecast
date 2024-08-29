class DailyTemperatureData:
    """Daily temperature information"""

    def __init__(
        self, temperature_max: float, temperature_min: float, date: str
    ) -> None:
        """Daily temperature information

        Args:
            temperature_max (float): Max temperature of day
            temperature_min (float): Max temperature of day
            date (str): Date of the sample
        """
        self.temperature_max = temperature_max
        self.temperature_min = temperature_min
        self.date = date

    def __eq__(self, value: object) -> bool:
        if isinstance(value, DailyTemperatureData):
            return (
                value.temperature_max == self.temperature_max
                and value.temperature_min == self.temperature_min
                and value.date == self.date
            )

        return False
