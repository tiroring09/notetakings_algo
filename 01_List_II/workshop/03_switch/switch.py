import sys

sys.stdin = open('input.txt')

def control(switch, sex, number):
    if sex == 1:
        for i in range(len(switch)):
            if (i + 1) % number == 0:
                switch[i] = (switch[i] + 1) % 2
    elif sex == 2:
        index = number - 1

        # 범위탐색
        step = 1
        while True:

            # 탈출조건: 인덱스벗어남
            if (index - step) < 0 or (index + step) >= len(switch):
                step -= 1
                break

            if switch[index - step] == switch[index + step]:
                pass

            # 탈출조건 서로 다름
            else:
                step -= 1
                break

            step += 1

        for i in range(index - step, index + step + 1):
            switch[i] = (switch[i] + 1) % 2
        


    return switch

size = int(input())
switch = list(map(int, input().split()))

stdnt_size = int(input())
stdnt = [list(map(int, input().split())) for _ in range(stdnt_size)]

for each in stdnt:
    switch = control(switch, *each)
    


# print
count = 1
for each in switch:
    print(each, end = '')
    if count % 20 == 0:
        print('\n', end = '')
    else:
        print(' ', end = '')
    count += 1
