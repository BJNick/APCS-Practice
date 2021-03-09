"""
Mykyta S.
binary_search.py
Performs a binary search on a sorted list
"""


def recursive_binary_search(list, num):
    # If the list is empty return -1
    if len(list) == 0:
        return -1
    # If the only number is not the result return -1
    if len(list) == 1:
        return 0 if num == list[0] else -1

    # Split in the middle
    middle = len(list) // 2
    if list[middle] == num:
        return middle

    # Search in either half
    if list[middle] > num:
        subindex = recursive_binary_search(list[:middle], num)
    else:
        result = recursive_binary_search(list[middle:], num)
        subindex = result + middle if result != -1 else -1

    return subindex


def loop_binary_search(list, num):
    minimum = 0
    maximum = len(list)

    # While range is positive
    while minimum != maximum-1:
        middle = (maximum + minimum) // 2
        # Split it in half or return the index
        if (list[middle] == num):
            return middle
        if (num < list[middle]):
            maximum = middle
        else:
            minimum = middle

    # If the sublist has one item left, check if it's correct or not
    if maximum-minimum == 1 and list[minimum] == num:
        return minimum
    else:
        return -1


if __name__ == "__main__":

    data = []
    filename = "DataSorted1000.csv"

    # For each line, add it to the list
    with open(filename) as f:
        for line in f:
            if line != "":
                data.append(int(line))

    number = int(input("Enter number: "))

    # Find number occurrence in the list
    result = loop_binary_search(data, number)
    if result >= 0:
        print("Found at", result)
    else:
        print("Item not found")

