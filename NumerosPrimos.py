import math

def is_prime(num: int) -> bool:
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


primos = [i for i in range(0, 100) if is_prime(i)]
print(primos)






