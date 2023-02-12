from .general import item
from .portal import Portal
from .bikedata import BikeDataFromPortal


class BikeMotorTuning(BikeDataFromPortal):
    def __init__(self, portal: Portal, bike_id: int) -> None:
        super().__init__(portal=portal)
        self.__params = {"fields": "tuning_speed,tuning_torque,tuning_agility"}
        self.__endpoint = "bike/%s/settings" % bike_id
        self._data = self._portal.get(self.__endpoint, self.__params)

    @property
    def tuning_torque(self) -> int:
        return item(self._data, "tuning_torque")

    @property
    def tuning_speed(self) -> int:
        return item(self._data, "tuning_speed")

    @property
    def tuning_agility(self) -> int:
        return item(self._data, "tuning_agility")

    def set(self, speed: int = None, torque: int = None, agility: int = None) -> None:
        if speed is None:
            speed = self.tuning_speed
        else:
            speed = speed

        if torque is None:
            torque = self.tuning_speed
        else:
            torque = torque

        if agility is None:
            agility = self.tuning_agility
        else:
            agility = agility

        data = {"tuning_speed": speed,
                "tuning_torque": torque,
                "tuning_agility": agility}
        new_data = self._portal.post(self.__endpoint, data)
        if new_data is not None:
            self._data = new_data

    @tuning_torque.setter
    def tuning_torque(self, val: int):
        self.set(torque=val)

    @tuning_agility.setter
    def tuning_agility(self, val: int):
        self.set(agility=val)

    @tuning_speed.setter
    def tuning_speed(self, val: int):
        self.set(speed=val)
