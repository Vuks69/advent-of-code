#!/usr/bin/python
import re
from itertools import chain
from multiprocessing import Pool

with open("inputs/05.txt") as f:
    puzzle_input = f.read().splitlines()

variables = [
    "seed",
    "soil",
    "fertilizer",
    "water",
    "light",
    "temperature",
    "humidity",
    "location",
]
steps = [f"{variables[i]}-to-{variables[i+1]}" for i in range(len(variables) - 1)]

almanac = {}
for step_name in steps:
    almanac[step_name] = []
    start = puzzle_input.index(f"{step_name} map:")
    try:
        stop = puzzle_input.index("", start)
    except ValueError:
        stop = None
    for line in puzzle_input[start + 1 : stop]:
        range_dest, range_src, range_len = line.split(" ")
        almanac[step_name].append(
            {
                "dst": int(range_dest),
                "src": int(range_src),
                "len": int(range_len),
            }
        )


def get_destination(step_name: str, source: int) -> int:
    for entry in almanac[step_name]:
        if entry["src"] <= source <= entry["src"] + entry["len"]:
            offset = source - entry["src"]
            return entry["dst"] + offset
    return source


def get_location(seed: int) -> int:
    next_source = seed
    for step in steps:
        next_source = get_destination(step, next_source)
    return next_source


def part1(puzzle_input):
    seeds = map(int, puzzle_input[0].removeprefix("seeds: ").split(" "))
    return min(map(get_location, seeds))


def part2(puzzle_input):
    seed_data = list(map(int, puzzle_input[0].removeprefix("seeds: ").split(" ")))

    # seed_ranges = [range(123456, 234567), range(345678, 456789), ...]
    seed_ranges = map(
        lambda sr: range(sr[0], sum(sr)), zip(seed_data[0::2], seed_data[1::2])
    )

    # seeds ~= [1234567, 1234568, ...] - not evaluated to memory, but seeds.__next__() gives next number,
    # which is what map and Pool.map care about (Iterable objects).
    seeds = chain.from_iterable(seed_ranges)

    # Pool() by default takes os.cpu_count() workers.
    with Pool() as pool:
        # WARNING: do not run without limiting RAM accessible to the main process, eg:
        # systemd-run --scope -p MemoryMax=1G --user ./day05.py
        # Otherwise you risk locking the system down and have to forcibly power it off.
        results = pool.map(get_location, seeds)

    # regular map works as expected - pretty much no impact on memory,
    # but only takes one cpu at a time
    # results = map(get_location, seeds)
    return min(results)


print(part1(puzzle_input))
print(part2(puzzle_input))
