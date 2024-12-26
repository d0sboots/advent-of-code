#!/usr/bin/python3

from collections import defaultdict
import re

conn_re = re.compile("(...) ([A-Z]+) (...) -> (...)")

with open("p24.txt") as f:
    inp = list(f.read().split("\n\n"))
conns = dict([((m := conn_re.fullmatch(x))[4], (m[2], m[1], m[3])) for x in inp[1].strip().split("\n")])
by_inp = defaultdict(list)
for k, v in conns.items():
    by_inp[v[1]].append(k)
    by_inp[v[2]].append(k)
zn = sum(1 if x[0] == "z" else 0 for x in conns.keys())
for k, v in conns.items():
    if v[0] == "XOR":
        if v[1][0] == "x" or v[2][0] == "x":
            pass
        else:
            if k[0] != "z":
                print("badx: " + k)
            i0 = conns[v[1]]
            i1 = conns[v[2]]
            if "AND" == i0[0] and i0[1] != "x00" and i0[2] != "x00":
                print("badxx: " + v[1])
            if "AND" == i1[0] and i1[1] != "x00" and i1[2] != "x00":
                print("badxx: " + v[2])
    if v[0] == "AND":
        if v[1] != "x00" and v[2] != "x00":
            if k not in by_inp:
                print("bada " + k)
            elif conns[by_inp[k][0]][0] != "OR":
                print("bada " + k)
        if v[1][0] == "x" or v[2][0] == "x":
            pass
        else:
            i0 = conns[v[1]]
            i1 = conns[v[2]]
            if "AND" == i0[0] and i0[1] != "x00" and i0[2] != "x00":
                print("badaa: " + v[1])
            if "AND" == i1[0] and i1[1] != "x00" and i1[2] != "x00":
                print("badaa: " + v[2])
    if v[0] == "OR":
        if conns[v[1]][0] != "AND":
            print("bado: " + v[1])
        if conns[v[2]][0] != "AND":
            print("bado: " + v[2])

