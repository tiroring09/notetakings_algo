T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    colorings = [list(map(int, input().split())) for _ in range(N)]

    matrix = [[{1:0, 2:0} for _ in range(10)] for _ in range(10)]

    for command in colorings:
        color = command[-1]
        start_x = command[0]
        start_y = command[1]
        end_x = command[2]
        end_y = command[3]

        for i in range(start_x, end_x + 1):
            for j in range(start_y, end_y + 1):
                matrix[i][j][color] = 1

    purple = 0
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j][1] and matrix[i][j][2] :
                purple += 1

    print('#{} {}'.format(tc, purple))
