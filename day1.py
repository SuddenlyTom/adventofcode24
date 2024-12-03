# Advent of Code
# Day 1
# @SuddenlyTom

def part1():
    left = []
    right = []
    with open("inputs/day1.txt") as inputs:
        for entry in inputs.readlines():
            a,b = entry.split("   ")
            left.append(int(a))
            right.append(int(b.strip()))

    left = sorted(left)
    right = sorted(right)
    difference = sum([abs(left[i] - right[i]) for i in range(len(left))])
    print(difference)
    return difference

def part2():
    left = []
    right = dict()
    with open("inputs/day1.txt") as inputs:
        for entry in inputs.readlines():
            a,b = entry.split("   ")
            left.append(int(a))

            b = int(b.strip())
            if b not in right:
                right[b] = 0
            right[b] = right[b] + 1

    similarity = sum([l * right[l] if l in right else 0 for l in left])
    print(similarity)
    return similarity

part1()
part2()