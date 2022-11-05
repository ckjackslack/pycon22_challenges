import os
import re
from pathlib import Path

CUR_DIR = os.path.abspath(os.path.dirname(__file__))
INPUT_PATH = Path(CUR_DIR) / ".." / "input" / "sample_input.txt"

def get_lines():
    with open(INPUT_PATH) as f:
        for line in f:
            yield line

def main():
    counter = 0
    for line in get_lines():
        # your code goes here, feel free to edit anything here
        # counting all antipattern
        anti_pattern = len(re.findall(r'^PUMPKIN|PUMPKIN$|[PUMKIN]PUMPKIN|PUMPKIN[PUMKIN]', line))
        # counting the pattern
        pattern = len(re.findall(r'PUMPKIN|NIKPUMP', line))
        line_count = pattern - anti_pattern
        print(line, end=f' PUMPKINS FOUND: {line_count} ')
        counter += line_count

    print(f'\nTOTAL COUNT = {counter}')


if __name__ == '__main__':
    main()