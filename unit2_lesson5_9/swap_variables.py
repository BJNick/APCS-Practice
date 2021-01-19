"""
Mykyta S.
swap_variables.py
Swap two variables
"""

a = 1
b = 2
print(a, b)

# Use 3 lines of code

a = a + b
b = a - b
a = a - b

print(a, b)

# Or use this

a, b = b, a

print(a, b)


