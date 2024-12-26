#!/usr/bin/python3

dirr = []
for i in range(-1, 2):
    for j in range(-1, 2):
        if i == 0 and j == 0:
            continue
        dirr.append([i, j])

count = 0
with open("p4.txt") as f:
    words = [x.strip() for x in f.readlines()]
    dim = [len(words), len(words[0])]
    for i in range(dim[0]):
        for j in range(dim[1]):
            for dr in dirr:
                lasti = i + dr[0] * 3
                lastj = j + dr[1] * 3
                if lasti < 0 or lasti >= dim[0] or lastj < 0 or lastj >= dim[1]:
                    continue
                if [words[i+dr[0]*x][j+dr[1]*x] for x in range(4)] != ["X","M","A","S"]:
                    continue
                count += 1

print(count)
