from .general import item
from .bikedata import BikeDataFromPortal
from .portal import Portal
from .periodstats import PeriodStats
import datetime
import calendar


class MonthStats(BikeDataFromPortal, PeriodStats):
    def __init__(self, portal: Portal, year: int, month: int, num_months: int = 1) -> None:
        # sourcery skip: raise-specific-error
        BikeDataFromPortal.__init__(self, portal)
        self.__statistics_endpoint = "bike/statistics"
        self.__extra_data_endpoint = "bike/statistics/extra_data"

        # start day cannot be in the future
        start_date = datetime.date(year, month, 1)
        if start_date > datetime.date.today():
            raise Exception("Start date is in the future")
        start = "%04d%02d%02d" % (year, month, 1)

        # set stop_date to today if it is in the future
        stop_month = (month + num_months - 2) % 12 + 1
        stop_year = year + (month + num_months - 2) // 12
        stop_date = datetime.date(stop_year, stop_month, calendar.monthrange(stop_year, stop_month)[1])
        if stop_date > datetime.date.today():
            stop = datetime.date.today().strftime("%Y%m%d")
        else:
            stop = "%04d%02d%02d" % (stop_year, stop_month, calendar.monthrange(stop_year, stop_month)[1])

        avg_rec = self._portal.get("bike/statistics/extra_data",
                                   params={"end": stop, "resolution": "months"})
        monthly_info = self._portal.get("bike/statistics",
                                        params={"start": start, "end": stop, "resolution": "months"},
                                        full_list=True)

        self.__data = {"start_date": start,
                       "end_date": stop,
                       "total_months": len(monthly_info),
                       "km_avg_12_months": avg_rec["km_avg_12_months"],
                       "month_record": avg_rec["month_record"],
                       "monthly_info": {}}

        for month_info in monthly_info:
            year_nr = datetime.datetime.strptime(month_info["start"], "%Y%m%d").year
            month_nr = datetime.datetime.strptime(month_info["start"], "%Y%m%d").month
            month_nr_str = "%04d-%02d" % (year_nr, month_nr)
            month_end_day = calendar.monthrange(year_nr, month_nr)[1]

            # end_day cannot be future date
            if datetime.date(year_nr, month_nr, month_end_day) > datetime.date.today():
                end_date = stop
            else:
                end_date = "%04d%02d%02d" % (year_nr, month_nr, month_end_day)

            self.__data["monthly_info"][month_nr_str] = {"start_date": month_info["start"],
                                                         "end_date": end_date,
                                                         "total_days": month_info["total_days"],
                                                         "active_days": month_info["active_days"],
                                                         "km": month_info["km"],
                                                         "sec": month_info["sec"],
                                                         "wh": month_info["wh"],
                                                         "first_record": month_info["first_record"]}

        PeriodStats.__init__(self, self.__data["monthly_info"])

    @property
    def start_date(self) -> str:
        return item(self.__data, "start_date")

    @property
    def end_date(self) -> str:
        return item(self.__data, "end_date")

    @property
    def total_months(self) -> int:
        return item(self.__data, "total_months")

    @property
    def km_avg_12_months(self) -> float:
        return item(self.__data, "km_avg_12_months")

    @property
    def month_record(self) -> float:
        return item(self.__data, "month_record")

    def csv_dump(self, field_seperator=",") -> None:
        print("\"Month\",\"Start Date\",\"End Date\",\"Total Days\",\"Active Days\",\"Distance (km)\","
              "\"Duration(sec)\",\"Power (wh)\",\"First Record Date\"")
        for month in self:
            info = self[month]
            print(f"\"{month}\"",
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
        self.create_worksheet(filename, "Month", "Start Date", "End Date", "Total Days", "Active Days",
                              "Distance (km)", "Duration(sec)", "Power (wh)", "First Record Date")
        for month in self:
            info = self[month]
            self.add_line(month, info.start_date, info.end_date, info.total_days, info.active_days, info.km,
                          info.sec, info.wh, info.first_record)
        self.close_worksheet()
