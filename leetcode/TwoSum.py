def two_sum(array: list[int], target: int) -> tuple[int, int] | None:
    """
     Search for the index of pair of numbers that sum up to a target value using the two-pointer approach.

    :param array: (list[int]) A list of integers (later sorted in ascending order).
    :param target: (int) The target sum to find.
    :return: A tuple containing the indexes of the pair of numbers that sum up to the target value
             (or None if no such pair exists).
    """
    sorted_arr = sorted(array)
    n = len(sorted_arr)
    left = 0
    right = n - 1

    while left < right:
        summ = sorted_arr[left] + sorted_arr[right]
        if summ == target:

            return array.index(sorted_arr[left]), array.index(sorted_arr[right])
        elif summ < target:
            left += 1
        elif summ > target:
            right -= 1
    return None

def two_sum_no_sort(array: list[int], target: int) -> tuple[int, int] | None:
    n = len(array)
    hash_map = {}

    for i in range(n):
        diff = target - array[i]
        if diff in hash_map:
            return hash_map[diff], i
        else:
            hash_map[array[i]] = i

    return None


if __name__ == '__main__':
    arr = [2, 7, 11, 15]
    solution = two_sum_no_sort(arr, 9)
    print(solution)
    arr2 = [3, 2, 4]
    solution2 = two_sum_no_sort(arr2, 6)
    print(solution2)
    arr3 = [3, 3]
    solution3 = two_sum_no_sort(arr3, 6)
    print(solution3)
