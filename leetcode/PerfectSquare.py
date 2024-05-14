def is_perfect_square(num):
    """
    :type num: int
    :rtype: bool
    """
    if num < 1:
        return False
    if num == 1:
        return True

    left_pointer = l = 1
    right_pointer = r = num // 2

    while l <= r:
        mid_pointer = m = (l + r) // 2

        if m * m == num:
            return True
        elif m * m < num:
            l = m + 1
        else:
            r = m - 1

    return False

print(is_perfect_square(16))
print(is_perfect_square(14))
print(is_perfect_square(1))