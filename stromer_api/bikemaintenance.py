from .general import item
from .bikedata import BikeDataFromDict


class BikeMaintenance(BikeDataFromDict):
    def __init__(self, data: dict) -> None:
        super().__init__(data)

    @property
    def display_maintenance_event(self) -> bool:
        return item(self._data, "display_maintenance_event")

    @property
    def next_maintenance_km(self) -> int:
        return item(self._data, "next_maintenance_km")

    @property
    def next_maintenance_date(self) -> str:
        return item(self._data, "next_maintenance_date")

    @property
    def next_maintenance_interval(self) -> int:
        return item(self._data, "next_maintenance_interval")

    @property
    def customer_enabled_maintenance(self) -> bool:
        return item(self._data, "customer_enabled_maintenance")

    @property
    def last_maintenance_reset_km(self) -> int:
        return item(self._data, "last_maintenance_reset_km")

    @property
    def last_maintenance_reset_date(self) -> str:
        return item(self._data, "last_maintenance_reset_date")
