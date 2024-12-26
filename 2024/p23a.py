#!/usr/bin/python3

from collections import defaultdict

count = 0
with open("p23.txt") as f:
    conns = [tuple(x.strip().split("-")) for x in f.readlines()]
    for i in range(len(conns)):
        conns.append((conns[i][1], conns[i][0]))
    conn_set = set(conns)
    conn_map = defaultdict(list)
    for a in conns:
        conn_map[a[0]].append(a[1])
    for a in conns:
        tf = a[0][0] == "t" or a[1][0] == "t"
        for b in conn_map[a[1]]:
            if (tf or b[0] == "t") and (b, a[0]) in conn_set:
                count += 1
print(count//6)
