#!/usr/bin/python3
thing = {(-1,0):1, (0,1):2, (1,0):4, (0,-1):8}
count = 0
with open("p6.txt") as f:
    words = [x.strip() for x in f.readlines()]
    oboard = [list(x) for x in words]
    dim = (len(oboard), len(oboard[0]))
    for i in range(dim[0]):
        for j in range(dim[1]):
            if oboard[i][j] == "^":
                opos = [i, j]
    for i in range(dim[0]):
        print(i)
        for j in range(dim[1]):
            if [i, j] == opos or oboard[i][j] == "#":
                continue
            dr = (-1, 0)
            pos = opos
            board = [list(x) for x in words]
            board[i][j] = "#"
            while pos[0] >= 0 and pos[1] >= 0 and pos[0] < dim[0] and pos[1] < dim[1]:
                curr = board[pos[0]][pos[1]]
                if curr == "#":
                    pos = last
                    dr = (dr[1], dr[0] * -1)
                    curr = board[pos[0]][pos[1]]
                if curr == "." or curr == "^":
                    curr = 0
                if curr & thing[dr]:
                    count += 1
                    break
                curr |= thing[dr]
                board[pos[0]][pos[1]] = curr
                last = pos
                pos = [pos[0] + dr[0], pos[1] + dr[1]]
    print(count)
