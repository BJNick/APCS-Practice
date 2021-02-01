"""
Mykyta S.
exercise_4.py
Answers the question about variables this and that
"""

if __name__ == '__main__':
    this = ["I", "am", "not", "a", "crook"]
    that = ["I", "am", "not", "a", "crook"]
    print("Test 1: {0}".format(this is that))
    that = this
    print("Test 2: {0}".format(this is that))


# The two lists have different references, even though they have the same
# contents. This means that (this is that) would return False, as the
# references are not the same. After we assign the reference (this) to variable
# (that), both variables contain the same reference, therefore (this is that)
# returns True.
