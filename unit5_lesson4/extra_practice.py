"""
Mykyta S.
extra_practice.py
Contains some extra exercises for recursion
"""


def fibonacci_loop(n):
    """Finds a fibonacci number using a loop"""
    a, b = 1, 1
    for i in range(n-1):
        a, b = b, a+b
    return a


def even_sum(n):
    """Finds a sum of even numbers up to n"""
    if n == 1:
        return 2
    return even_sum(n-1) + n*2


def recursive_min(item):
    """Finds the minimum integer in a nested list"""
    if isinstance(item, int):
        return item
    else:
        if len(item) == 1:
            return recursive_min(item[0])
        return min(recursive_min(item[0]), recursive_min(item[1:]))


if __name__ == "__main__":
    # Print outputs of the functions
    print(recursive_min([2, [[100, -10], 90], [10, -1111], 8, 6]))
    print(even_sum(4))
    print(fibonacci_loop(8))
