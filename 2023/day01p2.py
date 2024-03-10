#!/usr/bin/python
# task - get first and last letter from each line, concat into a 2-digit number.
# If there's only one digit in line, duplicate it.
import re

input_file = "inputs/01.txt"
numbers_regex = re.compile(
    r"(?=(one|two|three|four|five|six|seven|eight|nine|zero|\d))"
)
atoi = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "zero": 0,
}

total = 0
with open(input_file) as f:
    for line in f.readlines():
        finds = re.findall(numbers_regex, line)
        left = finds[0] if finds[0] not in atoi.keys() else atoi[finds[0]]
        right = finds[-1] if finds[-1] not in atoi.keys() else atoi[finds[-1]]
        number = int(f"{left}{right}")
        total += number

print(total)  # 54925
