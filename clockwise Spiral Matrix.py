#################################################################################
#                                                                               #
# Function that generates an "n by n" matrix (list of lists)                    #
# with spiraling numbers from 1 to "n", starting from center,                   #
# following clockwise or counter-clockwise sense, ascending or descending.      #
#                                                                               #
# example:                                                                      #
# >>> spiral_matrix(5)                                                          #
#                                                                               #
# Expected output:                                                              #
# [21, 22, 23, 24, 25]                                                          #
# [20, 7, 8, 9, 10]                                                             #
# [19, 6, 1, 2, 11]                                                             #
# [18, 5, 4, 3, 12]                                                             #
# [17, 16, 15, 14, 13]                                                          #
#                                                                               #
#################################################################################


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
