from .general import item
from .portal import Portal
from .bikedata import BikeDataFromPortal


class BikeSettings(BikeDataFromPortal):
    def __init__(self, portal: Portal, bike_id: int) -> None:
        super().__init__(portal=portal)
        self.__params = {"fields": "auto_lock_mode,auto_power_off_time,date_format,"
                                   "distance_unit,language,speed_unit,clock_format"}
        self.__endpoint = f"bike/{bike_id}/settings"
        self._data = self._portal.get(self.__endpoint, self.__params)

    @property
    def auto_lock_mode(self) -> bool:
        return item(self._data, "auto_lock_mode")

    @property
    def auto_power_off_time(self) -> int:
        return item(self._data, "auto_power_off_time")

    @property
    def clock_format(self) -> str:
        return item(self._data, "clock_format")

    @property
    def date_format(self) -> str:
        return item(self._data, "date_format")

    @property
    def distance_unit(self) -> str:
        return item(self._data, "distance_unit")

    @property
    def language(self) -> str:
        return item(self._data, "language")

    @property
    def speed_unit(self) -> str:
        return item(self._data, "speed_unit")

    def set(self, auto_lock_mode: bool = None, auto_power_off_time: int = None, clock_format: str = None,
            date_format: str = None, distance_unit: str = None, language: str = None, speed_unit: str = None) -> None:
        if auto_lock_mode is None:
            auto_lock_mode = self.auto_lock_mode
        else:
            auto_lock_mode = auto_lock_mode

        if auto_power_off_time is None or auto_power_off_time not in [0, 180, 300, 600]:
            auto_power_off_time = self.auto_power_off_time
        else:
            auto_power_off_time = auto_power_off_time

        if clock_format is None or clock_format.lower() not in ["12h", "24h"]:
            clock_format = self.clock_format
        else:
            clock_format = clock_format.lower()

        if date_format is None or date_format.upper() not in ["DD_MM_YYYY", "MM_DD_YYYY"]:
            date_format = self.date_format
        else:
            date_format = date_format.upper()

        if distance_unit is None or distance_unit not in ["km", "mi"]:
            distance_unit = self.distance_unit
        else:
            distance_unit = distance_unit

        if language is None or language.lower() not in ["nl", "de", "fr", "en"]:
            language = self.language
        else:
            language = language.lower()

        if speed_unit is None or speed_unit.lower() not in ["kmh", "mph"]:
            speed_unit = self.speed_unit
        else:
            speed_unit = speed_unit.lower()

        data = {"auto_lock_mode": auto_lock_mode,
                "auto_power_off_time": auto_power_off_time,
                "clock_format": clock_format,
                "date_format": date_format,
                "distance_unit": distance_unit,
                "language": language,
                "speed_unit": speed_unit}
        new_data = self._portal.post(self.__endpoint, data)
        if new_data is not None:
            self._data = new_data

    @auto_lock_mode.setter
    def auto_lock_mode(self, val: bool) -> None:
        self.set(auto_lock_mode=val)

    @auto_power_off_time.setter
    def auto_power_off_time(self, val: int) -> None:
        self.set(auto_power_off_time=val)

    @clock_format.setter
    def clock_format(self, val: str) -> None:
        self.set(clock_format=val)

    @date_format.setter
    def date_format(self, val: str) -> None:
        self.set(date_format=val)

    @distance_unit.setter
    def distance_unit(self, val: str) -> None:
        self.set(distance_unit=val)

    @language.setter
    def language(self, val: str) -> None:
        self.set(language=val)

    @speed_unit.setter
    def speed_unit(self, val: str) -> None:
        self.set(speed_unit=val)
