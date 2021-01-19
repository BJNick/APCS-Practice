"""
Mykyta S.
interview.py
Asks a classmate some questions about themselves
"""
import time

name = input("Hi! I'm Kytabot. ^_^\nWhat's your name? ")

print("Nice to meet you,", name.capitalize() + "!")

game = input("What's your favourite video game? ")

print("Awesome!")

hobby = input("Do you have a hobby? What is it? ")

if(hobby.lower() == "no"):
    print("Aw man!")
else:
    print("Nice.")

food = input("What's your favourite food? ")

print("Mmm, yes. Delicious.")

print("That's it for questions.")

print()

time.sleep(2)

print("DATABASE ENTRY:\n\"" + name.upper() + "\" LIKES", game.upper(), "AND", food.upper() + ", HOBBY:", hobby.upper())
print("ATTITUDE: POSITIVE")



