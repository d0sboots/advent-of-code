#!/usr/bin/python3

from collections import deque

with open("p18.txt") as f:
    moves = [tuple(int(y) for y in x.strip().split(",")) for x in f.readlines() ]
dm = (71 + 2, 71 + 2)
board = [[99999] * dm[0] for x in range(dm[1])]
for i in range(dm[1]):
    board[i][0] = False
    board[i][-1] = False
for i in range(dm[0]):
    board[0][i] = False
    board[-1][i] = False
for m in moves[:1024]:
    print(m)
    board[m[1]+1][m[0]+1] = False
q = deque()
goal = (dm[0]-2, dm[1]-2)
q.append((1,1,0))
while len(q):
    x,y,c = q.popleft()
    sq = board[y][x]
    if sq == False or sq <= c:
        continue
    board[y][x] = c
    if (x,y) == goal:
        break
    q.append((x,y+1,c+1))
    q.append((x,y-1,c+1))
    q.append((x+1,y,c+1))
    q.append((x-1,y,c+1))
print(board[dm[1]-2][dm[0]-2])
