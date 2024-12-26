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
while len(heap):
    cost, dr, i, j = heapq.heappop(heap)
    if score[dr][i][j] <= cost:
        continue
    if maze[i][j] == "E":
        print(cost)
        break
    score[dr][i][j] = cost
    heapq.heappush(heap, (cost+1000, (dr+1)%4, i, j))
    heapq.heappush(heap, (cost+1000, (dr-1)%4, i, j))
    drr = dirs[dr]
    ni = i + drr[0]
    nj = j + drr[1]
    if maze[ni][nj] != "#":
        heapq.heappush(heap, (cost+1, dr, ni, nj))
