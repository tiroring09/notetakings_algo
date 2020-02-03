import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    N, M = tuple(map(int, input().split()))
    d = list(map(int, input().split()))

    max_value = 0
    min_value = 10000000

    for i in range(N - M + 1):
        s = 0
        for j in range(i, i + M):
            s += d[j]
        if s > max_value:
            max_value = s
        if s < min_value:
            min_value = s
    




    print('#{} {}'.format(tc, max_value - min_value))