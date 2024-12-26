#!/usr/bin/python3

import sys
import re

prev_parts = []
s = 0

symbols = []

data = sys.stdin.readlines()
for l in data:
    symbols.append({})
    row = symbols[-1]
    for i, c in enumerate(l):
        if c >= "0" and c <= "9" or c == "." or c == "\n":
            continue
        row[i] = c
symbols.append({})  # Extra row handles negative indexing
for y, l in enumerate(data):
    n = 0
    part = False
    for x, c in enumerate(l):
        if c >= "0" and c <= "9":
            n = 10 * n + ord(c) - 48
            for yy in range(y - 1, y + 2):
                row = symbols[yy]
                # No symbols in first/last column, so we can get lazy
                for xx in range(x - 1, x + 2):
                    if xx in row:
                        part = True
            continue
        if n != 0:
            if part:
                s += n
            n = 0
            part = False

print(s)
