#!/usr/bin/python3

def test_wall(i, j, ni, nj):
    return ni < 0 or nj < 0 or ni >= dims[0] or nj >= dims[1] or inp[i][j] != inp[ni][nj]

dirs = [(-1,0), (0,1), (1,0), (0,-1)]

def expand(i, j):
    global area, per
    if seen[i][j]:
        return
    seen[i][j] = True
    area += 1
    tests = [test_wall(i,j,i+x[0],j+x[1]) for x in dirs]
    for k, tr in enumerate(dirs):
        if tests[k]:
            if not tests[k-1]:
                ni = i+dirs[k-1][0]
                nj = j+dirs[k-1][1]
                if test_wall(ni, nj, ni+tr[0], nj+tr[1]):
                    continue
            per += 1
            continue
        else:
            expand(i+tr[0], j+tr[1])

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
