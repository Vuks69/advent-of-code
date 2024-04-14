#!/usr/bin/python
with open("inputs/09.txt") as f:
    puzzle_input = f.read().splitlines()


def check_nonzero(seq: [int]) -> bool:
    for e in seq:
        if e != 0:
            return True
    return False


def predict_forwards(seq: [int]) -> [int]:
    mask = [0] + seq[:-1]
    next_seq = [a - b for a, b in zip(seq, mask)][1:]
    if check_nonzero(next_seq):
        # need to go deeper
        # return this level + sum of last elements of seq and next_seq
        return seq + [seq[-1] + predict_forwards(next_seq)[-1]]
    else:
        # this is the final level
        # return final level extended by
        # its last element (+ 0 from next level)
        return seq + [seq[-1]]

def extrapolate_backwards(seq: [int]) -> [int]:
    mask = [0] + seq[:-1]
    next_seq = [a - b for a, b in zip(seq, mask)][1:]
    if check_nonzero(next_seq):
        # return final level prepended by
        # its first element minus first element of next extrapolation
        return [seq[0] - extrapolate_backwards(next_seq)[0]] + seq
    else:
        # this is the final level
        # return final level prepended by
        # its first element (- 0 from next level)
        return [seq[0]] + seq


def part1(puzzle_input):
    sequences = [map(int, line.split()) for line in puzzle_input]
    return sum([predict_forwards(list(seq))[-1] for seq in sequences])


def part2(puzzle_input):
    sequences = [map(int, line.split()) for line in puzzle_input]
    return sum([extrapolate_backwards(list(seq))[0] for seq in sequences])
    pass


print(part1(puzzle_input))
print(part2(puzzle_input))
