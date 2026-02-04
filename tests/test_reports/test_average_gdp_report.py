from reports import AverageGDPReport


class TestAverageGDPReport:
    def test_generate_report_from_one_row(self, germany_2020):
        average_gdp_report = AverageGDPReport()
        report = average_gdp_report.generate_report([germany_2020])
        assert "countries" in report
        assert "average-gdp" in report
        assert report["countries"] == ["Germany"]
        assert report["average-gdp"] == [100]

    def test_generate_report_from_two_rows(self, germany_2020, germany_2021):
        average_gdp_report = AverageGDPReport()
        report = average_gdp_report.generate_report([germany_2020, germany_2021])
        assert "countries" in report
        assert "average-gdp" in report
        assert report["countries"] == ["Germany"]
        assert report["average-gdp"] == [150]

    def test_generate_report_for_multiple_countries(
        self, germany_2020, germany_2021, japan_2020, japan_2021
    ):
        average_gdp_report = AverageGDPReport()
        report = average_gdp_report.generate_report(
            [germany_2020, germany_2021, japan_2020, japan_2021]
        )
        assert "countries" in report
        assert "average-gdp" in report
        assert set(report["countries"]) == {"Germany", "Japan"}
        assert set(report["average-gdp"]) == {150, 300}

    def test_report_is_ordered_by_average_gdp(
        self, germany_2020, germany_2021, japan_2020, japan_2021
    ):
        average_gdp_report = AverageGDPReport()
        report = average_gdp_report.generate_report(
            [germany_2020, germany_2021, japan_2020, japan_2021]
        )
        assert report["countries"] == ["Japan", "Germany"]
        assert report["average-gdp"] == [300, 150]

    def test_generate_report_from_csv_files(self, first_csv_file, second_csv_file):
        average_gdp_report = AverageGDPReport()
        parsed_data = average_gdp_report.parse_csv_files(
            [first_csv_file, second_csv_file]
        )
        report = average_gdp_report.generate_report(parsed_data)
        assert report["countries"] == ["France", "United States"]
        assert report["average-gdp"] == [1500, 1000]
