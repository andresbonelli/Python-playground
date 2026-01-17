import time, random
from typing import List


def binary_search(nums: List[int], target: int) -> int:
    if len(nums) == 1:
        return 0 if nums[0] == target else -1

    left_pointer = l = 0
    right_pointer = r = len(nums) - 1

    while l <= r:
        mid_pointer = m = (l + r) // 2
        if nums[m] == target:
            return m
        elif target < nums[m]:
            r = m - 1
        elif nums[m] < target:
            l = m + 1
    return -1


def recursive_binary_search(nums: List[int], target: int, offset=0) -> int:
    if len(nums) == 0:
        return -1

    left_pointer = l = 0
    right_pointer = r = len(nums) - 1
    mid_pointer = m = (l + r) // 2
    if nums[m] == target:
        return m + offset
    elif target < nums[m]:
        return recursive_binary_search(nums[:m], target, offset)
    elif nums[m] < target:
        return recursive_binary_search(nums[m + 1:], target, offset + m + 1)
    return -1

def medir_tiempo(funcion, *args):
 inicio = time.time()
 resultado = funcion(*args)
 fin = time.time()
 return resultado, fin - inicio

LIMIT = 10000
nums = [random.randint(0, LIMIT) for _ in range(LIMIT)]
nums = list(set(sorted(nums)))
TARGET = random.randint(0, LIMIT)
#binary_search(nums, 50)
#recursive_binary_search(nums, 50)
resultado1, tiempo1 = medir_tiempo(recursive_binary_search, nums, TARGET)
resultado2, tiempo2 = medir_tiempo(binary_search, nums, TARGET)

print(f"Busqueda binaria recursiva: Numero Buscado={TARGET}, Posicion={resultado1 if resultado1 >= 0 else "(no encontraado)"}, Tiempo={tiempo1:.8f} segundos")
print(f"Busqueda binaria optimizada: Numero Buscado={TARGET}, Posicion={resultado2 if resultado2 >= 0 else "(no encontrado)"}, Tiempo={tiempo2:.8f} segundos")
