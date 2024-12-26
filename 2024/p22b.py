#!/usr/bin/python3

from collections import deque
from collections import defaultdict

def next(n):
    n = (n ^ (n << 6)) & 0xffffff
    n = (n ^ (n >> 5)) & 0xffffff
    n = (n ^ (n << 11)) & 0xffffff
    return n

count = 0
with open("p22.txt") as f:
    best = defaultdict([0,-1].copy)
    for l, secret in enumerate(f.readlines()):
        num = int(secret.strip())
        nd = num % 10
        changes = []
        for i in range(2000):
            next_n = next(num)
            next_nd = next_n % 10
            changes.append(next_nd - nd)
            if len(changes) >= 4:
                slot = best[tuple(changes)]
                if slot[1] < l:
                    slot[1] = l
                    slot[0] += next_nd
                changes = changes[1:]
            num = next_n
            nd = next_nd
        count += num
print(max(x[0] for x in best.values()))
