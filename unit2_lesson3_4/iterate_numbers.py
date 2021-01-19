"""
Mykyta S.
iterate_numbers.py
Iterate different sequences of numbers
"""

def all_num(n):
    i = 1
    while i <= n:
        print(i)
        i += 1

def even_num(n):
    i = 2
    while i <= n:
        print(i)
        i += 2

def multiples_of_five(n):
    i = 1
    while i <= n:
        print(i*5)
        i += 1

multiples_of_five(3)
