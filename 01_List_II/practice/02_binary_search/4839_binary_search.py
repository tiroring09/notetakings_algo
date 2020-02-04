import sys

# sys.setrecursionlimit(10**8)
sys.stdin = open('input.txt')

def bin_search(start, end, target):
    middle = (start + end) // 2
    if middle == target:
        return 1
    elif middle < target:
        return bin_search(middle, end, target) + 1
    elif middle > target:
        return bin_search(start, middle, target) + 1

T = int(input())

for tc in range(1, T + 1):
    N, A, B = tuple(map(int, input().split()))
    
    if bin_search(1, N, A) == bin_search(1, N, B):
        result = '0'
    elif bin_search(1, N, A) < bin_search(1, N, B):
        result = 'A'
    elif bin_search(1, N, A) >  bin_search(1, N, B):
        result = 'B'
        
    print('#{} {}'.format(tc, result))