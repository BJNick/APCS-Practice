"""
Mykyta S.
for_loop_practice.py
Writes outputs for the programs
"""

sum=0
for i  in range(1,10,2):
    print( i )
    sum = sum + i
print(sum)
print()

#   i   sum out
#   1   1   1
#   3   4   3
#   5   9   5
#   7   16  7
#   9   25  9
#   11  --  --
#   --  25  --


sum=0
for i  in range(10,21):
    print( i )
    sum = sum + i
print( sum)
print()

#   i   sum
#   10  10
#   11  21
#   12  33
#   13  46

sum=0
for i  in range(10,0,-1):
    print( i )
    sum = sum + i
print( sum)
print()

#   i   sum
#   10  10
#   9   19
#   8   27
#   ...
#   1   55

sum=0
for i  in range(10,0,-2):
    print( i )
    sum = sum + i
print( sum)
print()

#   i   sum
#   10  10
#   8   18
#   6   24
#   4   28
#   2   30
#   0   --

sum=0
for i  in range(2,21,3):
    print( i )
    sum = sum + i
print( sum)
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
#       77


Name = "Souls"
numChar=len(Name)
for i in range(numChar):
    AChar = Name[i]
    print (AChar)
print()

#   i   char
#   0   S
#   1   o
#   2   u
#   3   l
#   4   s

Name = "Souls"
numChar=len(Name)
for i in range(numChar-1,-1,-1):
    AChar = Name[i]
    print (AChar)
print()

#   i   char
#   4   s
#   3   l
#   2   u
#   1   o
#   0   S
#   -1  --

Name = "Souls"
for i in range(len(Name)):
    AChar = Name[i]
    if (AChar =='a') or (AChar == 'e'):
        print (AChar)
    elif (AChar =='i') or (AChar == 'o'):
        print (AChar)
    elif (AChar == 'u'):
        print (AChar)
print()

#   i   char
#   0-4 ou

Name = "Souls"
for i in range(len(Name)):
    AChar = Name[i].upper()
    print (AChar)
print()

#   i   char
#   0-4 SOULS


Name = "Souls"
AChar=''
for i in range(len(Name)):
    if i % 2 ==1:
        AChar = Name[i].upper()
        print (AChar)

#   i   char
#   0   --
#   1   O
#   2   --
#   3   L
#   4   --

