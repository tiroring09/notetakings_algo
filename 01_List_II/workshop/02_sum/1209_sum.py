import sys

sys.stdin = open('input.txt')

for _ in range(10):
    c = 100
    tc = int(input())
    d = [list(map(int, input().split())) for _ in range(c)]

    m = 0

    # horisontal
    for i in range(c):
        s = 0
        for j in range(c):
            s += d[i][j]
        if s > m:
            m = s

    # vertical
    for i in range(c):
        s = 0
        for j in range(c):
            s += d[j][i]
        if s > m:
            m = s
    
    # diagonal
    s = 0
    for i in range(c):
        s += d[i][i]
    if s > m:
        m = s

    # diagonal_2
    s = 0
    for i in range(c):
        s += d[i][-(i + 1)]
        # s += d[i][(c - 1) - i]
    if s > m:
        m = s

    print(m)

