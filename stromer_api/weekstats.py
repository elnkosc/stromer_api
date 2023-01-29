from .general import item
from .periodstats import PeriodStats


class WeekStats(PeriodStats):
    def __init__(self, data: dict) -> None:
        super().__init__(data, item(data, "weekly_info"))

    @property
    def start_date(self) -> str:
        return item(self._data, "start_date")

    @property
    def end_date(self) -> str:
        return item(self._data, "end_date")

    @property
    def total_weeks(self) -> int:
        return item(self._data, "total_weeks")

    @property
    def km_avg_12_weeks(self) -> float:
        return item(self._data, "km_avg_12_weeks")

    @property
    def week_record(self) -> float:
        return item(self._data, "week_record")

    def csv_dump(self, field_seperator=",") -> None:
        print("\"Week\",\"Start Date\",\"End Date\",\"Total Days\",\"Active Days\",\"Distance (km)\","
              "\"Duration(sec)\",\"Power (wh)\",\"First Record Date\"")
        for week in self:
            info = self[week]
            print(f"\"{week}\"",
                  f"\"{info.start_date}\"",
                  f"\"{info.end_date}\"",
                  info.total_days,
                  info.active_days,
                  f"{info.km:.2f}",
                  info.sec,
                  info.wh,
                  f"\"{info.first_record}\"",
                  sep=field_seperator)
