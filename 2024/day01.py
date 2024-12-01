#!/usr/bin/python
with open("inputs/01.txt") as f:
    puzzle_input = f.read().splitlines()


def part1(puzzle_input):
    puzzle_input = [i.split() for i in puzzle_input]
    llist = sorted([int(lval) for lval, _ in puzzle_input])
    rlist = sorted([int(rval) for _, rval in puzzle_input])
    return sum([abs(l - r) for l, r in zip(llist, rlist)])


def part2(puzzle_input):
    puzzle_input = [i.split() for i in puzzle_input]
    llist = sorted([int(lval) for lval, _ in puzzle_input])
    rlist = sorted([int(rval) for _, rval in puzzle_input])
    return sum([i * rlist.count(i) for i in llist])


print(part1(puzzle_input))
print(part2(puzzle_input))
