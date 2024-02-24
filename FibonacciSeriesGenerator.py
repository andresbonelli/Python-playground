

def fibonaci_series_generator(series_length: int, first_num=0, second_num=1):
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

    return list(series), gold_ratio

if __name__ == "__main__":
    n = 20
    fib_series, golden_ratio = fibonaci_series_generator(n)
    print(f'Fibonacci series first {n} numbers: {fib_series}')
    print(f'Golden ratio: {round(golden_ratio, 3)}')


