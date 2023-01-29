import datetime


def item(dictionary: dict, key_name: str, default_value: object = None):
    if key_name in dictionary:
        return dictionary[key_name]
    else:
        return default_value


def time_str(seconds: int) -> str:
    return str(datetime.timedelta(seconds=seconds))


def datetime_str(timestamp: int) -> str:
    return datetime.datetime.fromtimestamp(timestamp).strftime("%A, %B %d, %Y %I:%M:%S")


class BikeData:
    def __init__(self, data: dict) -> None:
        self._data = data

    def __str__(self) -> str:
        return str(self._data)
