
def spiral_matrix(size: int, clockwise=True, ascending=True) -> list:
    """
        Generates an n by n matrix (list of lists) with spiraling numbers from 1 to n*n,
        starting from the center, following either a clockwise or counter-clockwise direction,
        and in ascending or descending order.

        Args:
        - size (int): The size of the square matrix.
        - clockwise (bool): If True, generates a clockwise spiral. If False, generates a counter-clockwise spiral.
        - ascending (bool): If True, numbers go in ascending order. If False,numbers go in descending order.

        Returns:
        - list of lists: The generated spiral matrix.
    """
    if ascending:
        num = size * size
        k = -1
        condition = "num >= 1"
    else:
        num = 1
        k = 1
        condition = "num <= size * size"

    matrix = [[0] * size for _ in range(size)]
    top, left = 0, 0
    bottom, right = size - 1, size - 1

    if clockwise:

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

    else:

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

    return matrix


if __name__ == "__main__":

    my_spiral_matrix = spiral_matrix(5)

    for row in my_spiral_matrix:
        print(row)

"""
    Expected output:                                                              
    [21, 22, 23, 24, 25]                                                          
    [20, 7, 8, 9, 10]                                                             
    [19, 6, 1, 2, 11]                                                             
    [18, 5, 4, 3, 12]                                                             
    [17, 16, 15, 14, 13]      
"""
