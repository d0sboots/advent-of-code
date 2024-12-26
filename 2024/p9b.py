#!/usr/bin/python3

with open("p9.txt") as f:
    line = f.read().strip()

spots = []
pos = 0
i = 0
while True:
    spots.append((pos, ord(line[i]) - ord('0')))
    if i + 1 >= len(line):
        break
    pos += ord(line[i]) + ord(line[i+1]) - ord('0') * 2
    i += 2

checksum = 0
i, j = 0, len(spots) - 1
amt = spots[j][1]
while j > i:
    s1 = spots[i]
    checksum += i * s1[1] * (2 * s1[0] + s1[1] - 1) // 2
    pos = s1[0] + s1[1]
    rl = spots[i+1][0] - pos
    while rl > 0 and j > i:
        n = rl if rl < amt else amt
        checksum += j * n * (2 * pos + n - 1) // 2
        amt -= n
        if amt <= 0:
            j -= 1
            amt = spots[j][1]
        rl -= n
        pos += n
    i += 1
checksum += j * amt * (2 * spots[j][0] + amt - 1) // 2

print(checksum)
