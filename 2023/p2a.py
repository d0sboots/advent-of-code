#!/usr/bin/python3

import sys
import re

RE1 = re.compile("Game ([0-9]+):(.*)")
RE2 = re.compile(" ?([0-9]+) ([a-z]*)")

limits = {"red": 12, "green": 13, "blue": 14}

def do_cubes(parts):
    for cubes in parts.split(";"):
        for cube in cubes.split(","):
            m = RE2.match(cube)
            if limits[m[2]] < int(m[1]):
                return False
    return True

s = 0

for l in sys.stdin.readlines():
    l = l.strip()
    m = RE1.match(l)
    gid = int(m[1])
    if do_cubes(m[2]):
        s += gid

print(s)
