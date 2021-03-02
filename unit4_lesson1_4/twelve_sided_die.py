"""
Mykyta S.
twelve_sided_die.py
Compares the results of a twelve sided die with 2 six sided dice
"""

import random


def roll_d12():
    """Returns a roll of a twelve sided die"""
    return random.randint(1, 12)


def roll_2d6():
    """Returns a roll of two six sided dice"""
    return random.randint(1, 6) + random.randint(1, 6)


if __name__ == "__main__":

    # Make a list of the outcomes, an integer for each outcome 0-12
    d12outcomes = [0]*13
    d6outcomes = [0]*13

    # Simulate rolling 1000 times
    for i in range(1000):

        result_d12 = roll_d12()
        result_2d6 = roll_2d6()

        d12outcomes[result_d12] += 1
        d6outcomes[result_2d6] += 1

    # Print out the results side by side
    print("N", "d12", "2d6", sep='\t')

    for i in range(1, 13):
        print(i, d12outcomes[i], d6outcomes[i], sep='\t')
