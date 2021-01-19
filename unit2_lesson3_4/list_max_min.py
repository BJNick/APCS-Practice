"""
Mykyta S.
list_max_min.py
Returns the sum, the maximum and the minimum values of a list
"""

my_list = [10, -13, 999, -200, 0]

max_num = my_list[0]
min_num = my_list[0]

for item in my_list:
    if min_num > item:
        min_num = item

    if max_num < item:
        max_num = item

print("Min value is", min_num, " and max value is", max_num)

sum = 0
for item in my_list:
    sum += item

print("The sum is", sum)


