#!/usr/bin/python3

def get_score(i, j, h):
    if i < 0 or i >= dim[0] or j < 0 or j >= dim[1]:
        return
    if lines[i][j] != chr(48 + h):
        return
    if h == 9:
        visited.add((i, j))
        return
    h += 1
    get_score(i+1, j, h)
    get_score(i-1, j, h)
    get_score(i, j+1, h)
    get_score(i, j-1, h)

with open("p10.txt") as f:
    lines = [x.strip() for x in f.readlines()]

dim = [len(lines), len(lines[0])]
score = 0
for i in range(dim[0]):
    for j in range(dim[1]):
        visited = set()
        get_score(i, j, 0)
        score += len(visited)
print(score)
