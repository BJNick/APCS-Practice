"""
Mykyta S.
exercise_11.py
Explains why the function swap(x, y) doesn't work in this case
"""


def swap(x, y):  # Incorrect version
    print("before swap statement: x:", x, "y:", y)
    (x, y) = (y, x)
    print("after swap statement: x:", x, "y:", y)


if __name__ == "__main__":
    a = ["This", "is", "fun"]
    b = [2, 3, 4]
    print("before swap function call: a:", a, "b:", b)
    swap(a, b)
    print("after swap function call: a:", a, "b:", b)

# After we call the function swap, a and b are still the same as they were
# before. This is because (x, y) only contain references to the lists,
# swapping (x, y) changes the references stored in them, but not the references
# in (a, b). The variable scope of the function does not interact with the
# scope of the main program here, thus it cannot change its variables.
# A possible solution might be to iterate through both lists and swap the
# elements one by one.
