from decorators.Decorators import leetcode_test
@leetcode_test
def sqrt(x: int) -> int:
    if x == 0 or x == 1:
        return x

    left_pointer = l = 1
    right_pointer = r = x
    result = 0

    while l <= r:
        mid_pointer = m = (l+r) // 2
        if m * m == x:
            return m
        elif m * m < x:
            l = m + 1
            result = m
        else:
            r = m - 1

    return result


# Example usage:
sqrt(8)  # Output: 2
sqrt(16)  # Output: 4