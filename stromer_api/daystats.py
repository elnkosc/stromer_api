from .general import item
from .periodstats import PeriodStats


class DayStats(PeriodStats):
    def __init__(self, data: dict) -> None:
        super().__init__(data, item(data, "daily_info"))

    @property
    def start_date(self) -> str:
        return item(self._data, "start_date")

    @property
    def end_date(self) -> str:
        return item(self._data, "end_date")

    @property
    def total_days(self) -> int:
        return item(self._data, "total_days")

    @property
    def km_avg_30_days(self) -> float:
        return item(self._data, "km_avg_30_days")

    @property
    def day_record(self) -> float:
        return item(self._data, "day_record")

    def csv_dump(self, field_seperator=",") -> None:
        print("\"Day\",\"Active Days\",\"Distance (km)\",\"Duration(sec)\",\"Power (wh)\",\"First Record Date\"")
        for day in self:
            info = self[day]
            print(f"\"{day}\"",
                  info.active_days,
                  f"{info.km:.2f}",
                  info.sec,
                  info.wh,
                  f"\"{info.first_record}\"",
                  sep=field_seperator)
