import math

def is_prime(num: int) -> bool:
    """
    Check if a given integer is a prime number.

    :param num: The integer to be checked for primality.
    :return bool: True if the number is prime, False otherwise.
    """
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    for i in range(5, (round(math.sqrt(num)+1)), 6):
        if num % i == 0 or num % (i + 2) == 0:
            return False
    return True


if __name__ == "__main__":

    primos = [i for i in range(0, 100) if is_prime(i)]
    print(primos)

"""
Expected output:
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
"""




