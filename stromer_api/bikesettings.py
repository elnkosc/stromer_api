from .general import item, BikeData


class BikeSettings(BikeData):
    def __init__(self, data: dict) -> None:
        super().__init__(data)

    @property
    def auto_lock_mode(self) -> bool:
        return item(self._data, "auto_lock_mode")

    @property
    def auto_power_off_time(self) -> int:
        return item(self._data, "auto_power_off_time")

    @property
    def clock_format(self) -> str:
        return item(self._data, "clock_format")

    @property
    def date_format(self) -> str:
        return item(self._data, "date_format")

    @property
    def distance_unit(self) -> str:
        return item(self._data, "distance_unit")

    @property
    def language(self) -> str:
        return item(self._data, "language")

    @property
    def speed_unit(self) -> str:
        return item(self._data, "speed_unit")
