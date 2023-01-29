from .general import item, BikeData


class PeriodicInfo(BikeData):
    def __init__(self, data: dict) -> None:
        super().__init__(data)

    @property
    def start_date(self) -> str:
        return item(self._data, "start_date")

    @property
    def end_date(self) -> str:
        return item(self._data, "end_date")

    @property
    def total_days(self) -> int:
        return item(self._data, "total_days")

    @property
    def active_days(self) -> int:
        return item(self._data, "active_days")

    @property
    def km(self) -> float:
        return item(self._data, "km")

    @property
    def sec(self) -> int:
        return item(self._data, "sec")

    @property
    def wh(self) -> int:
        return item(self._data, "wh")

    @property
    def first_record(self) -> str:
        return item(self._data, "first_record")
