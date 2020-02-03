# min & max 함수 없이 풀기

import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    d = list(map(int, input().split()))

    max_num = d[0]
    min_num = d[0]

    for i in range(1, n):
        if d[i] > max_num:
            max_num = d[i]
        if d[i] < min_num:
            min_num = d[i]

    print('#{} {}'.format(tc, max_num - min_num))