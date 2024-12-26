#!/usr/bin/python3

dirr = [[1,1],[1,-1],[-1,1],[-1,-1]]

count = 0
with open("p4.txt") as f:
    words = [x.strip() for x in f.readlines()]
    dim = [len(words), len(words[0])]
    for i in range(1, dim[0] - 1):
        for j in range(1, dim[1] - 1):
            for dr1 in dirr:
                if [words[i+dr1[0]*x][j+dr1[1]*x] for x in range(-1, 2)] != ["M","A","S"]:
                    continue
                for dr2 in dirr:
                    if dr1 == dr2:
                        continue
                    if [words[i+dr2[0]*x][j+dr2[1]*x] for x in range(-1, 2)] != ["M","A","S"]:
                        continue
                    count += 1

print(count//2)
