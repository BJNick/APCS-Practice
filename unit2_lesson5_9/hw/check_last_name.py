"""
Mykyta S.
check_last_name.py
Checks last name in the alphabet
"""

last_name = input("Enter last name: ")
letter = last_name[0].lower()

if letter >= 'a' and letter < 'e':
    print("Group 1 A-D")
elif letter < 'm':
    print("Group 2 E-L")
elif letter < 't':
    print("Group 3 M-S")
else:
    print("Group 4 T-Z")