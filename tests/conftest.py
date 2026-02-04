import csv
import tempfile
from decimal import Decimal
from pathlib import Path

import pytest

from reports import DataRow


def create_temporary_csv_file(data: list[dict[str, str]]) -> Path:
    temp_file = tempfile.NamedTemporaryFile(mode="w", suffix=".csv", delete=False)
    writer = csv.DictWriter(
        temp_file,
        fieldnames=[
            "country",
            "year",
            "gdp",
            "gdp_growth",
            "inflation",
            "unemployment",
            "population",
            "continent",
        ],
    )
    writer.writeheader()

    for row in data:
        writer.writerow(row)

    temp_file.close()
    return Path(temp_file.name)


@pytest.fixture(scope="session")
def first_csv_file():
    test_data = [
        {
            "country": "United States",
            "year": "2020",
            "gdp": "1000",
            "gdp_growth": "2.0",
            "inflation": "5.0",
            "unemployment": "4.0",
            "population": "300",
            "continent": "North America",
        },
    ]
    csv_file = create_temporary_csv_file(test_data)
    yield csv_file
    csv_file.unlink()


@pytest.fixture(scope="session")
def second_csv_file():
    test_data = [
        {
            "country": "France",
            "year": "2020",
            "gdp": "1000",
            "gdp_growth": "2.0",
            "inflation": "5.0",
            "unemployment": "4.0",
            "population": "70",
            "continent": "Europe",
        },
        {
            "country": "France",
            "year": "2021",
            "gdp": "2000",
            "gdp_growth": "2.0",
            "inflation": "5.0",
            "unemployment": "4.0",
            "population": "70",
            "continent": "Europe",
        },
    ]
    csv_file = create_temporary_csv_file(test_data)
    yield csv_file
    csv_file.unlink()


@pytest.fixture(scope="session")
def germany_2020():
    return DataRow(
        country="Germany",
        year=2020,
        gdp=100,
        gdp_growth=Decimal(1.0),
        inflation=Decimal(2.0),
        unemployment=Decimal(5.0),
        population=80,
        continent="Europe",
    )


@pytest.fixture(scope="session")
def germany_2021():
    return DataRow(
        country="Germany",
        year=2021,
        gdp=200,
        gdp_growth=Decimal(1.0),
        inflation=Decimal(2.0),
        unemployment=Decimal(5.0),
        population=80,
        continent="Europe",
    )


@pytest.fixture(scope="session")
def japan_2020():
    return DataRow(
        country="Japan",
        year=2020,
        gdp=400,
        gdp_growth=Decimal(1.0),
        inflation=Decimal(2.0),
        unemployment=Decimal(5.0),
        population=80,
        continent="Europe",
    )


@pytest.fixture(scope="session")
def japan_2021():
    return DataRow(
        country="Japan",
        year=2021,
        gdp=200,
        gdp_growth=Decimal(1.0),
        inflation=Decimal(2.0),
        unemployment=Decimal(5.0),
        population=80,
        continent="Europe",
    )
