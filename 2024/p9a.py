#!/usr/bin/python3

from heapq import *

with open("p9.txt") as f:
    line = f.read().strip()

spots = []
pos = []
space = []
heaps = [[] for x in range(10)]
i = 0
checksum = 0
while True:
    if i == 0:
        pos.append(0)
    else:
        pos.append(pos[-1] + spots[-1] + space[-1])
    spots.append(ord(line[i]) - ord('0'))
    if i + 1 >= len(line):
        break
    space.append(ord(line[i+1]) - ord('0'))
    heaps[space[-1]].append(pos[-1] + spots[-1])
    i += 2
for i in range(10):
    heapify(heaps[i])
for i in range(len(pos) - 1, -1, -1):
    sz, ps = spots[i], pos[i]
    mn = 999999999
    mj = -1
    for j in range(sz, 10):
        if len(heaps[j]) and mn > heaps[j][0]:
            mn = heaps[j][0]
            mj = j
    if mn < ps:
        heappop(heaps[mj])
        pos[i] = mn
        new_sz = mj - sz
        if new_sz:
            heappush(heaps[new_sz], mn + sz)
for i, ps in enumerate(pos):
    sz = spots[i]
    checksum += i * sz * (2 * ps + sz - 1) // 2
print(checksum)
