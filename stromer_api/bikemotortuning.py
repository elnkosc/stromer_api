from .general import item, BikeData


class BikeMotorTuning(BikeData):
    def __init__(self, data: dict) -> None:
        super().__init__(data)

    @property
    def tuning_torque(self) -> int:
        return item(self._data, "tuning_torque")

    @property
    def tuning_speed(self) -> int:
        return item(self._data, "tuning_speed")

    @property
    def tuning_agility(self) -> int:
        return item(self._data, "tuning_agility")
