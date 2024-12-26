#!/usr/bin/python3

from collections import deque

with open("p20.txt") as f:
    inp = [x.strip() for x in f.readlines()]
for i, l in enumerate(inp):
    if "S" in l:
        startp = (i, l.index("S"))
    if "E" in l:
        endp = (i, l.index("E"))
dm = (len(inp), len(inp[0]))
dist = [[False] * dm[1] for i in range(dm[0])]
dr = [(1,0), (0,1), (-1,0), (0,-1)]
pos = startp
d = 0
while True:
    dist[pos[0]][pos[1]] = d
    d += 1
    for dirr in dr:
        newp = (pos[0]+dirr[0], pos[1]+dirr[1])
        if dist[newp[0]][newp[1]] is False and inp[newp[0]][newp[1]] != "#":
            pos = newp
            break
    else:
        break
count = 0
for i in range(1, dm[0]-1):
    for j in range(1, dm[1]-1):
        startd = dist[i][j]
        if startd is False:
            continue
        for k in range(-20, 21):
            i2 = i + k
            if i2 < 1 or i2 >= dm[0]-1:
                continue
            ak = abs(k)
            for m in range(ak-20, 21-ak):
                j2 = j + m
                if j2 < 1 or j2 >= dm[1]-1:
                    continue
                endd = dist[i2][j2]
                if endd - startd >= 100 + ak + abs(m):
                    count += 1
print(count)
