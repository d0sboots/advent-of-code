#!/usr/bin/python3

keys = []
locks = []
count = 0
with open("p25.txt") as f:
    for thing in f.read().split("\n\n"):
        lines = list(thing.strip().split("\n"))
        counts = [sum(x=="#" for x in y)-1 for y in zip(*lines)]
        if lines[0] == "#####":
            locks.append(counts)
        else:
            keys.append(counts)
for k in keys:
    for l in locks:
        for i in range(5):
            if k[i]+l[i] > 5:
                break
        else:
            count += 1
print(count)
