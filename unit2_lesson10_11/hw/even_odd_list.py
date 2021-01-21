"""
Mykyta S.
even_odd_list.py
Exercise 2 from Unit 2 Lesson 11
"""

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

even_total = 0
odd_total = 0

for n in numbers:
    if n % 2:
        odd_total += 1
    else:
        even_total += 1

print("Number of even numbers:", even_total)
print("Number of odd numbers:", odd_total)
