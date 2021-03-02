"""
Mykyta S.
spam_confidence.py
Calculates and prints out the average spam confidence (Exercise 7.2)
"""

if __name__ == "__main__":

    # Open a file
    filename = input("Enter the file name: ")
    with open(filename) as f:
        total = 0
        count = 0
        # For each line, check the condition
        for line in f:
            if "X-DSPAM-Confidence:" in line:
                count += 1
                value = float(line.removeprefix("X-DSPAM-Confidence:"))
                total += value
        # Calculate and print the average
        average = total / count
        print("Average spam confidence:", average)
