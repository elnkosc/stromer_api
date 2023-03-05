from .general import item
from .portal import Portal
from .bikedata import BikeDataFromPortal


class BikeSensors(BikeDataFromPortal):
    def __init__(self, portal: Portal, bike_id: int) -> None:
        super().__init__(portal=portal)
        self.__params = {"fields": "recup_level_user_offset,user_torque_sensitivity"}
        self.__endpoint = f"bike/{bike_id}/settings"
        self._data = self._portal.get(self.__endpoint, self.__params)

    @property
    def user_torque_sensitivity(self) -> int:
        return item(self._data, "user_torque_sensitivity")

    @property
    def recup_level_user_offset(self) -> int:
        return item(self._data, "recup_level_user_offset")

    def set(self, recup: int = None, torque: int = None) -> None:
        recup = self.recup_level_user_offset if recup is None else recup
        torque = self.user_torque_sensitivity if torque is None else torque
        data = {"recup_level_user_offset": recup,
                "user_torque_sensitivity": torque}
        new_data = self._portal.post(self.__endpoint, data)
        if new_data is not None:
            self._data = new_data

    @recup_level_user_offset.setter
    def recup_level_user_offset(self, val: int) -> None:
        self.set(recup=val)

    @user_torque_sensitivity.setter
    def user_torque_sensitivity(self, val: int) -> None:
        self.set(torque=val)
