#!/usr/bin/python3

from collections import deque

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

with open("p21test.txt") as f:
    codes = [x.strip() for x in f.readlines()]

count = 0
for code_str in codes:
    code = [10 if x == "A" else int(x) for x in code_str]
    q = deque()
    seen = set()
    q.append((0,(0,10,4,4)))
    while True:
        cost, s = q.popleft()
        if s in seen:
            continue
        seen.add(s)
        if s[0] == 4:
            break
        cost += 1
        for i in range(4):
            n = trans1[i][s[3]]
            if n < 0:
                continue
            q.append((cost, (s[0],s[1],s[2],n)))
        if s[3] != 4:
            i = 2
            n = trans1[s[3]][s[2]]
        elif s[2] != 4:
            i = 1
            n = trans0[s[2]][s[1]]
        else:
            if code[s[0]] != s[1]:
                continue
            i = 0
            n = s[0] + 1
        if n >= 0:
            s = list(s)
            s[i] = n
            s = tuple(s)
            q.append((cost, s))
    count += cost * int(code_str[:3])
print(count)
