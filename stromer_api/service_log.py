from .general import item
from .bikedata import BikeDataFromDict


class ServiceLog(BikeDataFromDict):
    def __init__(self, data: dict) -> None:
        super().__init__(data)

    @property
    def note(self) -> str:
        return item(self._data, "note")

    @property
    def created_on(self) -> int:
        return item(self._data, "created_on")
