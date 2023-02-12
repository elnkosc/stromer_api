from .general import item, datetime_str
from .portal import Portal
from .bikedata import BikeDataFromPortal


class BikePosition(BikeDataFromPortal):
    def __init__(self, portal: Portal, bike_id: int, cached: bool = False) -> None:
        super().__init__(portal=portal)
        self.__endpoint = "bike/%s/position" % bike_id
        if cached:
            self.__params = {"cached": "true"}
        else:
            self.__params = {"cached": "false"}
        self._data = self._portal.get(self.__endpoint, self.__params)

    @property
    def latitude(self) -> float:
        return item(self._data, "latitude")

    @property
    def longitude(self) -> float:
        return item(self._data, "longitude")

    @property
    def altitude(self) -> int:
        return item(self._data, "altitude")

    @property
    def speed(self) -> float:
        return item(self._data, "speed")

    @property
    def timets(self) -> int:
        return item(self._data, "timets")

    @property
    def timets_str(self) -> str:
        return datetime_str(item(self._data, "timets"))

    @property
    def rcvts(self) -> int:
        return item(self._data, "rcvts")

    @property
    def rcvts_str(self) -> str:
        return datetime_str(item(self._data, "rcvts"))
