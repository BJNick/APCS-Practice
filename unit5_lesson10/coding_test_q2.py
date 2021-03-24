"""
Mykyta S.
coding_test_q2.py
Answers question 2 - a binary search
"""

animal_list = ['tiger', 'horse', 'kangaroo', 'ostrich', 'cougar']


def sort_list(list):
    """A simple bubble sort to make binary search work"""
    all_sorted = False
    while not all_sorted:
        all_sorted = True
        for i in range(len(list) - 1):
            if list[i] > list[i + 1]:
                all_sorted = False
                list[i], list[i + 1] = list[i + 1], list[i]


def recursive_binary_search(list, animal):
    """Recursive binary search, returns whether it found the animal"""
    # If the list is empty return False
    if len(list) == 0:
        return False
    # If the only number is not the right animal return False
    if len(list) == 1:
        return animal == list[0]

    # Split in the middle, if the middle is the right animal return True
    middle = len(list) // 2
    if list[middle] == animal:
        return True

    # Search in either half for the right animal
    if list[middle] > animal:
        return recursive_binary_search(list[:middle], animal)
    else:
        return recursive_binary_search(list[middle:], animal)


if __name__ == "__main__":

    # Sort the list first
    sort_list(animal_list)
    print(animal_list)

    # Test the binary search
    print(recursive_binary_search(animal_list, 'horse')) # True
    print(recursive_binary_search(animal_list, 'apple')) # False
