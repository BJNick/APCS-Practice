"""
Mykyta S.
palindromes.py
Checks whether the entered string is a palindrome
"""

def is_a_palindrome(word):
    # Split the word in half, get last half
    last_half = word[-len(word)//2:]
    # Reverse it
    last_half = last_half[::-1]
    # Check if the first half same as the last
    return word.startswith(last_half)


if __name__ == "__main__":
    entered_word = input("Enter a word: ").lower()
    print("It's a palindrome!" if is_a_palindrome(entered_word) else \
          "It's not a palindrome.")