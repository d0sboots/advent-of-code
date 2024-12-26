#!/usr/bin/python3

from collections import deque

def next(n):
    n = (n ^ (n << 6)) & 0xffffff
    n = (n ^ (n >> 5)) & 0xffffff
    n = (n ^ (n << 11)) & 0xffffff
    return n

count = 0
with open("p22.txt") as f:
    for secret in f.readlines():
        num = int(secret.strip())
        for i in range(2000):
            num = next(num)
        count += num
print(count)
