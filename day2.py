# Advent of Code
# Day 2
# @SuddenlyTom

def is_sorted(levels):
    delta = [b - a for a, b in zip(levels[:-1], levels[1:])]
    in_order = all([i > 0 for i in delta]) | all([i < 0 for i in delta])
    step_in_range = all([abs(i) <= 3 for i in delta]) and all([abs(i) >= 1 for i in delta])
    return in_order and step_in_range


def is_passable(levels: list):
    return any(is_sorted(list(levels[:i] + levels[i+1:])) for i in range(len(levels)))

def part1():
    reports = [list(map(int, line.split())) for line in open("inputs/day2.txt").readlines()]
    return sum(map(is_sorted, reports))


def part2():
    reports = [list(map(int, line.split())) for line in open("inputs/day2.txt").readlines()]
    return sum(map(is_passable, reports))

print(f"part 1: {part1()}")
print(f"part 2: {part2()}")