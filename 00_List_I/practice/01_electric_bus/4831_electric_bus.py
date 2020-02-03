'''
import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    K, N, M = tuple(map(int, input().split()))
    d = list(map(int, input().split()))

    # 출발역, 종착역 추가
    d.insert(0, 0)
    d.append(N)

    last = d[0]
    cnt = 0

    # 몇번째 정류장에 주유소가 있는지 리스트에 있으니까 인덱스 하나씩 전진하면서 최장주행거리 K와 비교한다.
    for i in range(1, M + 2):
        # 주행거리 K보다 주유소간 거리가 멀어서 운행불가능
        if d[i] - d[i - 1] > K:
            cnt = 0
            break
        # 운행가능한 경우에 마지막으로 들르게 될 정류소 저장
        if d[i] > last + K:
            last = d[i - 1]
            cnt += 1

    print('#{} {}'.format(tc, cnt))
'''

K, N, M = 3, 10, 5
d = [1,3,5,7,9]



print(cnt)