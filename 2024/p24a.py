#!/usr/bin/python3

from collections import defaultdict
import re

conn_re = re.compile("(...) ([A-Z]+) (...) -> (...)")

def eval(name):
    v = values.get(name)
    if v is not None:
        return v
    rule = conns[name]
    p1 = eval(rule[1])
    p2 = eval(rule[2])
    if rule[0] == "AND":
        v = p1 & p2
    elif rule[0] == "OR":
        v = p1 | p2
    elif rule[0] == "XOR":
        v = p1 ^ p2
    values[name] = v
    return v

count = 0
with open("p24.txt") as f:
    inp = list(f.read().split("\n\n"))
init = [((sp := list(x.split(": ")))[0], int(sp[1])) for x in inp[0].split("\n")]
conns = dict([((m := conn_re.fullmatch(x))[4], (m[2], m[1], m[3])) for x in inp[1].strip().split("\n")])
values = dict(init)
zn = sum(1 if x[0] == "z" else 0 for x in conns.keys())
for num in range(zn):
    v = eval(f'z{num:02d}')
    count |= v << num
print(count)
