import asyncio
import time

def fibonacciSeries(series_length: int, first_num=0, second_num=1):
    """
    Generates a Fibonacci series and computes the golden ratio.

    The Fibonacci series is a sequence of numbers where each number is the sum
    of the two preceding ones, usually starting with 0 and 1.

    The golden ratio, often denoted by the Greek letter phi (φ), is the limit
    of the ratio of consecutive Fibonacci numbers as the series approaches infinity.

    The purpose of this function is to demonstrate how a Fibonacci series from two any
    initial values except (0, 0) will always yield the same golden ratio.

    :param series_length: The length of the series to generate.
    :param first_num: The first number of the series. (0 by default).
    :param second_num: The second number of the series. (1 by default).
    :return: A tuple containing two values:
        - (list of integers): The Fibonacci series of length `series_length`.
        - (float): The golden ratio computed from the last two numbers of the generated series.
    """
    if first_num == 0 and second_num == 0:
        print("Error: initial numbers cannot be both 0.")
        return [], None
    a, b = first_num, second_num
    series = []
    for _ in range(series_length):
        series.append(a)
        a, b = b, a + b

    gold_ratio = series[-1] / series[-2]

    return list(series), round(gold_ratio, 3)


def recursiveFib(n):
    """
    This function generates Fibonacci numbers using recursion.
    It has exponential time complexity O(2^n) due to repeated calculations.
    :param n:
    :return:
    """
    try:
        if n == 0: return 0
        if n == 1: return 1
        return recursiveFib(n - 1) + recursiveFib(n - 2)
    except RecursionError:
        print(f'[recursiveFib ERROR] - Recursion depth exceeded')

def memoizationFib(n):
    """
    This function uses memoization to optimize the recursive Fibonacci.
    It stores already computed numbers in a dictionary to avoid redundant calculations.
    The time complexity of this function is O(n), as each Fibonacci number is computed only once.
    :param n:
    :return:
    """
    try:
        memo = {0:0, 1:1}
        def f(n):
            if n in memo:
                return memo[n]
            memo[n] = f(n-1) + f(n-2)
            return memo[n]
        return f(n)
    except RecursionError:
        print(f'[memoizationFib ERROR] - Recursion depth exceeded')
        return None

def tabulationFib(n):
    """
    This function uses dynamic programming, specifically tabulation, to compute Fibonacci numbers.
    It iteratively builds up the Fibonacci sequence from the bottom up, storing the results in an array.
    It has linear time complexity O(n).
    :param n:
    :return:
    """
    tab = [0, 1]
    for i in range(2, n+1):
        new = tab[i-2] + tab[i-1]
        tab.append(new)
    return tab[n]

def noMemoFib(n):
    """
    This is another iterative approach to computing Fibonacci numbers without memoization.
    It has the same time complexity as the tabulation and memoization methods, O(n).
    :param n:
    :return:
    """
    if n < 2: return n
    a, b = 0, 1
    for i in range(2, n+1):
        a, b = b, a + b

    return b

async def measure_time(func, n):
    """
    Prints the execution time along with the result from a callback function.
    :param func: Fibonacci number computing function
    :param n: The index of the Fibonacci number to compute
    :return: None
    """
    start_time = time.time()
    result = func(n)
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"{func.__name__}({n}) excecution time: {execution_time:.6f} (Result: {result})")

async def main(n):
    """
    Runs asynchronous tasks to measure the execution time of various Fibonacci functions.
    :param n: The index of the Fibonacci number to compute
    :return: None
    """
    tasks = [
        #measure_time(recursiveFib, n),
        measure_time(memoizationFib, n),
        measure_time(tabulationFib, n),
        measure_time(noMemoFib, n),
    ]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    n = 40
    asyncio.run(main(n))


