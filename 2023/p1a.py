#!/usr/bin/python3

import sys
import re

RE = re.compile("[^0-9]*([0-9]).*?([0-9]?)[^0-9]*$")

s = 0

for l in sys.stdin.readlines():
    m = RE.match(l)
    s += int(m[1] + (m[2] or m[1]))

print(s)
