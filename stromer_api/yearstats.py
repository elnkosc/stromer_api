from .general import item
from .portal import Portal
from .bikedata import BikeDataFromPortal
from .periodstats import PeriodStats
import datetime


class YearStats(BikeDataFromPortal, PeriodStats):
    def __init__(self, portal: Portal, year: int, num_years: int = 1) -> None:
        BikeDataFromPortal.__init__(self, portal)
        self.__statistics_endpoint = "bike/statistics"
        self.__extra_data_endpoint = "bike/statistics/extra_data"

        # start day cannot be in the future
        start_date = datetime.date.fromisocalendar(year, 1, 1)
        if start_date > datetime.date.today():
            raise Exception("Start date is in the future")
        start = "%04d%02d%02d" % (year, 1, 1)

        # set stop_date to today if it is in the future
        stop_date = datetime.date(year + num_years - 1, 12, 31)
        if stop_date > datetime.date.today():
            stop = datetime.date.today().strftime("%Y%m%d")
        else:
            stop = stop_date.strftime("%Y%m%d")

        avg_rec = self._portal.get("bike/statistics/extra_data",
                                   params={"end": stop, "resolution": "years"})
        yearly_info = self._portal.get("bike/statistics",
                                       params={"start": start, "end": stop, "resolution": "years"},
                                       full_list=True)

        self.__data = {"start_date": start,
                       "end_date": stop,
                       "total_years": len(yearly_info),
                       "km_avg_years_since_beginning": avg_rec["km_avg_years_since_beginning"],
                       "year_record": avg_rec["year_record"],
                       "yearly_info": {}}

        for year_info in yearly_info:
            year_nr = datetime.datetime.strptime(year_info["start"], "%Y%m%d").year

            # end_date cannot be in the future
            if datetime.date(year_nr, 12, 31) > datetime.date.today():
                end_date = stop
            else:
                end_date = "%04d%02d%02d" % (year_nr, 12, 31)

            self.__data["yearly_info"][str(year_nr)] = {"start_date": year_info["start"],
                                                        "end_date": end_date,
                                                        "total_days": year_info["total_days"],
                                                        "active_days": year_info["active_days"],
                                                        "km": year_info["km"],
                                                        "sec": year_info["sec"],
                                                        "wh": year_info["wh"],
                                                        "first_record": year_info["first_record"]}

        PeriodStats.__init__(self, self.__data["yearly_info"])

    @property
    def start_date(self) -> str:
        return item(self.__data, "start_date")

    @property
    def end_date(self) -> str:
        return item(self.__data, "end_date")

    @property
    def total_years(self) -> int:
        return item(self.__data, "total_years")

    @property
    def km_avg_years_since_beginning(self) -> float:
        return item(self.__data, "km_avg_years_since_beginning")

    @property
    def year_record(self) -> float:
        return item(self.__data, "year_record")

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

    def excel_dump(self, filename: str) -> None:
        self.create_worksheet(filename, "Year", "Start Date", "End Date", "Total Days", "Active Days",
                              "Distance (km)", "Duration(sec)", "Power (wh)", "First Record Date")
        for year in self:
            info = self[year]
            self.add_line(year, info.start_date, info.end_date, info.total_days, info.active_days, info.km,
                          info.sec, info.wh, info.first_record)
        self.close_worksheet()
