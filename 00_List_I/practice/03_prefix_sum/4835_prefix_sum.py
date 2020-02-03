import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    N, M = tuple(map(int, input().split()))
    d = list(map(int, input().split()))

    arr = []

    for i in range(N - M + 1):
        arr.append(sum(d[i:i + M]))

    print('#{} {}'.format(tc, max(arr)))