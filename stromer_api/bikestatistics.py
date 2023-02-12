from .general import item, time_str
from .portal import Portal
from .bikedata import BikeDataFromPortal


class BikeStatistics(BikeDataFromPortal):
    def __init__(self, portal: Portal) -> None:
        super().__init__(portal=portal)
        self.__endpoint = "bike/statistics/all"
        self._data = self._portal.get(self.__endpoint)

    @property
    def total_km(self) -> float:
        return item(self._data, "total_km")

    @property
    def average_km(self) -> float:
        return item(self._data, "average_km")

    @property
    def total_sec(self) -> int:
        return item(self._data, "total_sec")

    @property
    def total_time_str(self) -> str:
        return time_str(item(self._data, "total_sec"))

    @property
    def average_sec(self) -> float:
        return item(self._data, "average_sec")

    @property
    def average_time_str(self) -> str:
        return time_str(item(self._data, "average_sec"))

    @property
    def total_wh(self) -> int:
        return item(self._data, "total_wh")

    @property
    def average_wh(self) -> float:
        return item(self._data, "average_wh")

    @property
    def kmh(self) -> float:
        return item(self._data, "kmh")

    @property
    def average_kmh(self) -> float:
        return item(self._data, "average_kmh")

    @property
    def active_days(self) -> int:
        return item(self._data, "active_days")

    @property
    def average_days(self) -> float:
        return item(self._data, "average_days")
