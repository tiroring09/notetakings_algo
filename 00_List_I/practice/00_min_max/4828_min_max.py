import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    d = list(map(int, input().split()))

    # 제일 간단한 방법
    print('#{} {}'.format(tc, max(d) - min(d)))