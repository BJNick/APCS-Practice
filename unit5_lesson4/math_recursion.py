"""
Mykyta S.
math_recursion.py
Contains some of the recursive sequence algorithms (Fibonacci, sums, factorial)
"""

def fibonacci(n):
    """Returns a number in the Fibonacci sequence"""
    if n <= 2:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)


def factorial(n):
    """Returns the factorial of a number"""
    if n <= 1:
        return 1
    return n * factorial(n-1)


def sum(n):
    """Recursive sum of the numbers up to n"""
    if n <= 1:
        return n
    return n + sum(n-1)


if __name__ == "__main__":

    # Print out the number sum sequence
    print("Number sum:")
    for i in range(1, 10):
        print(sum(i), end=" ")
    print()

    # Print out the Fibonacci sequence
    print("Fibonacci:")
    for i in range(1, 10):
        print(fibonacci(i), end=" ")
    print()

    # Print out the factorial sequence
    print("Factorial:")
    for i in range(1, 10):
        print(factorial(i), end=" ")
    print()