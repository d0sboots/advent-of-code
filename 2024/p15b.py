#!/usr/bin/python3

import re

ire = re.compile("p=(\\d+),(\\d+) v=(-?\\d+),(-?\\d+)\n")

def canpush(x, dr):
    ch = state[x[0]][x[1]]
    if ch == ".":
        return True
    if ch == "#":
        return False
    n = (x[0]+dr[0],x[1]+dr[1])
    if ch == "@":
        return canpush(n, dr)
    if ch == "[":
        if dr == (0,1):
            return canpush((n[0],n[1]+1), dr)
        return canpush(n, dr) and canpush((n[0], n[1]+1), dr)
    if ch == "]":
        if dr == (0,-1):
            return canpush((n[0],n[1]-1), dr)
        return canpush(n, dr) and canpush((n[0], n[1]-1), dr)
    raise "Foo!"

def dopush(x, dr):
    ch = state[x[0]][x[1]]
    if ch == "." or ch == "#":
        return
    n = (x[0]+dr[0],x[1]+dr[1])
    if ch == "@":
        dopush(n, dr)
    if ch == "[":
        if dr == (0,1):
            dopush((n[0],n[1]+1), dr)
            state[n[0]][n[1]+1] = "]"
        else:
            dopush(n, dr)
            dopush((n[0], n[1]+1), dr)
            state[n[0]][n[1]+1] = "]"
            state[x[0]][x[1]+1] = "."
    if ch == "]":
        if dr == (0,-1):
            dopush((n[0],n[1]-1), dr)
            state[n[0]][n[1]-1] = "["
        else:
            dopush(n, dr)
            dopush((n[0], n[1]-1), dr)
            state[n[0]][n[1]-1] = "["
            state[x[0]][x[1]-1] = "."
    state[n[0]][n[1]] = ch
    state[x[0]][x[1]] = "."

with open("p15.txt") as f:
    maze, moves = f.read().split("\n\n")
state = [list("".join({"#":"##", "@":"@.", ".":"..", "O":"[]"}[y] for y in x)) for x in maze.split("\n")]
for i, m in enumerate(state):
    if "@" in m:
        pos = (i, m.index("@"))
        break
for line in moves.split("\n"):
    for l in line:
        dr = {"^":(-1,0), "v":(1,0), "<":(0,-1), ">":(0,1)}[l]
        #print(pos, l)
        if canpush(pos, dr):
            dopush(pos, dr)
            pos = (pos[0]+dr[0], pos[1]+dr[1])
        #for line in state:
            #print("".join(line))
count = 0
for i, line in enumerate(state):
    for j, x in enumerate(line):
        if x == "[":
            count += i * 100 + j
print(count)
print(pos)
for line in state:
    print("".join(line))
