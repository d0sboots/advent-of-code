#!/usr/bin/python3

import sys
import re

RE1 = re.compile("Game ([0-9]+):(.*)")
RE2 = re.compile(" ?([0-9]+) ([a-z]*)")

def do_cubes(parts):
    mins = {"red": 0, "green": 0, "blue": 0}
    for cubes in parts.split(";"):
        for cube in cubes.split(","):
            m = RE2.match(cube)
            if mins[m[2]] < int(m[1]):
                mins[m[2]] = int(m[1])
    return mins["red"] * mins["green"] * mins["blue"]

s = 0

for l in sys.stdin.readlines():
    l = l.strip()
    m = RE1.match(l)
    s += do_cubes(m[2])

print(s)
