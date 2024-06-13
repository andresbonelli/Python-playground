import time


def leetcode_test(func):
    def wrapper(*args, **kwargs):
        print(f"Executing '{func.__name__}' with input '{args}'")

        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        execution_time = end_time - start_time

        print(f"Output: {result}")
        print(f"Execution Time: {execution_time:.6f}s")
        # assert result == kwargs['expected_output'], "Wrong result!"
        return result

    return wrapper
