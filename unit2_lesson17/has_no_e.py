__author__ = 'Ms. Burton'

def has_no_e (text):
    #open a file and read in the text
    with open (text) as file:
        #split the file in to a list of words
        words = file.read().split()

    #Your Code Goes Here!!
    #For each word in the list, check to see if it has an e
    #If it does not, print it!


#Call the function to make it run!