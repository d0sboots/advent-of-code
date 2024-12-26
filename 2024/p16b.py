#!/usr/bin/python3

import heapq

with open("p16.txt") as f:
    maze = [x.strip() for x in f.readlines()]
dim = (len(maze), len(maze[0]))
goal = (1, dim[1] - 2)
start = (0, 0, dim[0] - 2, 1)
dirs = [(0,1), (1,0), (0,-1), (-1,0)]

score = [[[999999999] * dim[1] for x in range(dim[0])] for y in range(4)]
heap = [start]
best_pos = False
while len(heap):
    cost, dr, i, j = heapq.heappop(heap)
    if score[dr][i][j] <= cost:
        continue
    score[dr][i][j] = cost
    if best_pos and cost > best_pos[0]:
        break
    if maze[i][j] == "E":
        best_pos = (cost, dr, i, j)
    heapq.heappush(heap, (cost+1000, (dr+1)%4, i, j))
    heapq.heappush(heap, (cost+1000, (dr-1)%4, i, j))
    drr = dirs[dr]
    ni = i + drr[0]
    nj = j + drr[1]
    if maze[ni][nj] != "#":
        heapq.heappush(heap, (cost+1, dr, ni, nj))

stack = [best_pos]
seen = [[False] * dim[1] for x in range(dim[0])]
while len(stack):
    cost, dr, i, j = stack.pop()
    seen[i][j] = True
    c1 = score[(dr+1)%4][i][j]
    if c1 == cost - 1000:
        stack.append((cost-1000, (dr+1)%4, i, j))
    c2 = score[(dr-1)%4][i][j]
    if c2 == cost - 1000:
        stack.append((cost-1000, (dr-1)%4, i, j))
    drr = dirs[dr]
    ni = i - drr[0]
    nj = j - drr[1]
    c3 = score[dr][ni][nj]
    if c3 == cost - 1:
        stack.append((cost-1, dr, ni, nj))
print(sum(sum(x) for x in seen))
