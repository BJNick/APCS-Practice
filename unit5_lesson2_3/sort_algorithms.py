"""
Mykyta S.
sort_algorithms.py
Implements Bubble, Selection and Merge sort algorithms
"""


def bubble_sort(list):
    """Sorts the provided list using bubble sort"""
    all_sorted = False
    while not all_sorted:
        all_sorted = True
        for i in range(len(list)-1):
            if list[i] > list[i+1]:
                all_sorted = False
                list[i], list[i+1] = list[i+1], list[i]


def selection_sort(list):
    """Sorts the provided list using selection sort"""
    for sorted_length in range(len(list)-1):
        # Find min number
        min_index = sorted_length
        for i in range(sorted_length, len(list)):
            if list[min_index] > list[i]:
                min_index = i
        # Swap it
        list[sorted_length], list[min_index] = \
            list[min_index], list[sorted_length]


def merge_sort(list, start=0, end=-1):
    """Sorts the provided list using a recursive merge sort"""
    if end == -1:
        end = len(list)
    if end - start < 2:
        return

    # Sort the two halves
    middle = (start + end) // 2
    merge_sort(list, start, middle)
    merge_sort(list, middle, end)

    min_first_half = start
    min_second_half = middle

    # Merge the elements together in a new list
    sorted = []
    for i in range(start, end):
        if min_second_half >= end or \
                                (list[min_first_half] <= list[min_second_half]
                                 and min_first_half < middle):
            sorted.append(list[min_first_half])
            min_first_half += 1
        else:
            sorted.append(list[min_second_half])
            min_second_half += 1

    list[start:end] = sorted
    return


if __name__ == "__main__":

    list = []
    filename = "DataRand1000.csv"

    # For each line, add it to the list
    with open(filename) as f:
        for line in f:
            if line != "":
                list.append(int(line))

    merge_sort(list)
    print(list)
