import requests
import datetime
from urllib.parse import urlencode, parse_qs, splitquery


def item(dictionary: dict, key_name: str, default_value: object = None):
    if key_name in dictionary:
        return dictionary[key_name]
    else:
        return default_value


def time_str(seconds: int) -> str:
    return str(datetime.timedelta(seconds=seconds))


def datetime_str(timestamp: int) -> str:
    return datetime.datetime.fromtimestamp(timestamp).strftime("%A, %B %d, %Y %I:%M:%S")


class BikeState:
    def __init__(self, state: dict) -> None:
        self.__state = state

    def __str__(self):
        return str(self.__state)

    @property
    def trip_distance(self) -> float:
        return item(self.__state, "trip_distance")

    @property
    def suiversion(self) -> str:
        return item(self.__state, "suiversion")

    @property
    def average_speed_trip(self) -> float:
        return item(self.__state, "average_speed_trip")

    @property
    def power_on_cycles(self) -> int:
        return item(self.__state, "power_on_cycles")

    @property
    def tntversion(self) -> str:
        return item(self.__state, "tntversion")

    @property
    def atmospheric_pressure(self) -> int:
        return item(self.__state, "atmospheric_pressure")

    @property
    def battery_SOC(self) -> int:
        return item(self.__state, "battery_SOC")

    @property
    def assistance_level(self) -> int:
        return item(self.__state, "assistance_level")

    @property
    def bike_speed(self) -> float:
        return item(self.__state, "bike_speed")

    @property
    def trip_time(self) -> int:
        return item(self.__state, "trip_time")

    @property
    def trip_time_str(self) -> str:
        return time_str(item(self.__state, "trip_time"))

    @property
    def battery_health(self) -> int:
        return item(self.__state, "battery_health")

    @property
    def theft_flag(self) -> bool:
        return item(self.__state, "theft_flag")

    @property
    def motor_temp(self) -> float:
        return item(self.__state, "motor_temp")

    @property
    def battery_temp(self) -> float:
        return item(self.__state, "battery_temp")

    @property
    def rcvts(self) -> int:
        return item(self.__state, "rcvts")

    @property
    def rcvts_str(self) -> str:
        return datetime_str(item(self.__state, "rcvts"))

    @property
    def average_energy_consumption(self) -> int:
        return item(self.__state, "average_energy_consumption")

    @property
    def total_time(self) -> int:
        return item(self.__state, "total_time")

    @property
    def total_time_str(self) -> str:
        return time_str(item(self.__state, "total_time"))

    @property
    def total_distance(self) -> float:
        return item(self.__state, "total_distance")

    @property
    def light_on(self) -> int:
        return item(self.__state, "light_on")

    @property
    def total_energy_consumption(self) -> int:
        return item(self.__state, "total_energy_consumption")

    @property
    def lock_flag(self) -> bool:
        return item(self.__state, "lock_flag")


class BikePosition:
    def __init__(self, position: dict) -> None:
        self.__position = position

    def __str__(self):
        return str(self.__position)

    @property
    def latitude(self) -> float:
        return item(self.__position, "latitude")

    @property
    def longitude(self) -> float:
        return item(self.__position, "longitude")

    @property
    def altitude(self) -> int:
        return item(self.__position, "altitude")

    @property
    def speed(self) -> float:
        return item(self.__position, "speed")

    @property
    def timets(self) -> int:
        return item(self.__position, "timets")

    @property
    def timets_str(self) -> str:
        return datetime_str(item(self.__position, "timets"))

    @property
    def rcvts(self) -> int:
        return item(self.__position, "rcvts")

    @property
    def rcvts_str(self) -> str:
        return datetime_str(item(self.__position, "rcvts"))


class StromerBike:
    __url = "https://stromer-portal.ch/mobile/v4/login/"
    __token_url = "https://stromer-portal.ch/mobile/v4/o/token/"
    __api_url = "https://api3.stromer-portal.ch/rapi/mobile/v4.1/"

    def __init__(self, username: str, password: str, client_id: str) -> None:
        self.__session = requests.session()
        self.__session.get(self.__url)
        self.__state = None
        self.__position = None

        qs = urlencode(
            {
                "client_id": client_id,
                "response_type": "code",
                "redirect_url": "stromerauth://auth",
                "scope": "bikeposition bikestatus bikeconfiguration bikelock biketheft bikedata bikepin bikeblink userprofile"
            }
        )

        data = {
            "password": password,
            "username": username,
            "csrfmiddlewaretoken": self.__session.cookies.get("csrftoken"),
            "next": "/mobile/v4/o/authorize/?" + qs
        }

        res = self.__session.post(self.__url, data=data, headers={"Referer": self.__url}, allow_redirects=False)
        res = self.__session.send(res.next, allow_redirects=False)
        _, qs = splitquery(res.headers["Location"])
        query = parse_qs(qs)
        if "code" in query:
            code = query["code"][0]
        else:
            raise KeyError("Code not present in return object")

        params = {
            "grant_type": "authorization_code",
            "client_id": client_id,
            "code": code,
            "redirect_uri": "stromer://auth"
        }

        res = requests.post(self.__token_url, params=params)
        if "access_token" in res.json():
            self.__access_token = res.json()["access_token"]
        else:
            raise KeyError("access_token not found")

        self.__bike = self.get_endpoint("bike")

    def get_endpoint(self, endpoint):
        res = requests.get(self.__api_url + endpoint,
                           headers={"Authorization": "Bearer %s" % self.__access_token},
                           params={})
        if "data" in res.json() and isinstance(res.json()["data"], list):
            return res.json()["data"][0]
        else:
            raise KeyError("No bike data found")

    def update(self):
        self.__state = None
        self.__position = None

    @property
    def state(self):
        if self.__state is None:
            self.__state = BikeState(self.get_endpoint("bike/%s/state" % self.__bike["bikeid"]))
        return self.__state

    @property
    def position(self):
        if self.__position is None:
            self.__position = BikePosition(self.get_endpoint("bike/%s/position" % self.__bike["bikeid"]))
        return self.__position
