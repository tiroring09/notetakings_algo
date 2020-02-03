import sys

sys.stdin = open('input.txt')

T = 10

for tc in range(1, T + 1):
    n = int(input())
    d = list(map(int, input().split()))

    # dumping
    for c in range(n):
        max_idx = 0
        min_idx = 0

        for i in range(1, 100):
            if d[i] > d[max_idx]:
                max_idx = i
            if d[i] < d[min_idx]:
                min_idx = i

        d[max_idx] -= 1
        d[min_idx] += 1

    max_value = d[0]
    min_value = d[0]

    # after dumping, find min & max
    for j in range(1, 100):
        if d[j] > max_value:
            max_value = d[j]
        if d[j] < min_value:
            min_value = d[j]
    
    print('#{} {}'.format(tc, max_value - min_value))