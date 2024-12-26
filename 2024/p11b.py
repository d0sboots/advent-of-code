#!/usr/bin/python3

from collections import defaultdict

with open("p11.txt") as f:
    nums = [int(x) for x in f.read().strip().split()]

count = defaultdict(int)
mapp = defaultdict(list)
for n in nums:
    count[n] += 1
for i in range(75):
    n2 = defaultdict(int)
    for n, v in count.items():
        mv = mapp[n]
        if not len(mv):
            if n == 0:
                mv.append(1)
            else:
                s = str(n)
                if (len(s) & 1) == 0:
                    ls = len(s)//2
                    mv.append(int(s[:ls]))
                    mv.append(int(s[ls:]))
                else:
                    mv.append(n * 2024)
        for m in mv:
            n2[m] += v
    count = n2

print(sum(n2.values()))
