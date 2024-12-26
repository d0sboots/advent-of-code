#!/usr/bin/python3

from collections import deque

with open("p19.txt") as f:
    inp = list(f.readlines())
stripes = inp[0].strip().split(", ")

maxl = max(len(x) for x in stripes)
by_size = [[] for x in range(maxl+1)]
for s in stripes:
    by_size[len(s)].append(s)

count = 0
for desired in inp[2:]:
    desired = desired.strip()
    reached = [0] * (len(desired) + 1)
    reached[0] = 1
    for i in range(1, len(desired) + 1):
        for j in range(1, min(i, maxl) + 1):
            if not reached[i-j]:
                continue
            if desired[i-j:i] in by_size[j]:
                reached[i] += reached[i-j]
                continue
    count += reached[-1]
print(count)
