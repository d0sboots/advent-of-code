#!/usr/bin/python3

count = 0
with open("p6.txt") as f:
    board = [list(x.strip()) for x in f.readlines()]
    dim = (len(board), len(board[0]))
    for i in range(dim[0]):
        for j in range(dim[1]):
            if board[i][j] == "^":
                pos = [i, j]
    dr = [-1, 0]
    while pos[0] >= 0 and pos[1] >= 0 and pos[0] < dim[0] and pos[1] < dim[1]:
        if board[pos[0]][pos[1]] == "#":
            pos = last
            dr = [dr[1], dr[0] * -1]
        board[pos[0]][pos[1]] = "X"
        last = pos
        pos = [pos[0] + dr[0], pos[1] + dr[1]]
    print(sum(sum(y == "X" for y in x) for x in board))
