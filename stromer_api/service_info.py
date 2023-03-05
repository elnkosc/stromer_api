from .general import item
from .portal import Portal
from .bikedata import BikeDataFromPortal
from .bikeshop import BikeShop
from .bikepart import BikePart
from .service_log import ServiceLog


class ServiceInfo(BikeDataFromPortal):
    def __init__(self, portal: Portal, bike_id: int) -> None:
        super().__init__(portal=portal)
        self.__endpoint = f"bike/{bike_id}/service_info"
        self._data = self._portal.get(self.__endpoint)
        self._bike_parts = None
        self._service_logs = None

    @property
    def shop(self) -> BikeShop:
        return BikeShop(item(self._data, "shop"))

    @property
    def vin(self) -> str:
        return item(self._data, "vin")

    @property
    def serial(self) -> str:
        return item(self._data, "serial")

    @property
    def service_logs(self) -> list:
        if self._service_logs is None:
            self._service_logs = []
            self._service_logs.extend(
                ServiceLog(log) for log in item(self._data, "servicelogs")
            )
        return self._service_logs

    @property
    def bike_parts(self) -> list:
        if self._bike_parts is None:
            self._bike_parts = []
            self._bike_parts.extend(
                BikePart(part) for part in item(self._data, "bikeparts")
            )
        return self._bike_parts
