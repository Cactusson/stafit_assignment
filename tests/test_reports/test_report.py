from unittest.mock import patch

from reports import DataRow, Report


@patch.multiple(Report, __abstractmethods__=set())
class TestReport:
    def test_parse_one_csv_file(self, first_csv_file):
        report = Report()  # type: ignore
        result = report.parse_csv_files([first_csv_file])
        assert len(result) == 1
        assert type(result[0]) is DataRow
        assert hasattr(result[0], "country")
        assert result[0].country == "United States"
        assert result[0].year == 2020
        assert result[0].gdp == 1000
        assert result[0].population == 300

    def test_parse_two_csv_files(self, first_csv_file, second_csv_file):
        report = Report()  # type: ignore
        result = report.parse_csv_files([first_csv_file, second_csv_file])
        assert len(result) == 3
        assert type(result[0]) is DataRow
        assert set(row.country for row in result) == {"France", "United States"}
