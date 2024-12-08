import re
from typing import TextIO


def main():
    input_data: TextIO = open('input.txt', 'r', encoding='utf-8')
    total: int = 0

    enabled_instruction_matches = re.finditer(r'(^|do\(\))(.|\s)*?(don\'t\(\)|$)', input_data.read())
    for enabled_match in enabled_instruction_matches:
        instruction_matches = re.finditer(r'mul\((\d+),(\d+)\)', enabled_match.group())

        for match in instruction_matches:
            total += int(match.groups()[0]) * int(match.groups()[1])

    print(total)


if __name__ == '__main__':
    main()
