import re
from typing import TextIO


def main():
    input_data: TextIO = open('input.txt', 'r', encoding='utf-8')
    total: int = 0
    instruction_matches = re.finditer(r'mul\((\d+),(\d+)\)', input_data.read())

    for match in instruction_matches:
        total += int(match.groups()[0]) * int(match.groups()[1])
    print(total)


if __name__ == '__main__':
    main()
