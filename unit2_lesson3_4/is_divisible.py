"""
Mykyta S.
is_divisible.py
Prints whether or not a number is divisible by another number.
"""


num1 = int(input("Enter dividend: "))
num2 = int(input("Enter divisor: "))

if num1 % num2 == 0:
    print(num1, "is divisible by", num2)
else:
    print(num1, "is not divisible by", num2)

