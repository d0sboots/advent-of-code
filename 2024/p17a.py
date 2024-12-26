#!/usr/bin/python3

import re

def combo():
    match prog[ip+1]:
        case w if w < 4:
            return w
        case 4:
            return A
        case 5:
            return B
        case 6:
            return C
    throw("Bad combo arg at " + ip)

with open("p17.txt") as f:
    inp = [x.strip() for x in f.readlines()]
A, B, C = [int(x.split()[-1]) for x in inp[:3]]
prog = [int(x) for x in inp[-1].split()[-1].split(",")]
ip = 0
out = []
while ip < len(prog):
    inst = prog[ip]
    match inst:
        case 0 | 6 | 7:
            res = A >> combo()
            if inst == 0:
                A = res
            elif inst == 6:
                B = res
            else:
                C = res
        case 1 | 4:
            B ^= C if inst == 4 else prog[ip+1]
        case 2:
            B = combo() % 8
        case 3:
            if A:
                ip = prog[ip+1] - 2
        case 5:
            out.append(combo() % 8)
    ip += 2
print(",".join(str(x) for x in out))
