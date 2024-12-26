#!/usr/bin/python3

def expand(i, j):
    global area, per
    if seen[i][j]:
        return
    seen[i][j] = True
    area += 1
    for o in [(-1,0), (1,0), (0,-1), (0,1)]:
        ni = i + o[0]
        nj = j + o[1]
        if ni < 0 or nj < 0 or ni >= dims[0] or nj >= dims[1] or inp[i][j] != inp[ni][nj]:
            per += 1
            continue
        expand(ni, nj)

with open("p12.txt") as f:
    inp = [x.strip() for x in f.readlines()]

dims = [len(inp), len(inp[0])]
seen = [[False] * dims[1] for x in range(dims[0])]
price = 0
for i in range(dims[0]):
    for j in range(dims[1]):
        if seen[i][j]:
            continue
        area = 0
        per = 0
        expand(i, j)
        price += area * per

print(price)
