from .general import item, BikeData


class BikeSensors(BikeData):
    def __init__(self, data: dict) -> None:
        super().__init__(data)

    @property
    def user_torque_sensitivity(self) -> int:
        return item(self._data, "user_torque_sensitivity")

    @property
    def recup_level_user_offset(self) -> int:
        return item(self._data, "recup_level_user_offset")
