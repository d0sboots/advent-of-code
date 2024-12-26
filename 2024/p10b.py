#!/usr/bin/python3

def get_score(i, j, h):
    if i < 0 or i >= dim[0] or j < 0 or j >= dim[1]:
        return 0
    if lines[i][j] != chr(48 + h):
        return 0
    if h == 9:
        return 1
    h += 1
    return (get_score(i+1, j, h) +
            get_score(i-1, j, h) +
            get_score(i, j+1, h) +
            get_score(i, j-1, h))

with open("p10.txt") as f:
    lines = [x.strip() for x in f.readlines()]

dim = [len(lines), len(lines[0])]
score = 0
for i in range(dim[0]):
    for j in range(dim[1]):
        visited = set()
        score += get_score(i, j, 0)
print(score)
