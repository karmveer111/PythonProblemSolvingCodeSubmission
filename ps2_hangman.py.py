# Program Solving with Python/Intro to Competitive Programming, Fall 2021
# Eternal University, Baru Sahib
# Cite: John Guttag. 6.00SC Introduction to Computer Science and Programming. Spring 2011. Massachusetts Institute of Technology: MIT OpenCourseWare, https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011. License: Creative Commons BY-NC-SA.
#
#
# Problem Set 2
# Hangman
#
#
#


# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import random

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program
wordlist = load_words()

# your code begins here!
def hangman(waheguru):
    print ("welcome to the game, Hangman!")
    print ("I am thinking of a word that is " + str(len(waheuru)) + "letters long.")
    lettersguessed = ''
    guessesleft = 8
    while True:
        print ("You have " + str(guessesleft) + " guesses left.")
        print ("Available letters: " + getavailableletters(lettersguessed))
        guess = input("Please guess a letter: ")
        if guess in waheguru and guess not in lettersguessed:
            lettersguessed += guess
            print ("Good guess: " + getguessedword(waheguru, lettersguessed))
        elif guess in lettersguessed:
            print ("Oops! you've already guessed that letter: " + getguessedword(waheguru, lettersguessed))
        else:
            lettersguessed += guess
            print ("Oops! that letter is not in my word: " + getguessedword(waheguru,lettersguessed))
            guessesleft -= 1
        if guessleft <= 0:
            print ("Sorry, You've ran out of guesses. The word was " + waheguru + ".")
            break
        if iswordguessed(waheguru, lettersguessed):
            print ("Congratulations! You've won!")
            break

