"""
Mykyta S.
has_no_e.py
Prints only words that contain no 'e' and calculates their total percentage
"""


def has_no_e(text):
    """Prints words with no 'e' and calculates the percentage"""

    with open(text) as file:
        # Split the file in to a list of words
        words = remove_punctuation(file.read()).split()
        no_e_count = 0

        print("Words without E: \n")
        # For each word check if it contains no e and add it to the count
        for word in words:
            if "e" not in word.lower():
                print(word, end=", ")
                no_e_count += 1

        # Calculate the percentage = words with no e / total word count
        percentage = round(100 * no_e_count / len(words))
        print(f"\n\nThe file contains {percentage}% words with no e.")


def remove_punctuation(text):
    """Removes punctuation characters from a string"""
    bad_characters = [".", ",", ";", "!", "?", ":", "(", ")", "-", "/", "*",
                      "' ", " '", '"', "&"]
    for bad_character in bad_characters:
        text = text.replace(bad_character, "")
    return text.lower()


# Call the function to make it run!
if __name__ == "__main__":
    has_no_e("shakespeareExerpt.txt")
