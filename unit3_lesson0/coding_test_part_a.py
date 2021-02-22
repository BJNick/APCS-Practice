"""
Mykyta S.
coding_test_part_a.py
Contains Part A of the AP CSP 20 Coding Test A
"""


def count_vowels(word):
    """Returns the number of vowels in a given word"""
    vowels = "aeiouAEIOU"
    vowel_count = 0
    for letter in word:
        if letter in vowels:
            vowel_count += 1
    return vowel_count


def odd_average(list):
    """Returns the average of all the odd numbers in the list"""
    total = 0
    count = 0
    for num in list:
        if num % 2 == 1:
            total += num
            count += 1
    average = total / count
    return average


if __name__ == "__main__":
    # Call the first function
    word = "Supercalifragilisticexpialidocious"
    print(word)
    print("Vowel count:", count_vowels(word))

    # Call the second function
    list = [1, 2, 3, 4, 5, 6, 7]
    print(list)
    print("Average of the odd numbers:", odd_average(list))
