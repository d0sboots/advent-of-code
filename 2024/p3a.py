#!/usr/bin/python3

import re

with open("p3.txt") as f:
    print(sum(int(x[0])*int(x[1]) for x in re.findall("mul[(]([0-9]+),([0-9]+)[)]", f.read())))
