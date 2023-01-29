from .general import item, BikeData
from .periodicinfo import PeriodicInfo


class PeriodStats(BikeData):
    def __init__(self, data: dict, info: dict) -> None:
        super().__init__(data)
        self.__info = info
        self.__sorted = sorted(self.__info)
        self.__info_iterator = None

    def __getitem__(self, period: str) -> PeriodicInfo:
        return PeriodicInfo(item(self.__info, period))

    def __iter__(self):
        self.__info_iterator = iter(self.__sorted)
        return self

    def __next__(self):
        return next(self.__info_iterator)

    @property
    def info(self) -> dict:
        return self.__info
