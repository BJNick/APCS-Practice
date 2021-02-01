"""
Mykyta S.
exercise_5.py
Contains a function add_vectors(u, v) that adds two vectors together
"""


def add_vectors(u, v):
    """Adds two vectors u and v together"""
    new_list = []
    # Creates and returns a new list with the sums
    for count in range(len(u)):
        new_list.append(u[count] + v[count])
    return new_list


if __name__ == "__main__":
    print(add_vectors([1, 1], [1, 1]) == [2, 2])
    print(add_vectors([1, 2], [1, 4]) == [2, 6])
    print(add_vectors([1, 2, 1], [1, 4, 3]) == [2, 6, 4])
    # Prints True for each correct test
