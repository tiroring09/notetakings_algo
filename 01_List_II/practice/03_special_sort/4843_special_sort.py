T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    numbers = list(map(int, input().split()))

    result = []
    numbers.sort()
    for i in range(len(numbers)):
        if i % 2 == 0:
            result.append(numbers.pop())
        else:
            result.append(numbers.pop(0))

    print('#{} {}'.format(tc, ' '.join(map(str, result[:10]))))

