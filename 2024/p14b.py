#!/usr/bin/python3

import re

def egcd(a, b):
    r0, r1 = a, b
    s0, s1 = 1, 0
    t0, t1 = 0, 1
    while r1 > 0:
        q = r0 // r1
        r0, r1 = r1, r0 - q * r1
        s0, s1 = s1, s0 - q * s1
        t0, t1 = t1, t0 - q * t1
    return (r0, s0, t0)

ire = re.compile("p=(\\d+),(\\d+) v=(-?\\d+),(-?\\d+)\n")

def sim_num(num):
    counts = [[0] * 101 for x in range(103)]
    for s in state:
        px, py, vx, vy = s
        px = (px + vx * num) % 101
        py = (py + vy * num) % 103
        counts[py][px] += 1
    return counts

with open("p14.txt") as f:
    state = [[int(y) for y in ire.fullmatch(x).groups()] for x in f.readlines()]
    i = 0
    r, s0, t0 = egcd(103, 101)
    mxv, mx = 9999, 0
    myv, my = 9999, 0
    for num in range(103):
        counts = sim_num(num)
        xv = sum(sum(x) for x in (counts[0:20] + counts[83:103]))
        yv = sum(sum(x[0:20])+sum(x[81:101]) for x in counts)
        if xv < mxv:
            mxv = xv
            mx = num
        if yv < myv:
            myv = yv
            my = num
    mul = my - mx
    num = (103 * mul * s0 + mx) % (103 * 101)
    print(num, "\n")
    counts = sim_num(num)
    for line in counts:
        print("".join(chr(x+48) if x else "." for x in line))
    print()
