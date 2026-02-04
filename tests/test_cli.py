from unittest.mock import patch

import pytest

from main import main


class TestCLI:
    def test_main_success(self, first_csv_file, second_csv_file):
        args = [
            "main.py",
            "--files",
            str(first_csv_file),
            str(second_csv_file),
            "--report",
            "average-gdp",
        ]
        with patch("sys.argv", args):
            main()  # does not raise an error

    def test_csv_file_does_not_exist(self):
        args = [
            "main.py",
            "--files",
            "this_file_does_not_exist.csv",
            "--report",
            "average-gdp",
        ]
        with pytest.raises(FileNotFoundError):
            with patch("sys.argv", args):
                main()

    def test_report_does_not_exist(self, first_csv_file):
        args = [
            "main.py",
            "--files",
            str(first_csv_file),
            "--report",
            "this-report-does-not-exist",
        ]
        with pytest.raises(SystemExit):
            with patch("sys.argv", args):
                main()

    def test_files_argument_is_not_provided(self):
        args = [
            "main.py",
            "--report",
            "average-gdp",
        ]
        with pytest.raises(SystemExit):
            with patch("sys.argv", args):
                main()

    def test_report_argument_is_not_provided(self, first_csv_file):
        args = [
            "main.py",
            "--files",
            str(first_csv_file),
        ]
        with pytest.raises(SystemExit):
            with patch("sys.argv", args):
                main()

    def test_unnecessary_argument_is_provided(self, first_csv_file):
        args = [
            "main.py",
            "--files",
            str(first_csv_file),
            "--report",
            "average-gdp",
            "--unnecessary",
        ]
        with pytest.raises(SystemExit):
            with patch("sys.argv", args):
                main()

    def test_tabulate_is_called(self, first_csv_file):
        # serves as an integration test since tabulate is called after everything else
        args = [
            "main.py",
            "--files",
            str(first_csv_file),
            "--report",
            "average-gdp",
        ]

        with patch("reports.tabulate") as mock_tabulate:
            with patch("sys.argv", args):
                main()
                assert mock_tabulate.called, "tabulate was not called"
