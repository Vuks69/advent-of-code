#!/usr/bin/python
import numpy as np
from numpy.polynomial import Polynomial as Poly

with open("inputs/06.txt") as f:
    puzzle_input = f.read().splitlines()


def part1(puzzle_input):
    times = puzzle_input[0].split()[1:]
    distances = puzzle_input[1].split()[1:]
    records = list(zip(map(int, times), map(int, distances)))
    ways = []
    for time, to_beat in records:
        eq = Poly((-to_beat, time, -1))
        x, y = eq.roots()
        ways.append(int(np.floor(y) - np.floor(x)))
    return np.prod(ways, dtype=int)


# x + y = t -> y = t - x
# x * y > d -> x * (t - x) > d -> -x2 + tx - d > 0
# ret = t - 2x
# how to limit initial x?
# t and d are known - simple equation, find roots and calculate distance between them
# numpy?


def part2(puzzle_input):
    times = puzzle_input[0].split()[1:]
    time = int("".join(times))
    distances = puzzle_input[1].split()[1:]
    to_beat = int("".join(distances))
    eq = Poly((-to_beat, time, -1))
    x, y = eq.roots()
    return int(np.floor(y) - np.floor(x))


print(part1(puzzle_input))
print(part2(puzzle_input))
