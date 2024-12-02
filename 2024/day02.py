#!/usr/bin/python
import copy

with open("inputs/02.txt") as f:
    puzzle_input = f.read().splitlines()

# a report only counts as safe if both of the following are true:
# Any two adjacent levels differ by at least one and at most three.
# The levels are either all increasing or all decreasing.
# How many reports are safe?

# example report
# 77 79 82 85 87

sanitycheck = [
    [7, 6, 4, 2, 1],  # Safe without removing any level.
    [1, 2, 7, 8, 9],  # Unsafe regardless of which level is removed.
    [9, 7, 6, 2, 1],  # Unsafe regardless of which level is removed.
    [1, 3, 2, 4, 5],  # Safe by removing the second level, 3.
    [8, 6, 4, 4, 1],  # Safe by removing the third level, 4.
    [1, 3, 6, 7, 9],  # Safe without removing any level.
]


def check_safety(report):
    return check_ordering(report) and check_levels(report)


def check_ordering(report):
    sorted_report = sorted(report)
    return sorted_report == report or sorted_report == list(reversed(report))


def check_levels(report):
    for i in range(len(report) - 1):
        # Any two adjacent levels differ by at least one and at most three.
        difference = abs(report[i] - report[i + 1])
        if not 1 <= difference <= 3:
            return False
    return True


def correctable(report):
    for i in range(len(report)):
        cr = copy.deepcopy(report)
        # self note: list.remove deletes FIRST OCCURENCE ONLY
        cr.pop(i)
        if check_safety(cr):
            return True
    return False


def part1(puzzle_input):
    reports = [[int(level) for level in line.split()] for line in puzzle_input]
    safe = 0
    for report in reports:
        if check_safety(report):
            safe += 1
    return safe


def part2(puzzle_input):
    reports = [[int(level) for level in line.split()] for line in puzzle_input]
    safe_reports = [report for report in reports if check_safety(report)]
    unsafe_reports = [report for report in reports if report not in safe_reports]
    corrected_reports = [report for report in unsafe_reports if correctable(report)]
    return len(safe_reports) + len(corrected_reports)


print(part1(puzzle_input))
print(part2(puzzle_input))
