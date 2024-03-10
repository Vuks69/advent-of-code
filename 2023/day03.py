#!/usr/bin/python
import re


def prepare_schematics(lines):
    schematics = ["." * (len(lines[0]) + 2)]
    for line in lines:
        schematics.append(f".{line}.")
    schematics.append(schematics[0])
    return schematics


with open("inputs/02.txt") as f:
    puzzle_input = prepare_schematics(f.read().split("\n"))


def part1(puzzle_input):
    total = 0
    for index in range(1, len(puzzle_input)):
        for reiter in re.finditer(r"\d+", puzzle_input[index]):
            for x in range(reiter.start() - 1, reiter.end() + 1):
                if (
                    puzzle_input[index - 1][x] not in "1234567890."
                    or puzzle_input[index][x] not in "1234567890."
                    or puzzle_input[index + 1][x] not in "1234567890."
                ):
                    total += int(reiter.group())
                    break
    return total


def part2(puzzle_input):
    class gearPos:
        x: int
        y: int

        def __init__(self, x, y):
            self.x = x
            self.y = y

        def __eq__(self, gear):
            return self.x == gear.x and self.y == gear.y

    gear_positions: [gearPos] = []
    for index in range(1, len(puzzle_input)):
        for reiter in re.finditer(r"\*", puzzle_input[index]):
            gear_positions.append(gearPos(reiter.start(), index))

    total = 0
    for gear in gear_positions:
        ratios: [int] = []
        for linenum in [gear.y - 1, gear.y, gear.y + 1]:
            for reiter in re.finditer(r"\d+", puzzle_input[linenum]):
                # if number is within 1 block from gear, it applies
                if gear.x in range(reiter.start() - 1, reiter.end() + 1):
                    ratios.append(int(reiter.group()))
        if len(ratios) == 2:
            total += ratios[0] * ratios[1]
    return total


print(part1(puzzle_input))
print(part2(puzzle_input))
