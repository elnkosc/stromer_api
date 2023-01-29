from .general import item, BikeData


class BikeShop(BikeData):
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
