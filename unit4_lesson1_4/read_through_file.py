"""
Mykyta S.
read_through_file.py
Prints out the lines of a file in UPPERCASE (Exercise 7.1)
"""

if __name__ == "__main__":
    filename = input("Enter file name: ")

    # For each line, print it out in uppercase
    with open(filename) as f:
        for line in f:
            print(line.upper(), end='')
