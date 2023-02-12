import datetime
from .general import item
from .portal import Portal
from .bikedata import BikeDataFromPortal
from .periodstats import PeriodStats


class DayStats(BikeDataFromPortal, PeriodStats):
    def __init__(self, portal: Portal, year: int, month: int, day: int, num_days: int = 1) -> None:
        BikeDataFromPortal.__init__(self, portal)
        self.__statistics_endpoint = "bike/statistics"
        self.__extra_data_endpoint = "bike/statistics/extra_data"

        # start day cannot be in the future
        start_date = datetime.date(year, month, day)
        if start_date > datetime.date.today():
            raise Exception("Start date is in the future")
        start = start_date.strftime("%Y%m%d")

        # set stop_date to today if it is in the future
        stop_date = datetime.date(year, month, day) + datetime.timedelta(days=num_days - 1)
        if stop_date > datetime.date.today():
            stop = datetime.date.today().strftime("%Y%m%d")
        else:
            stop = stop_date.strftime("%Y%m%d")

        avg_rec = self._portal.get(self.__extra_data_endpoint,
                                   params={"end": stop, "resolution": "days"})

        daily_info = self._portal.get(self.__statistics_endpoint,
                                      params={"start": start, "end": stop, "resolution": "days"},
                                      full_list=True)

        self.__data = {"start_date": start,
                       "end_date": stop,
                       "total_days": len(daily_info),
                       "km_avg_30_days": avg_rec["km_avg_30_days"],
                       "day_record": avg_rec["day_record"],
                       "daily_info": {}}

        for day_info in daily_info:
            self.__data["daily_info"][day_info["start"]] = {"total_days": day_info["total_days"],
                                                           "active_days": day_info["active_days"],
                                                           "km": day_info["km"],
                                                           "sec": day_info["sec"],
                                                           "wh": day_info["wh"],
                                                           "first_record": day_info["first_record"]}

        PeriodStats.__init__(self, self.__data["daily_info"])

    @property
    def start_date(self) -> str:
        return item(self.__data, "start_date")

    @property
    def end_date(self) -> str:
        return item(self.__data, "end_date")

    @property
    def total_days(self) -> int:
        return item(self.__data, "total_days")

    @property
    def km_avg_30_days(self) -> float:
        return item(self.__data, "km_avg_30_days")

    @property
    def day_record(self) -> float:
        return item(self.__data, "day_record")

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

    def excel_dump(self, filename: str) -> None:
        self.create_worksheet(filename, "Day", "Active Days", "Distance (km) ", "Duration(sec)",
                              "Power (wh)", "First Record Date")
        for day in self:
            info = self[day]
            self.add_line(day, info.active_days, info.km, info.sec, info.wh, info.first_record)
        self.close_worksheet()
