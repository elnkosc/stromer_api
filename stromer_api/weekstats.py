from .general import item
from .portal import Portal
from .bikedata import BikeDataFromPortal
from .periodstats import PeriodStats
import datetime


class WeekStats(BikeDataFromPortal, PeriodStats):
    def __init__(self, portal: Portal, year: int, week: int, num_weeks: int = 1) -> None:
        BikeDataFromPortal.__init__(self, portal)
        self.__statistics_endpoint = "bike/statistics"
        self.__extra_data_endpoint = "bike/statistics/extra_data"

        # start day cannot be in the future
        start_date = datetime.date.fromisocalendar(year, week, 1)
        if start_date > datetime.date.today():
            raise Exception("Start date is in the future")
        start = start_date.strftime("%Y%m%d")

        # set stop_date to today if it is in the future
        stop_date = datetime.date.fromisocalendar(year, week + num_weeks - 1, 7)
        if stop_date > datetime.date.today():
            stop = datetime.date.today().strftime("%Y%m%d")
        else:
            stop = stop_date.strftime("%Y%m%d")

        avg_rec = self._portal.get("bike/statistics/extra_data",
                                   params={"end": stop, "resolution": "weeks"})
        weekly_info = self._portal.get("bike/statistics",
                                       params={"start": start, "end": stop, "resolution": "weeks"},
                                       full_list=True)

        self.__data = {"start_date": start,
                       "end_date": stop,
                       "total_weeks": len(weekly_info),
                       "km_avg_12_weeks": avg_rec["km_avg_12_weeks"],
                       "week_record": avg_rec["week_record"],
                       "weekly_info": {}}

        for week_info in weekly_info:
            year_nr = datetime.datetime.strptime(week_info["start"], "%Y%m%d").year
            week_nr = datetime.datetime.strptime(week_info["start"], "%Y%m%d").isocalendar().week
            week_nr_str = "%04d-W%02d" % (year_nr, week_nr)

            # week_end_day cannot be in the future
            week_last_day = datetime.datetime.strptime(week_info["start"], "%Y%m%d") + datetime.timedelta(days=6)
            if week_last_day > datetime.datetime.today():
                week_end_day = stop
            else:
                week_end_day = week_last_day.strftime("%Y%m%d")

            self.__data["weekly_info"][week_nr_str] = {"start_date": week_info["start"],
                                                       "end_date": week_end_day,
                                                       "total_days": week_info["total_days"],
                                                       "active_days": week_info["active_days"],
                                                       "km": week_info["km"],
                                                       "sec": week_info["sec"],
                                                       "wh": week_info["wh"],
                                                       "first_record": week_info["first_record"]}

        PeriodStats.__init__(self, self.__data["weekly_info"])

    @property
    def start_date(self) -> str:
        return item(self.__data, "start_date")

    @property
    def end_date(self) -> str:
        return item(self.__data, "end_date")

    @property
    def total_weeks(self) -> int:
        return item(self.__data, "total_weeks")

    @property
    def km_avg_12_weeks(self) -> float:
        return item(self.__data, "km_avg_12_weeks")

    @property
    def week_record(self) -> float:
        return item(self.__data, "week_record")

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

    def excel_dump(self, filename: str) -> None:
        self.create_worksheet(filename, "Week", "Start Date", "End Date", "Total Days", "Active Days", "Distance (km)",
                              "Duration(sec)", "Power (wh)", "First Record Date")
        for week in self:
            info = self[week]
            self.add_line(week, info.start_date, info.end_date, info.total_days, info.active_days, info.km,
                          info.sec, info.wh, info.first_record)
        self.close_worksheet()
