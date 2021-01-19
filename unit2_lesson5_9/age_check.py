"""
Mykyta S.
age_check.py
Check and output age
"""

age = int(input("Enter age: "))
print("You are", end=" ")

if age < 0:
    print("an idiot")
elif age < 18:
    print("underage")
elif age <= 65:
    print("an adult")
elif age <= 200:
    print("a senior")
else:
    print("a robot")
