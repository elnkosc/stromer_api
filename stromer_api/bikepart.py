from .general import item
from .bikedata import BikeDataFromDict


class BikePart(BikeDataFromDict):
    def __init__(self, data: dict) -> None:
        super().__init__(data)

    @property
    def serial(self) -> str:
        return item(self._data, "serial")

    @property
    def name(self) -> str:
        return item(self._data, "name")

    @property
    def category(self) -> str:
        return item(self._data, "category")
