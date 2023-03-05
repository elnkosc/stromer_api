from .general import item, time_str, datetime_str
from .portal import Portal
from .bikedata import BikeData
from .bikemaintenance import BikeMaintenance
from .bikestate import BikeState
from .bikeposition import BikePosition
from .bikestatistics import BikeStatistics
from .bikesensors import BikeSensors
from .bikemotortuning import BikeMotorTuning
from .bikesettings import BikeSettings
from .bikeuser import BikeUser
from .yearstats import YearStats
from .monthstats import MonthStats
from .weekstats import WeekStats
from .daystats import DayStats
from .bikeshop import BikeShopList
from .service_info import ServiceInfo


class StromerBike:
    def __init__(self, username: str, password: str, client_id: str) -> None:
        self.__portal = Portal(username, password, client_id)
        self.__bike = self.__portal.get("bike")
        self.__state = None
        self.__position = None
        self.__statistics = None
        self.__sensors = None
        self.__motor_tuning = None
        self.__settings = None
        self.__user = None
        self.__shops = None
        self.__trip_data = None
        self.__service_info = None
        self.__day_stats = None
        self.__week_stats = None
        self.__month_stats = None
        self.__year_stats = None

    def refresh(self):
        self.__state = None
        self.__position = None
        self.__statistics = None
        self.__sensors = None
        self.__motor_tuning = None
        self.__settings = None
        self.__user = None
        self.__shops = None
        self.__trip_data = None
        self.__service_info = None
        self.__day_stats = None
        self.__week_stats = None
        self.__month_stats = None
        self.__year_stats = None

    @property
    def bikeid(self) -> int:
        return item(self.__bike, "bikeid")

    @property
    def nickname(self) -> str:
        return item(self.__bike, "nickname")

    @property
    def bikemodel(self) -> str:
        return item(self.__bike, "bikemodel")

    @property
    def biketype(self) -> str:
        return item(self.__bike, "biketype")

    @property
    def color(self) -> str:
        return item(self.__bike, "color")

    @property
    def size(self) -> str:
        return item(self.__bike, "size")

    @property
    def hardware(self) -> str:
        return item(self.__bike, "hardware")

    @property
    def connectivity(self) -> str:
        return item(self.__bike, "connectivity")

    @property
    def has_crash_detection(self) -> bool:
        return item(self.__bike, "has_crash_detection")

    @property
    def maintenance_feature(self) -> BikeMaintenance:
        return BikeMaintenance(item(self.__bike, "maintenance_feature"))

    @property
    def state(self) -> BikeState:
        if self.__state is None:
            self.__state = BikeState(self.__portal, self.bikeid)
        return self.__state

    @property
    def position(self) -> BikePosition:
        if self.__position is None:
            self.__position = BikePosition(self.__portal, self.bikeid)
        return self.__position

    @property
    def statistics(self) -> BikeStatistics:
        if self.__statistics is None:
            self.__statistics = BikeStatistics(self.__portal)
        return self.__statistics

    @property
    def sensors(self) -> BikeSensors:
        if self.__sensors is None:
            self.__sensors = BikeSensors(self.__portal, self.bikeid)
        return self.__sensors

    @property
    def motor_tuning(self) -> BikeMotorTuning:
        if self.__motor_tuning is None:
            self.__motor_tuning = BikeMotorTuning(self.__portal, self.bikeid)
        return self.__motor_tuning

    @property
    def settings(self) -> BikeSettings:
        if self.__settings is None:
            self.__settings = BikeSettings(self.__portal, self.bikeid)
        return self.__settings

    @property
    def user(self) -> BikeUser:
        if self.__user is None:
            self.__user = BikeUser(self.__portal)
        return self.__user

    @property
    def service_info(self) -> ServiceInfo:
        if self.__service_info is None:
            self.__service_info = ServiceInfo(self.__portal, self.bikeid)
        return self.__service_info

    @property
    def shops(self) -> BikeShopList:
        if self.__shops is None:
            self.__shops = BikeShopList(self.__portal)
        return self.__shops

    def day_stats(self, year: int, month: int, day: int, num_days: int = 1) -> DayStats:
        if self.__day_stats is None:
            self.__day_stats = DayStats(self.__portal, year, month, day, num_days)
        return self.__day_stats

    def week_stats(self, year: int, week: int, num_weeks: int = 1) -> WeekStats:
        if self.__week_stats is None:
            self.__week_stats = WeekStats(self.__portal, year, week, num_weeks)
        return self.__week_stats

    def month_stats(self, year: int, month: int, num_months: int = 1) -> MonthStats:
        if self.__month_stats is None:
            self.__month_stats = MonthStats(self.__portal, year, month, num_months)
        return self.__month_stats

    def year_stats(self, year: int, num_years: int = 1) -> YearStats:
        if self.__year_stats is None:
            self.__year_stats = YearStats(self.__portal, year, num_years)
        return self.__year_stats

    def reset_trip_data(self) -> bool:
        return self.__portal.delete(f"bike/id/{self.bikeid}/trip_data")

    def lock(self) -> bool:
        data = {"lock": True}
        new_data = self.__portal.post(f"bike/{self.bikeid}/settings", data)
        if new_data is not None:
            self.__state = None
            return True
        return False

    def unlock(self) -> bool:
        data = {"lock": False}
        new_data = self.__portal.post(f"bike/{self.bikeid}/settings", data)
        if new_data is not None:
            self.__state = None
            return True
        return False

    def light(self, mode: str) -> bool:
        if mode.lower() not in ["on", "off", "flash"]:
            return False
        data = {"mode": mode.lower()}
        new_data = self.__portal.post(f"bike/{self.bikeid}/light", data)
        if new_data is not None:
            self.__state = None
            return True
        return False
