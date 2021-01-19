"""
Mykyta S.
rock_paper_scissors.py
Plays 10 games of rock paper scissors and displays the results.
"""

import random

# Constants to keep the code more readable
R, S, P = 1, 2, 3


def random_choice():
    """Generates a random choice 1-3"""
    return random.randint(1, 3)


def does_beat(a, b):
    """Returns whether A beats B"""
    if a == b:
        return 0
    elif (a == S and b==P) or (a==P and b==R) or (a==R and b==S):
        return 1
    else:
        return -1


def to_str(n):
    """Convert a number to string"""
    return "rock" if n == R else "scissors" if n == S else "paper"


# Total number of ties and wins
ties = 0
pat_wins = 0
chris_wins = 0

for i in range(10):

    chris_choice = random_choice()
    pat_choice = random_choice()

    outcome = does_beat(chris_choice, pat_choice)

    print("#" + str(i+1), end="\t")

    if outcome == 0:
        ties += 1
        print("It's a tie! Both of them chose",
              to_str(chris_choice), end=".\n")

    elif outcome == 1:
        chris_wins += 1
        print("Chris wins!", to_str(chris_choice).capitalize(), "beats",
              to_str(pat_choice), end=".\n")

    else:
        pat_wins += 1
        print("Pat wins!", to_str(pat_choice).capitalize(), "beats",
              to_str(chris_choice), end=".\n")

print()

print("Chris won", chris_wins, "times.")
print("Pat won", pat_wins, "times.")
print("There were", ties, "ties.")