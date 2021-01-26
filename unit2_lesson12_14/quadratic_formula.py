"""
Mykyta S.
quadratic_formula.py
Applies the quadratic formula on user-entered a, b, c values
"""


def discriminant(a,b,c):
    """Returns the discriminant of the quadratic function"""
    test = b**2 - 4*a*c
    if (test < 0):
        return None
    return test**0.5


def quad_roots(a,b,c):
    """Calculates the roots of the quadratic function"""
    D = discriminant(a,b,c)
    if not D:
        return (None, None)
    root1 = (-b + D) / (2 * a)
    root2 = (-b - D) / (2 * a)
    return (root1, root2)


if __name__ == '__main__':
    a = float(input("Enter a: "))
    b = float(input("Enter b: "))
    c = float(input("Enter c: "))

    roots = quad_roots(a, b, c)
    rt1, rt2 = roots

    if (rt1):
        print("The roots are", rt1, "and", rt2)
    else:
        print("There are no roots")
