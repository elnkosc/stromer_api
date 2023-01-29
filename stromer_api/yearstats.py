from .general import item
from .periodstats import PeriodStats


class YearStats(PeriodStats):
    def __init__(self, data: dict) -> None:
        super().__init__(data, item(data, "yearly_info"))

    @property
    def start_date(self) -> str:
        return item(self._data, "start_date")

    @property
    def end_date(self) -> str:
        return item(self._data, "end_date")

    @property
    def total_years(self) -> int:
        return item(self._data, "total_years")

    @property
    def km_avg_years_since_beginning(self) -> float:
        return item(self._data, "km_avg_years_since_beginning")

    @property
    def year_record(self) -> float:
        return item(self._data, "year_record")

    def csv_dump(self, field_seperator=",") -> None:
        print("\"Year\",\"Start Date\",\"End Date\",\"Total Days\",\"Active Days\",\"Distance (km)\","
              "\"Duration(sec)\",\"Power (wh)\",\"First Record Date\"")
        for year in self:
            info = self[year]
            print(year,
                  f"\"{info.start_date}\"",
                  f"\"{info.end_date}\"",
                  info.total_days,
                  info.active_days,
                  f"{info.km:.2f}",
                  info.sec,
                  info.wh,
                  f"\"{info.first_record}\"",
                  sep=field_seperator)
