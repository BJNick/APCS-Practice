"""
Mykyta S.
coding_test_q1.py
Answers question 1 - a linear search
"""

animal_list = ['tiger', 'horse', 'kangaroo', 'ostrich', 'cougar']


def linear_search(animal):
    """Returns a tuple containing whether the element was found and index"""
    # Goes through each element in the list and if it matches returns
    for i in range(len(animal_list)):
        if animal == animal_list[i]:
            return True, i
    # If no element is found return False
    return False, -1


if __name__ == "__main__":

    # Test the function
    print(linear_search('horse')) # (True, 1)
    print(linear_search('apple')) # (False, -1)

