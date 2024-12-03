#!/usr/bin/python
with open("inputs/03.txt") as f:
    puzzle_input = f.read().splitlines()

# It seems like the goal of the program is just to multiply some numbers.
# It does that with instructions like mul(X,Y), where X and Y are each 1-3 digit numbers.
# For instance, mul(44,46) multiplies 44 by 46 to get a result of 2024. Similarly, mul(123,4) would multiply 123 by 4.
# However, because the program's memory has been corrupted, there are also
# many invalid characters that should be ignored, even if they look like part of a mul instruction.

# Sequences like mul(4*, mul(6,9!, ?(12,34), or mul ( 2 , 4 ) do nothing.

# For example, consider the following section of corrupted memory:
# xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))
# Only the four highlighted sections are real mul instructions.
# Adding up the result of each instruction produces 161 (2*4 + 5*5 + 11*8 + 8*5).

# Scan the corrupted memory for uncorrupted mul instructions. What do you get if you add up all of the results of the multiplications?

import re


def part1(puzzle_input: list[str]):
    pattern = re.compile("mul\((\d{1,3}),(\d{1,3})\)")
    return sum([int(x) * int(y) for x, y in pattern.findall("-".join(puzzle_input))])


def part2(puzzle_input: list[str]):
    p_valid = re.compile("do\(\)(.*?)don't\(\)")  # strings with valid instructions
    valid_strings = [
        s for s in p_valid.findall("do()" + "-".join(puzzle_input) + "don't()")
    ]
    pattern = re.compile("mul\((\d{1,3}),(\d{1,3})\)")
    return sum([int(x) * int(y) for x, y in pattern.findall("-".join(valid_strings))])


print(part1(puzzle_input))
print(part2(puzzle_input))
