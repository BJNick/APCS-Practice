"""
Mykyta S.
coding_test_q3.py
Answers question 3 - a merge sort
"""


def recursive_merge_sort(list):
    """Implements a recursive merge sort that returns the sorted list"""

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


if __name__ == "__main__":

    name_list = ['Bob', 'Alice', 'Gregg', 'Charles', 'Deb', 'Frank', 'Elsa']

    # Print the output to test it
    sorted_list = recursive_merge_sort(name_list)
    print(sorted_list)
    # Expected ['Alice', 'Bob', 'Charles', 'Deb', 'Elsa', 'Frank', 'Gregg']
