from .general import item, datetime_str, BikeData


class BikePosition(BikeData):
    def __init__(self, data: dict) -> None:
        super().__init__(data)

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
