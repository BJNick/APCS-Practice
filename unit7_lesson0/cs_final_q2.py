"""
Mykyta S.
cs_final_q2.py
Contains the recursive function for the n terms of an alternating series
"""

import sys


# Calculates the sum of the n terms of the series 1 - 1/2 + 1/3 - 1/4 + ...
def calculate_series(n_terms):
    if n_terms <= 1:
        return 1
    elif n_terms % 2 == 0:
        return calculate_series(n_terms - 1) - (1 / n_terms)
    else:
        return calculate_series(n_terms - 1) + (1 / n_terms)


if __name__ == "__main__":

    # Set max recursion depth to 1500 instead of the default 1000
    sys.setrecursionlimit(1500)

    # Should return 0.6926474305598223
    print(calculate_series(1000))
