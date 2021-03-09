"""
Mykyta S.
linear_search.py
Performs a linear search in an unsorted list
"""


if __name__ == "__main__":

    list = []
    filename = "DataRand1000.csv"

    # For each line, add it to the list
    with open(filename) as f:
        for line in f:
            if line != "":
                list.append(int(line))

    number = int(input("Enter number: "))

    # Find number occurrences in the list
    for i in range(len(list)):
        if (list[i] == number):
            print("Found", number, "at", i)




