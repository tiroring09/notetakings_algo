# 모듈 및 내장함수 사용없이 문제풀이
import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    d = list(input())

    # 카운팅할 값이 숫자들이므로, 인덱스를 키 역할로 사용함으로써 딕셔너리를 리스트로 대체가능
    c = [0] * 10

    # 카운팅
    for i in range(n):
        c[int(d[i])] += 1

    # 최대값 찾기
    max_idx = 0
    max_value = c[0]

    for i in range(1, 10):
        if max_value <= c[i]:
            max_value = c[i]
            max_idx = i

    print('#{} {} {}'.format(tc, max_idx, max_value))
