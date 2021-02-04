"""
Mykyta S.
while_loop_practice.py
Writes outputs for the programs
"""


sum = 0
i = 0
while i < 10:
    print(i)
    sum = sum + i
    i += 1
print(sum)
print()

#   i   sum
#   0   0
#   1   1
#   ...
#   9   45

sum = 0
i = 10
while i < 21:
    print(i)
    sum = sum + i
    i += 2
print(sum)
print()

#   i   sum
#   10  10
#   12  22
#   14  36
#   16  52
#   18  70
#   20  90
#   22  --

i = 10
sum = 0
while i >= 0:
    print(i)
    sum = sum + i
    i -= 1
print(sum)
print()

#   i   sum
#   10  10
#   9   19
#   ....
#   0   55


sum = 0
i = 10
while i > -1:
    print(i)
    sum = sum + i
    i -= 2
print(sum)
print()

#   i   sum
#   10  10
#   8   18
#   6   24
#   4   28
#   2   30
#   0   30
#   -2  --

i = 2
sum = 0
while i < 21:
    print(i)
    sum = sum + i
    i += 3
print(sum)
print()

#   i   sum
#   2   2
#   5   7
#   8   15
#   11  26
#   14  40
#   17  57
#   20  77
#   23  --

Name = "Python"
numChar = len(Name)
i = numChar - 1
while i >= 0:
    AChar = Name[i]
    print(AChar)
    i -= 1
print()

#   i   char
#   5   n
#   4   o
#   3   h
#   2   t
#   1   y
#   0   P
#   -1  --

Name = "Loops"
numChar = len(Name)
i = numChar - 1
while i >= 0:
    AChar = Name[i]
    print(AChar)
    i -= 1

#   i   char
#   4   s
#   3   p
#   2   o
#   1   o
#   0   L

