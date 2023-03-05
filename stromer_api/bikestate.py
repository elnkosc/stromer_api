from .general import time_str, datetime_str, item
from .portal import Portal
from .bikedata import BikeDataFromPortal


class BikeState(BikeDataFromPortal):
    def __init__(self, portal: Portal, bike_id: int, cached: bool = False) -> None:
        super().__init__(portal=portal)
        self.__endpoint = f"bike/{bike_id}/state"
        self.__params = {"cached": "true"} if cached else {"cached": "false"}
        self._data = self._portal.get(self.__endpoint, self.__params)

    @property
    def trip_distance(self) -> float:
        return item(self._data, "trip_distance")

    @property
    def suiversion(self) -> str:
        return item(self._data, "suiversion")

    @property
    def average_speed_trip(self) -> float:
        return item(self._data, "average_speed_trip")

    @property
    def power_on_cycles(self) -> int:
        return item(self._data, "power_on_cycles")

    @property
    def tntversion(self) -> str:
        return item(self._data, "tntversion")

    @property
    def atmospheric_pressure(self) -> int:
        return item(self._data, "atmospheric_pressure")

    @property
    def battery_SOC(self) -> int:
        return item(self._data, "battery_SOC")

    @property
    def assistance_level(self) -> int:
        return item(self._data, "assistance_level")

    @property
    def bike_speed(self) -> float:
        return item(self._data, "bike_speed")

    @property
    def trip_time(self) -> int:
        return item(self._data, "trip_time")

    @property
    def trip_time_str(self) -> str:
        return time_str(item(self._data, "trip_time"))

    @property
    def battery_health(self) -> int:
        return item(self._data, "battery_health")

    @property
    def theft_flag(self) -> bool:
        return item(self._data, "theft_flag")

    @property
    def motor_temp(self) -> float:
        return item(self._data, "motor_temp")

    @property
    def battery_temp(self) -> float:
        return item(self._data, "battery_temp")

    @property
    def rcvts(self) -> int:
        return item(self._data, "rcvts")

    @property
    def rcvts_str(self) -> str:
        return datetime_str(item(self._data, "rcvts"))

    @property
    def average_energy_consumption(self) -> int:
        return item(self._data, "average_energy_consumption")

    @property
    def total_time(self) -> int:
        return item(self._data, "total_time")

    @property
    def total_time_str(self) -> str:
        return time_str(item(self._data, "total_time"))

    @property
    def total_distance(self) -> float:
        return item(self._data, "total_distance")

    @property
    def light_on(self) -> int:
        return item(self._data, "light_on")

    @property
    def total_energy_consumption(self) -> int:
        return item(self._data, "total_energy_consumption")

    @property
    def lock_flag(self) -> bool:
        return item(self._data, "lock_flag")
