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

ire = re.compile("X\+(\d+), Y\+(\d+).*X\+(\d+), Y\+(\d+).*X=(\d+), Y=(\d+)",
                 re.DOTALL)

count = 0
with open("p13.txt") as f:
    for x in f.read().split("\n\n"):
        ax, ay, bx, by, px, py = [int(y) for y in ire.search(x).groups()]
        px += 10000000000000
        py += 10000000000000
        gcd, xa, xb = egcd(ax, bx)
        if px % gcd:
            continue
        basea = xa * (px // gcd)
        baseb = xb * (px // gcd)
        basey = basea * ay + baseb * by
        diffy = (ax // gcd) * by - ay * (bx // gcd)
        if (basey - py) % diffy:
            continue
        adj = (basey - py) // diffy
        basea += (bx // gcd) * adj
        baseb -= (ax // gcd) * adj
        if basea < 0 or baseb < 0:
            continue
        count += basea * 3 + baseb
print(count)
