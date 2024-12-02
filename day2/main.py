import re
from typing import TextIO

"""
The levels are either all increasing or all decreasing.
Any two adjacent levels differ by at least one and at most three.
In the example above, the reports can be found safe or unsafe by checking those rules:

7 6 4 2 1: Safe because the levels are all decreasing by 1 or 2.
1 2 7 8 9: Unsafe because 2 7 is an increase of 5.
9 7 6 2 1: Unsafe because 6 2 is a decrease of 4.
1 3 2 4 5: Unsafe because 1 3 is increasing but 3 2 is decreasing.
8 6 4 4 1: Unsafe because 4 4 is neither an increase or a decrease.
1 3 6 7 9: Safe because the levels are all increasing by 1, 2, or 3.
So, in this example, 2 reports are safe.

Analyze the unusual data from the engineers. How many reports are safe?
"""


def main():
    # Read input data
    input_data: TextIO = open('input.txt', 'r', encoding='utf-8')
    # Parse into reports
    reports = parse_reports(input_data)
    # Determine safety of reports
    checked_reports = map(get_report_safety, reports)
    safe_reports = [status for status in checked_reports if status == True]
    print(f'Number of safe reports: {len(safe_reports)}')
    # Lenient safety check
    leniently_checked_reports = map(get_lenient_report_safety, reports)
    lenient_safe_reports = [status for status in leniently_checked_reports if status == True]
    print(f'Number of lenient safe reports: {len(lenient_safe_reports)}')


def parse_reports(data: TextIO) -> list[list[int]]:
    reports: list[list[int]] = []
    for report in data.readlines():
        level_matches = re.finditer(r'\d+', report)
        levels: list[int] = []
        for match in level_matches:
            levels.append(int(match.group()))
        reports.append(levels)

    return reports


def get_report_safety(report: list[int]) -> bool:
    is_safe: bool = True
    prev_ascending: bool | None = None

    for index, level in enumerate(report):
        if index + 1 < len(report):
            delta = level - report[index + 1]
            # Check if delta is between 1 and 3
            if abs(delta) < 1 or abs(delta) > 3:
                is_safe = False

            # Check if levels are only increasing/decreasing
            is_ascending: bool = delta < 0
            if prev_ascending is not None and prev_ascending is not is_ascending:
                is_safe = False
            prev_ascending = is_ascending

    return is_safe


def can_make_safe(report: list[int]) -> bool:
    # Iterate through each index in the report
    for i in range(len(report)):
        # Create a new list excluding the current index
        modified_report = report[:i] + report[i + 1:]
        # Check if the modified report is safe
        if get_report_safety(modified_report):
            return True
    return False


def get_lenient_report_safety(report: list[int]) -> bool:
    return can_make_safe(report)


if __name__ == '__main__':
    main()
