"""
Mykyta S.
count_words.py
Finds the total count of each word in a text, and finds unique words in 2 files
"""


def count_words(text):
    """Counts each word in a file called (text)"""

    # Open a file and read the text
    with open(text) as file:
        # Split the file in to a list of words
        words = remove_punctuation(file.read()).split()
        # Create a set of unique words from the list words
        unique_words = {*words}

        # For each string in the new list
        for unique_word in unique_words:
            # Count the number of times the word appears
            count = words.count(unique_word)
            # Print the string and the number of times it appears.
            print(f'"{unique_word.capitalize() }" appears {count} times.')


def find_unique_words(text1, text2):
    """Finds words unique to each text"""
    with open(text1) as file1:
        with open(text2) as file2:
            # Split the files in to a list of words
            words1 = remove_punctuation(file1.read()).split()
            words2 = remove_punctuation(file2.read()).split()

            # Create sets of unique words for each file
            unique_words1 = {*words1}
            unique_words2 = {*words2}

            # Make a set for the words they have in common
            common_words = set()

            for word in unique_words1:
                if word in unique_words2:
                    common_words.add(word)

            # Remove common words from unique words list
            unique_words1 = unique_words1.difference(common_words)
            unique_words2 = unique_words2.difference(common_words)

            print(f"{text1} contains these unique words: {unique_words1}\n")
            print(f"{text2} contains these unique words: {unique_words2}")


def remove_punctuation(text):
    """Removes punctuation characters from a string"""
    bad_characters = [".", ",", ";", "!", "?", ":", "(", ")", "-", "/", "*",
                      "' ", " '", '"', "&"]
    for bad_character in bad_characters:
        text = text.replace(bad_character, "")
    return text.lower()


# Call the function to make it run! Print the result to see what happens.
if __name__ == "__main__":
    count_words("lewisCarolExerpt.txt")
    print()
    find_unique_words("lewisCarolExerpt.txt", "shakespeareExerpt.txt")
