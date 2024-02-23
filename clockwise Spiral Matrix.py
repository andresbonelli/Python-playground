
def spiral_matrix(size: int, counter_clockwise=False, reverse=False):

    if reverse:
        num = 1
        k = 1
        condition = "num <= size * size"
    else:
        num = size * size
        k = -1
        condition = "num >= 1"

    matrix = [[0] * size for _ in range(size)]
    top, left = 0, 0
    bottom, right = size - 1, size - 1

    if not counter_clockwise:

        while eval(condition):
            for i in range(right, left - 1, -1):
                matrix[top][i] = num
                num += k
            top += 1

            for i in range(top, bottom + 1):
                matrix[i][left] = num
                num += k
            left += 1

            for i in range(left, right + 1):
                matrix[bottom][i] = num
                num += k
            bottom -= 1

            for i in range(bottom, top - 1, - 1):
                matrix[i][right] = num
                num += k
            right -= 1

    elif counter_clockwise:

        while eval(condition):
            for i in range(left, right + 1):
                matrix[top][i] = num
                num += k
            top += 1

            for i in range(top, bottom + 1):
                matrix[i][right] = num
                num += k
            right -= 1

            for i in range(right, left - 1, -1):
                matrix[bottom][i] = num
                num += k
            bottom -= 1

            for i in range(bottom, top - 1, -1):
                matrix[i][left] = num
                num += k
            left += 1

    print('\n')
    for row in matrix:
        print(row)


