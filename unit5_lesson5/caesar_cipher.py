"""
Mykyta S.
caesar_cipher.py
Encodes a message into a caesar cipher
"""

def encode(message, displacement):
    result = ""
    for c in message:
        # Get order in the alphabet
        number = ord(c) - ord('a')
        # Add displacement and wrap
        number = (number + displacement) % 26
        while number < 0:
            number += 26
        # Convert back into a character
        result += chr(number + ord('a'))
    return result


if __name__ == "__main__":

    print(encode("test", 1))
    print(encode("xyz", 1))
    print(encode("xyz", -1))

