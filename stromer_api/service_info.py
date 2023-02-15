from .general import item
from .portal import Portal
from .bikedata import BikeDataFromPortal
from .bikeshop import BikeShop
from .bikepart import BikePart
from .service_log import ServiceLog


class ServiceInfo(BikeDataFromPortal):
    def __init__(self, portal: Portal, bike_id: int) -> None:
        super().__init__(portal=portal)
        self.__endpoint = "bike/%s/service_info" % bike_id
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
            for log in item(self._data, "servicelogs"):
                self._service_logs.append(ServiceLog(log))
        return self._service_logs

    @property
    def bike_parts(self) -> list:
        if self._bike_parts is None:
            self._bike_parts = []
            for part in item(self._data, "bikeparts"):
                self._bike_parts.append(BikePart(part))
        return self._bike_parts
