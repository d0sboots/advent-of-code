#!/usr/bin/python3

import sys
import re

RE = re.compile(".*?([0-9]|one|two|three|four|five|six|seven|eight|nine)")
RE2 = re.compile(".*?([0-9]|eno|owt|eerht|ruof|evif|xis|neves|thgie|enin)")

s = 0
MAP = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}
for k, v in list(MAP.items()):
    MAP[k[::-1]] = v
    MAP[str(v)] = v

for l in sys.stdin.readlines():
    l = l.strip()
    m1 = RE.match(l)
    m2 = RE2.match(l[::-1])
    s += int(MAP[m1[1]] + MAP[m2[1]])

print(s)
