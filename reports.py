import csv
from abc import ABC, abstractmethod
from dataclasses import dataclass
from decimal import Decimal
from pathlib import Path
from typing import Any

from tabulate import tabulate


@dataclass
class DataRow:
    country: str
    year: int
    gdp: int
    gdp_growth: Decimal
    inflation: Decimal
    unemployment: Decimal
    population: int
    continent: str


class Report(ABC):
    def parse_csv_files(self, csv_files: list[Path]) -> list[DataRow]:
        data = []

        for file in csv_files:
            with file.open() as f:
                for row in csv.DictReader(f):
                    data_row = DataRow(
                        country=row["country"],
                        year=int(row["year"]),
                        gdp=int(row["gdp"]),
                        gdp_growth=Decimal(row["gdp_growth"]),
                        inflation=Decimal(row["inflation"]),
                        unemployment=Decimal(row["unemployment"]),
                        population=int(row["population"]),
                        continent=row["continent"],
                    )
                    data.append(data_row)

        return data

    def display_report(self, report: dict[str, list[Any]]) -> None:
        print(
            tabulate(
                report,
                headers="keys",
                tablefmt="psql",
                floatfmt=".2f",
                showindex=range(1, len(list(report.values())[0]) + 1),
            )
        )

    @abstractmethod
    def generate_report(self, data: list[DataRow]) -> dict[str, list[Any]]:
        pass


class AverageGDPReport(Report):
    def generate_report(self, data: list[DataRow]) -> dict[str, list[Any]]:
        countries = {}
        for data_row in data:
            if data_row.country in countries:
                countries[data_row.country].append(data_row.gdp)
            else:
                countries[data_row.country] = [data_row.gdp]

        gdp_by_country = [
            (sum(gdp_values) / len(gdp_values), country)
            for country, gdp_values in countries.items()
        ]
        gdp_by_country.sort(reverse=True)

        return {
            "countries": [country for _, country in gdp_by_country],
            "average-gdp": [gdp for gdp, _ in gdp_by_country],
        }
