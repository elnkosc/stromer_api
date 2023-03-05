import datetime


def item(dictionary: dict, key_name: str, default_value: object = None):
    return None if dictionary is None else dictionary.get(key_name, default_value)


def time_str(seconds: int):
    return None if seconds is None else str(datetime.timedelta(seconds=seconds))


def datetime_str(timestamp: int):
    if timestamp is None:
        return None
    else:
        return datetime.datetime.fromtimestamp(timestamp).strftime("%A, %B %d, %Y %I:%M:%S")
