#!/usr/bin/python3

def doesmatch(first, pos):
    if pos >= len(nums):
        return first == target
    return doesmatch(first + nums[pos], pos+1) or doesmatch(first * nums[pos], pos+1)

count = 0
with open("p7.txt") as f:
    for prob in f.readlines():
        prob = prob.strip().split(": ")
        target = int(prob[0])
        nums = [int(x) for x in prob[1].split()]
        if doesmatch(nums[0], 1):
            count += target
print(count)
