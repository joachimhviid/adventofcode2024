from typing import TextIO
import re


def main():
    input_data: TextIO = open('input.txt', 'r', encoding='utf-8')

    # Parse data into lists (left and right)
    left: list[str] = []
    right: list[str] = []

    location_matches = re.finditer(r'\d+', input_data.read(), re.MULTILINE)
    for index, match in enumerate(location_matches):
        if index % 2 == 0:
            left.append(match.group())
        else:
            right.append(match.group())

    # Sort lists
    left.sort()
    right.sort()

    # Get the absolute value of l[0...] - r[0...] and collect them in total_distance
    total_distance: int = 0
    for index, location_id in enumerate(left):
        distance: int = abs(int(location_id) - int(right[index]))
        total_distance += distance

    print(total_distance)



if __name__ == '__main__':
    main()