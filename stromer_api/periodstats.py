from .general import item
from .periodicinfo import PeriodicInfo
import xlsxwriter


class PeriodStats:
    def __init__(self, info: dict) -> None:
        self.__info = info
        self.__sorted = sorted(self.__info)
        self.__info_iterator = None
        self.__workbook = None
        self.__worksheet = None
        self.__line_number = 0

    def __getitem__(self, period: str) -> PeriodicInfo:
        return PeriodicInfo(item(self.__info, period))

    def __iter__(self):
        self.__info_iterator = iter(self.__sorted)
        return self

    def __next__(self):
        return next(self.__info_iterator)

    @property
    def info(self) -> dict:
        return self.__info

    def create_worksheet(self, filename: str, *args) -> None:
        self.__workbook = xlsxwriter.Workbook(filename.replace("\"", "/") + ".xlsx")
        self.__worksheet = self.__workbook.add_worksheet()
        headers = tuple(args)
        header_format = self.__workbook.add_format({"bold": True})
        self.__worksheet.write_row("A1", headers, header_format)
        self.__line_number = 1

    def add_line(self, *args):
        data = tuple(args)
        self.__line_number += 1
        self.__worksheet.write_row(f"A{self.__line_number}", data)

    def close_worksheet(self):
        self.__worksheet.autofit()
        self.__workbook.close()
