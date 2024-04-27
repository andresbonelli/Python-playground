def two_pointer_search(array: list[int], target: int) -> tuple[int, int] | None:
    """
     Search for a pair of numbers in a sorted list that sum up to a target value using the two-pointer approach.

    :param array: (list[int]) A list of integers sorted in ascending order.
    :param target: (int) The target sum to find.
    :return: A tuple containing a pair of numbers that sum up to the target value (or None if no such pair exists).

    Examples:
        >>> two_pointer_search([1, 2, 3, 4, 5], 9)
        (4, 5)

        >>> two_pointer_search([1, 2, 3, 4, 5], 10)
        None

        >>> two_pointer_search([1, 2, 3, 4, 5], 7)
        (2, 5)

    """
    array.sort()
    n = len(array)
    l = 0
    r = n - 1

    while l < r:
        summ = array[l] + array[r]
        if summ == target:

            return array[l], array[r]
        elif summ < target:
            l += 1
        elif summ > target:
            r -= 1
    return None


if __name__ == '__main__':
    arr = [5, 6, 89, 12, 1, 14, 22, 3, 14, 6]
    solution = two_pointer_search(arr, 13)
    print(solution)
