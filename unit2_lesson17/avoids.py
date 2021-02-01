"""
Mykyta S.
avoids.py
Checks if the input word contains forbidden letters from the input string
"""


def avoids(word, forbidden_letters):
    """Checks whether a word contains no forbidden letters"""
    word = word.lower()
    forbidden_letters = forbidden_letters.lower().strip()

    # Loop through each letter in the word
    # If a letter is in the string that is forbidden, return false
    for forbidden_letter in forbidden_letters:
        if forbidden_letter == "":
            continue
        if forbidden_letter in word:
            return False

    # If the function completes, there are no forbidden letters and the
    # function may return True.
    return True


# Call the function to make it run! Print the result to see what happens.
if __name__ == "__main__":
    entered_word = input("Enter a word: ")
    entered_string = input("Enter forbidden letters: ")
    result = avoids(entered_word, entered_string)
    print(f"Does \"{entered_word}\" contain forbidden letters?",
          "No." if result else "Yes.")
