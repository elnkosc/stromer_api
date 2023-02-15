import datetime


def item(dictionary: dict, key_name: str, default_value: object = None):
    if dictionary is None:
        return None
    if key_name in dictionary:
        return dictionary[key_name]
    else:
        return default_value


def time_str(seconds: int):
    if seconds is None:
        return None
    else:
        return str(datetime.timedelta(seconds=seconds))


def datetime_str(timestamp: int):
    if timestamp is None:
        return None
    else:
        return datetime.datetime.fromtimestamp(timestamp).strftime("%A, %B %d, %Y %I:%M:%S")
