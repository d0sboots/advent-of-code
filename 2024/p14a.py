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

q = [0,0,0,0]
with open("p14.txt") as f:
    for x in f.readlines():
        px, py, vx, vy = [int(y) for y in ire.fullmatch(x).groups()]
        px = (px + vx * 100) % 101
        py = (py + vy * 100) % 103
        if px == 50 or py == 51:
            continue
        q[px//51 + 2*(py//52)] += 1
print(q[0] * q[1] * q[2] * q[3])
