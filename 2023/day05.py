#!/usr/bin/python
from itertools import chain
from multiprocessing import Pool

with open("inputs/05.txt") as f:
    puzzle_input = f.read().splitlines()

stages = [
    "seed",
    "soil",
    "fertilizer",
    "water",
    "light",
    "temperature",
    "humidity",
    "location",
]
steps = [f"{stages[i]}-to-{stages[i+1]}" for i in range(len(stages) - 1)]

almanac: {str: [dict]} = {}
for step_name in steps:
    almanac[step_name] = []
    start = puzzle_input.index(f"{step_name} map:")
    try:
        stop = puzzle_input.index("", start)
    except ValueError:
        stop = None
    for line in puzzle_input[start + 1 : stop]:
        dest_start, src_start, range_len = line.split(" ")
        almanac[step_name].append(
            {
                "dst": range(int(dest_start), int(dest_start) + int(range_len)),
                "src": range(int(src_start), int(src_start) + int(range_len)),
            }
        )
    almanac[step_name].sort(key=lambda e: e["src"].start)


def get_location(seed: int) -> int:
    next_source = seed
    for step in steps:
        for entry in almanac[step]:
            if entry["src"].start <= next_source < entry["src"].stop:
                offset = entry["src"].index(next_source)
                next_source = entry["dst"][offset]
                break
    return next_source


def part1(puzzle_input):
    seeds = map(int, puzzle_input[0].removeprefix("seeds: ").split(" "))
    return min(map(get_location, seeds))


def part2(puzzle_input):
    seed_data = list(map(int, puzzle_input[0].removeprefix("seeds: ").split(" ")))
    # seed_ranges = [range(123456, 234567), range(345678, 456789), ...]
    seed_ranges = sorted(
        map(lambda sr: range(sr[0], sum(sr)), zip(seed_data[0::2], seed_data[1::2])),
        key=lambda r: r.start,
    )
    intervals = [(r, 0) for r in seed_ranges]
    min_loc = float("inf")
    while intervals:
        r, stage = intervals.pop()
        if stage == 7:
            min_loc = min(r.start, min_loc)
            continue

        for entry in almanac[steps[stage]]:
            src: range = entry["src"]
            dst: range = entry["dst"]
            offset = dst.start - src.start
            if r.stop <= src.start or src.stop <= r.start:
                continue
            if r.start < src.start:
                intervals.append((range(r.start, src.start), stage))
                r = range(src.start, r.stop)
            if src.stop < r.stop:
                intervals.append((range(src.stop, r.stop), stage))
                r = range(r.start, src.stop)
            intervals.append((range(r.start + offset, r.stop + offset), stage + 1))
            break
        else:
            intervals.append((r, stage + 1))

    return min_loc


print(part1(puzzle_input))
print(part2(puzzle_input))
