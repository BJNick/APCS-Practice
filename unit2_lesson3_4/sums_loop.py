"""
Mykyta S.
sums_loop.py
Computes a product of a and b
"""

a = int(input("Enter a: "))
b = int(input("Enter b: "))

sum = 0
count = 0

while count < b:
    sum += a
    count += 1

print(a, "*", b, "=", sum)
