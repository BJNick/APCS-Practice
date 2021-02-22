"""
Mykyta S.
coding_test_part_b.py
Contains Part B of the AP CSP 20 Coding Test A
"""


def encode(text):
    """Changes the vowels of a string from aeiou to @(:0[ respectively"""
    encoded_text = ""
    for letter in text:
        if letter == "a":
            encoded_text += "@"
        elif letter == "e":
            encoded_text += "("
        elif letter == "i":
            encoded_text += ":"
        elif letter == "o":
            encoded_text += "0"
        elif letter == "u":
            encoded_text += "["
        else:
            encoded_text += letter
    return encoded_text


if __name__ == "__main__":
    text = input("Enter message: ")
    print("Encoded message: ", encode(text))
