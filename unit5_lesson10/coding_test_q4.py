"""
Mykyta S.
coding_test_q4.py
Answers question 4 - simple recursion
"""

def f(x):
    """A recursive function as defined in the problem"""
    if x >= 6:
        return f(x-2) + 1
    else:
        return x


if __name__ == "__main__":

    # Test the function
    print(f(5)) # = 5
    print(f(6)) # = 5
    print(f(8)) # = 6


