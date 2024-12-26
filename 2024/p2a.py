#!/usr/bin/python3

def thing(levels):
    dir = levels[0] < levels[1]
    for i in range(1, len(levels)):
        if dir:
            if not (1 <= levels[i] - levels[i-1] <= 3):
                return 0
        else:
            if not (1 <= levels[i-1] - levels[i] <= 3):
                return 0
    return 1

with open("p2.txt") as f:
    safe = 0
    for x in f.readlines():
        levels = [int(y) for y in x.strip().split()]
        if levels[0] == levels[1]:
            continue
        safe += thing(levels)
    print(safe)
