import argparse
from pathlib import Path

from reports import AverageGDPReport

REPORTS = {
    "average-gdp": AverageGDPReport,
}


def parse_arguments():
    parser = argparse.ArgumentParser(description="Generate reports from CSV-files")
    parser.add_argument(
        "--files", required=True, nargs="+", help="One or more CSV-files to process"
    )
    parser.add_argument(
        "--report",
        required=True,
        choices=REPORTS.keys(),
        help=f"Select a report type: {', '.join(REPORTS.keys())}",
    )
    return parser.parse_args()


def main():
    args = parse_arguments()
    csv_files = [Path(file) for file in args.files]
    report = REPORTS[args.report]()
    parsed_data = report.parse_csv_files(csv_files)
    generated_report = report.generate_report(parsed_data)
    report.display_report(generated_report)


if __name__ == "__main__":
    main()
