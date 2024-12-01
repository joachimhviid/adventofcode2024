from typing import TextIO
import re


def main():
    input_data: TextIO = open('input.txt', 'r', encoding='utf-8')

    left, right = parse_input_data(input_data)

    total_distance = get_total_distance(left, right)
    print(f'Total distance = {total_distance}')
    similarity_score = get_similarity_score(left, right)
    print(f'Similarity score = {similarity_score}')


# Parse data into lists (left and right)
def parse_input_data(data: TextIO) -> tuple[list[str], list[str]]:
    left: list[str] = []
    right: list[str] = []

    location_matches = re.finditer(r'\d+', data.read(), re.MULTILINE)
    for index, match in enumerate(location_matches):
        if index % 2 == 0:
            left.append(match.group())
        else:
            right.append(match.group())

    return left, right


def get_total_distance(left_locations: list[str], right_locations: list[str]) -> int:
    # Sort lists
    left_locations.sort()
    right_locations.sort()

    # Get the absolute value of l[0...] - r[0...] and collect them in total_distance
    total_distance: int = 0
    for index, location_id in enumerate(left_locations):
        distance: int = abs(int(location_id) - int(right_locations[index]))
        total_distance += distance

    return total_distance


def get_similarity_score(left_locations: list[str], right_locations: list[str]) -> int:
    similarity_score: int = 0
    for location_id in left_locations:
        similarity = int(location_id) * right_locations.count(location_id)
        similarity_score += similarity

    return similarity_score



if __name__ == '__main__':
    main()