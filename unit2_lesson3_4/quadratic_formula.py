"""
Mykyta S.
quadratic_formula.py
Calculates x based on input of a, b and c
"""

import math


def find_roots(a, b, c):
    if (b**2 - 4*a*c < 0):
        return ()
    root1 = (-b + math.sqrt(b**2 - 4*a*c)) / (2 * a)
    root2 = (-b - math.sqrt(b**2 - 4*a*c)) / (2 * a)
    return (root1, root2)

a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

print("The roots are", find_roots(a,b,c))
