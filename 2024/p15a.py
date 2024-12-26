#!/usr/bin/python3

import re

ire = re.compile("p=(\\d+),(\\d+) v=(-?\\d+),(-?\\d+)\n")

with open("p15.txt") as f:
    maze, moves = f.read().split("\n\n")
state = [list(x) for x in maze.split("\n")]
for i, m in enumerate(maze.split("\n")):
    if "@" in m:
        pos = (m.index("@"), i)
        break
for line in moves.split("\n"):
    for l in line:
        dr = {"^":(-1,0), "v":(1,0), "<":(0,-1), ">":(0,1)}[l]
        p1 = (pos[0]+dr[0], pos[1]+dr[1])
        x = p1
        while state[x[0]][x[1]] == "O":
            x = (x[0]+dr[0], x[1]+dr[1])
        if state[x[0]][x[1]] == ".":
            state[x[0]][x[1]] = "O"
            state[pos[0]][pos[1]] = "."
            pos = p1
            state[pos[0]][pos[1]] = "@"
        #print(pos, l)
        #for line in state:
            #print("".join(line))
count = 0
for i, line in enumerate(state):
    for j, x in enumerate(line):
        if x == "O":
            count += i * 100 + j
print(count)
print(pos)
for line in state:
    print("".join(line))
