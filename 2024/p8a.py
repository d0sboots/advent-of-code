#!/usr/bin/python3

count = 0
pos = {}
dimi, dimj = 0, 0
with open("p8.txt") as f:
    for i, line in enumerate(f.readlines()):
        for j, char in enumerate(line.strip()):
            if char == ".":
                continue
            arr = pos.get(char)
            if not arr:
                arr = []
                pos[char] = arr
            arr.append((i, j))
        dimj = j + 1
    dimi = i + 1
hit = [[False] * dimj for x in range(dimi)]
for arr in pos.values():
    for i, p1 in enumerate(arr):
        for p2 in arr[i+1:]:
            p3 = (2*p1[0] - p2[0], 2*p1[1] - p2[1])
            p4 = (2*p2[0] - p1[0], 2*p2[1] - p1[1])
            if p3[0] >= 0 and p3[0] < dimi and p3[1] >= 0 and p3[1] < dimj:
                hit[p3[0]][p3[1]] = True
            if p4[0] >= 0 and p4[0] < dimi and p4[1] >= 0 and p4[1] < dimj:
                hit[p4[0]][p4[1]] = True
print("\n".join("".join("X" if x else " " for x in y) for y in hit))
print(sum(sum(x) for x in hit))