from .general import item
from .portal import Portal
from .bikedata import BikeDataFromDict, BikeDataFromPortal


class BikeShop(BikeDataFromDict):
    def __init__(self, data: dict) -> None:
        super().__init__(data)

    @property
    def city(self) -> str:
        return item(self._data, "city")

    @property
    def country_code(self) -> str:
        return item(self._data, "country_code")

    @property
    def country_name(self) -> str:
        return item(self._data, "country_name")

    @property
    def debitor(self) -> str:
        return item(self._data, "debitor")

    @property
    def latitude(self) -> float:
        return item(self._data, "latitude")

    @property
    def longitude(self) -> float:
        return item(self._data, "longitude")

    @property
    def name(self) -> str:
        return item(self._data, "name")

    @property
    def phone(self) -> str:
        return item(self._data, "phone")

    @property
    def postal_code(self) -> str:
        return item(self._data, "postal_code")

    @property
    def street(self) -> str:
        return item(self._data, "street")


class BikeShopList(BikeDataFromPortal):
    def __init__(self, portal: Portal) -> None:
        super().__init__(portal=portal)
        self.__endpoint = "shops"
        self._data = []
        shops = self._portal.get(self.__endpoint, full_list=True)
        for shop in shops:
            self._data.append(BikeShop(shop))

    def __getitem__(self, i: int) -> BikeShop:
        return self._data[i]

    def lookup(self, shop_name: str) -> BikeShop | None:
        for shop in self._data:
            if shop_name.lower() in shop.name.lower():
                return shop
        return None
