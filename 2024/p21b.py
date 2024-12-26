#!/usr/bin/python3

from collections import deque
import heapq

trans0 = [
    [2,4,5,6,7,8,9,-1,-1,-1,3],
    [-1,-1,0,10,1,2,3,4,5,6,-1],
    [-1,-1,1,2,-1,4,5,-1,7,8,0],
    [10,2,3,-1,5,6,-1,8,9,-1,-1],
]
# 0=U,1=D,2=L,3=R,4=A
trans1 = [
    [-1,0,-1,4,-1],
    [1,-1,-1,-1,3],
    [-1,2,-1,1,0],
    [4,3,1,-1,-1],
]

def one_level(level):
    costs.append([[None]*5 for x in range(5)])
    heap = [(0, 4, 1, None)]
    p_cost = costs[level-1]
    c_cost = costs[level]
    for i in range(5):
        c_cost[i][i] = 0
    remain = 20
    while True:
        node = heapq.heappop(heap)
        cost, n, rep, prev = node
        if not rep:
            if n == 4:
                for s_at in range(5):
                    bt = prev
                    at = s_at
                    while bt[3]:
                        _, bn, brep, bprev = bt
                        for i in range(brep):
                            if at == -1:
                                break
                            at = trans1[bn^1][at]
                        if at == -1:
                            break
                        bt = bprev
                    else:
                        if c_cost[at][s_at] is not None:
                            continue
                        c_cost[at][s_at] = cost
                        remain -= 1
                        if not remain:
                            return
            else:
                for i in range(1, 3 - (i < 2)):
                    heapq.heappush(heap, (cost+i, n, i, prev))
            continue
        for i in range(5):
            if i == n:
                continue
            heapq.heappush(heap, (cost+p_cost[n][i], i, 0, node))

costs = [[[0]*5]*5]
for level in range(1, 26):
    one_level(level)

with open("p21.txt") as f:
    codes = [x.strip() for x in f.readlines()]

count = 0
for code_str in codes:
    code = [10 if x == "A" else int(x) for x in code_str]
    q = [(0,(0,10,4))]
    seen = set()
    while True:
        cost, s = heapq.heappop(q)
        if s in seen:
            continue
        seen.add(s)
        if s[0] == 4:
            break
        for i in range(5):
            if i == s[-1]:
                continue
            heapq.heappush(q, (cost+costs[25][s[-1]][i], s[:-1] + (i,)))
        cost += 1
        if s[-1] != 4:
            i = 2
            n = trans0[s[2]][s[1]]
        else:
            i = 1
            if code[s[0]] != s[1]:
                n = -1
            else:
                n = s[0] + 1
        if n >= 0:
            heapq.heappush(q, (cost, s[:i-1] + (n,) + s[i:]))
    count += cost * int(code_str[:3])
print(count)
