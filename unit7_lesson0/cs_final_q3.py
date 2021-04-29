"""
Mykyta S.
cs_final_q3.py
Contains a merge sort and a binary search for a list
"""

import random


# Implements a recursive merge sort that returns the sorted list
def recursive_merge_sort(list):
    # If empty or just one element return same list
    if len(list) == 0 or len(list) == 1:
        return list[:]

    # Sort the two halves
    middle = len(list) // 2
    first_half = recursive_merge_sort(list[:middle])
    second_half = recursive_merge_sort(list[middle:])

    # Index the minimum elements in each list
    min_first_half = 0
    min_second_half = 0

    # Merge the elements together in a new list
    sorted = []
    for i in range(len(list)):
        if min_second_half >= len(second_half) or \
                (min_first_half < len(first_half) and
                 first_half[min_first_half] <= second_half[min_second_half]):

            sorted.append(first_half[min_first_half])
            min_first_half += 1
        else:
            sorted.append(second_half[min_second_half])
            min_second_half += 1

    return sorted


# Implements a looping binary search that returns the element index or None
def loop_binary_search(list, num):
    minimum = 0
    maximum = len(list)

    # While range is positive
    while minimum != maximum - 1:
        middle = (maximum + minimum) // 2
        # Split it in half or return the index
        if list[middle] == num:
            return middle
        if num < list[middle]:
            maximum = middle
        else:
            minimum = middle

    # If the sublist has one item left, check if it's correct or not
    if maximum - minimum == 1 and list[minimum] == num:
        return minimum
    else:
        return -1


if __name__ == "__main__":

    # Create a random list
    unsorted_list = []
    for n in range(5):
        unsorted_list.append(random.randrange(1, 100))
    print("Random list:")
    print(unsorted_list)

    # Sort the list
    sorted_list = recursive_merge_sort(unsorted_list)
    print("\nMerge sort:")
    print(sorted_list)

    # Test binary search
    print("\nSearch for 1000:")
    found_element_index = loop_binary_search(sorted_list, 1000)
    print(found_element_index)

    print(f"\nSearch for {unsorted_list[0]}:")
    found_element_index = loop_binary_search(sorted_list, unsorted_list[0])
    print(found_element_index)
