"""
Mykyta S.
square_dartboard.py
Performs a simulation of throwing darts on a square dartboard
"""


import random


def get_random_coordinates(min, max):
    """Returns random coordinates x, y in range (min, max)"""
    return random.uniform(min, max), random.uniform(min, max)


def hits_bullseye(x, y):
    """Returns whether the dart hits the bullseye"""
    return 0.25 <= x <= 0.75 and 0.25 <= y <= 0.75


if __name__ == "__main__":
    num_throws = int(input("Enter number of throws: "))
    n_bull = 0
    # Throw each dart
    for i in range(num_throws):
        x, y = get_random_coordinates(0, 1)
        # Add to the total if it hits
        if hits_bullseye(x, y):
            n_bull += 1
    print("Hit bullseye", n_bull, "times")
    # Calculate the percentage
    print(n_bull/num_throws*100, "% correct")


