from .portal import Portal


class BikeData:
    def __init__(self) -> None:
        self.__data = None

    def __str__(self) -> str:
        return str(self.__data)


class BikeDataFromDict(BikeData):
    def __init__(self, data: dict) -> None:
        super().__init__()
        self._data = data


class BikeDataFromPortal(BikeData):
    def __init__(self, portal: Portal) -> None:
        super().__init__()
        self._portal = portal
