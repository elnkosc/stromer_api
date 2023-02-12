from .general import item
from .portal import Portal
from .bikeshop import BikeShop
from .bikedata import BikeDataFromPortal


class BikeUser(BikeDataFromPortal):
    def __init__(self, portal: Portal) -> None:
        super().__init__(portal=portal)
        self.__endpoint = "user"
        self._data = self._portal.get(self.__endpoint)

    @property
    def accepted_gdpr_version(self) -> str:
        return item(self._data, "accepted_gdpr_version")

    @property
    def city(self) -> str:
        return item(self._data, "city")

    @property
    def country(self) -> str:
        return item(self._data, "country")

    @property
    def email(self) -> str:
        return item(self._data, "email")

    @property
    def first_name(self) -> str:
        return item(self._data, "first_name")

    @property
    def gender(self) -> str:
        return item(self._data, "gender")

    @property
    def house_number(self) -> str:
        return item(self._data, "house_number")

    @property
    def last_name(self) -> str:
        return item(self._data, "last_name")

    @property
    def may_receive_mails(self) -> bool:
        return item(self._data, "may_receive_mails")

    @property
    def mobile(self) -> str:
        return item(self._data, "mobile")

    @property
    def phone(self) -> str:
        return item(self._data, "phone")

    @property
    def postal_code(self) -> str:
        return item(self._data, "postal_code")

    @property
    def size(self) -> float:
        return item(self._data, "size")

    @property
    def street_name(self) -> str:
        return item(self._data, "street_name")

    @property
    def weight(self) -> float:
        return item(self._data, "weight")

    @property
    def shop(self) -> BikeShop:
        return BikeShop(item(self._data, "shop"))
