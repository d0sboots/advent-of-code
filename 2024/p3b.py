#!/usr/bin/python3

import re

with open("p3.txt") as f:
    enabled = True
    summ = 0
    for x in re.findall("mul[(]([0-9]+),([0-9]+)[)]|(do|don't)[(][)]", f.read()):
        if x[2]:
            enabled = x[2] == "do"
            continue
        if not enabled:
            continue
        summ += int(x[0]) * int(x[1])
    print(summ)
