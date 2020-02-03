from collections import Counter

import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    d = list(input())

    # 카운팅위한 딕셔너리를 컬렉션의 카운터함수를 통해 생성
    c = Counter(d)

    # 수업에서 다룬 Counter객체에서 사용가능한 메서드들
    # .elements()
    # .most_common()

# 다른 학우 예제들
'''
    n = int(input())
    cards = list(input())
    d = list(Counter(cards).most_common())
    result = sorted(d, key=lambda x: (-x[1], -int(x[0])))   # 음수취하면서 최다빈출 중 최대값 정렬했다
    mx_card, mx_cnt = result[0]
    print('#{0} {1} {2}'.format(t, mx_card, mx_cnt))
'''
'''
    n = int(input())
    d = list(input())
    c = Counter(d).most_common()
    max_num = c[0][1]
    max_cards = [x for x, y in c if y == max_num]   # max_num과 일치하는 자료 중 x만 원소로 받아 최대값 뽑아냄
    print(f'#{tc} {max(max_cards)} {max_num}')
'''