# Advent of Code
# Day 3
# @SuddenlyTom

import re

def part1(src) -> int:
    return sum(map(lambda a: eval(a, {'mul':lambda x,y: x*y }), re.findall(r"mul\(\d*,\d*\)", src)))

def part2(src):
    return sum(map(part1, [tup[1] for tup in re.findall(r"(?:\A|(do\(\)))([\s\S]*?)(?:(don't\(\))|\Z)", src)]))

day3 = open("inputs/day3.txt").read()
print(part1(day3))
print(part2(day3))


