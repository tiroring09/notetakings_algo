import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    N, M = tuple(map(int, input().split()))
    d = [list(map(int, input().split())) for _ in range(N)]

    kill = []
    for i in range(N - M + 1):
        for j in range(N - M + 1):
            s = 0
            for k in range(M):
                s += sum(d[i + k][j:j+M])   # 리스트 슬라이싱 응용
            
            kill.append(s)

    print('#{} {}'.format(tc, max(kill)))
