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
    inp = list(f.readlines())[-1].strip()
prog = [int(x) for x in inp.split()[-1].split(",")]
i = 0
while True:
    ip = 0
    out = []
    A,B,C = i,0,0
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
    if out == prog[-len(out):]:
        if len(out) == len(prog):
            break
        i <<= 3
    else:
        while (i & 7) == 7:
            i >>= 3
            if not i:
                raise Exception("Unsolvable!")
        i += 1

print(i)

#Program: 2,4,1,3,7,5,0,3,1,5,4,1,5,5,3,0
#bst A  b = a%8
#bxl 3  b ^= 3
#cdv B  c = a >> b
#adv 3  a = a >> 3
#bxl 5  b ^= 5
#bxc 1  b ^= c
#out 5  out b
#jnz 0

