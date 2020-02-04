from itertools import combinations
# collecting all subsets from given set
# https://docs.python.org/3/library/itertools.html#itertools.combinations

T = int(input())
twelve_set = {x for x in range(1, 13)}

for tc in range(1, T + 1):
    N, K = tuple(map(int, input().split()))

    count = 0
    for each in combinations(twelve_set, N):
        if sum(each) == K:
            count += 1

    print('#{} {}'.format(tc, count))