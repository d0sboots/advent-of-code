#!/usr/bin/python3

with open("p11.txt") as f:
    nums = [int(x) for x in f.read().strip().split()]

for i in range(25):
    n2 = []
    for n in nums:
        if n == 0:
            n2.append(1)
        else:
            s = str(n)
            if (len(s) & 1) == 0:
                ls = len(s)//2
                n2.append(int(s[:ls]))
                n2.append(int(s[ls:]))
            else:
                n2.append(n * 2024)
    nums = n2

print(len(nums))
