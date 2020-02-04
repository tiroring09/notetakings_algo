T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    given = list(map(int, input().split()))

    sticks = []
    for i in range(int(len(given) / 2)):
        sticks.append((given[2 * i], given[2 * i + 1]))

    result = [sticks.pop(0)]
    while len(sticks) != 0:
        for i in range(len(sticks)):
            if result[0][0] == sticks[i][-1]:
                result.insert(0, sticks.pop(i))
                break

        for i in range(len(sticks)):
            if result[-1][-1] == sticks[i][0]:
                result.append(sticks.pop(i))
                break

    answer = []
    for each in result:
        answer.append(each[0])
        answer.append(each[1])



    print('#{} {}'.format(tc, ' '.join(map(str, answer))))

