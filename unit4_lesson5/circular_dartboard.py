"""
Mykyta S.
circular_dartboard.py
Performs a simulation of throwing darts at a circular dartboard
"""


import random
import math


def get_random_coordinates(min, max):
    """Returns random coordinates x, y in range (min, max)"""
    return random.uniform(min, max), random.uniform(min, max)


if __name__ == "__main__":
    num_throws = int(input("Enter number of throws: "))
    n_outer, n_inner, n_bulls, n_missed = 0, 0, 0, 0

    # Throw each dart
    for i in range(num_throws):
        # Generate coordinates and calculate the distance from the center
        x, y = get_random_coordinates(-3, 3)
        radius = math.sqrt(x * x + y * y)
        # Find where it hits
        if (radius <= 1):
            n_bulls += 1
        elif (radius <= 2):
            n_inner += 1
        elif (radius <= 3):
            n_outer += 1
        else:
            n_missed += 1

    # Calculate the score
    points = n_bulls * 15 + n_inner * 5 + n_outer * 3

    print("Darts thrown:", num_throws)
    print("Score:", points)

    print()
    print("Hit bullseye", n_bulls, "times")
    print("Hit inner circle", n_inner, "times")
    print("Hit outer circle", n_outer, "times")
    print("Missed ", n_missed, "times")

    print()
    # Print the percentage
    print("Accuracy: ", n_bulls / num_throws * 100, "%", sep="")



