#!/usr/bin/python3

with open("p1a.txt") as f:
    inp = [[int(y) for y in x.strip().split()] for x in f.readlines()]
l1, l2 = [sorted(x) for x in zip(*inp)]
print(sum(abs(l1[x] - l2[x]) for x in range(len(l1))))
