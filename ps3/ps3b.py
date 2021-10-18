from ps3a import *
import time
from perm import *

#
#
# Problem #6A: Computer chooses a word
#
#

def comp_get_valid_words_with_scores(hand, word_list):
    """
    Given a hand and a word_list, returns a list of valid words
        sorted in descending order according to their word scores
    
    return list ( tuple (int,string) ) sorted according to int,
        or None if no valid words are found

    hand: dictionary (string -> int)
    word_list: list (string)
    """
    # TO DO...

def comp_choose_word(hand, word_list):
    """
    Given a hand and a word_list, find a valid word, and return it.
    This word should be calculated by considering all possible permutations
    of lengths 1 to hand length.
    
    Hint: First try to make a legal player, and then worry about making
    the computer player better (if you have time). 

    hand: dictionary (string -> int)
    word_list: list (string)
    """
    # TO DO...
    max_score = 0
    n = 7
    best_word = None
    for word in word_list:
        if is_valid_word(word, hand, word_list):
            score = get_word_score(word, n)
            if score > max_score:
                max_score = score
                best_word = word
    return best_word

#
# Problem #6B: Computer plays a hand
#
def comp_play_hand(hand, word_list):
    """
     Allows the computer to play the given hand, as follows:

     * The hand is displayed.

     * The computer chooses a word using comp_choose_words(hand, word_dict).

     * After every valid word: the score for that word is displayed, 
       the remaining letters in the hand are displayed, and the computer 
       chooses another word.

     * The sum of the word scores is displayed when the hand finishes.

     * The hand finishes when the computer has exhausted its possible choices (i.e. comp_play_hand returns None).

     hand: dictionary (string -> int)
     word_list: list (string)
    """
    # TO DO...
    score = 0
    n=7
     # The computer chooses a word
    word = comp_choose_word(hand, word_list)
    while word != None:
    
        # Display the hand
        print ("Current Hand:",)
        for letter in hand.keys():
            for j in range(hand[letter]):
                print (letter)             # print all on the same line
        print()
        points = get_word_score(word, n)
        print ('"' + word + '"' + " earned " + str(points) + " points.",)
        score += points
        print ("Total: " + str(score) + " points.\n")
        # Tell the computer how many points the word earned, and the updated total score, in one line followed by a blank line
        hand = update_hand(hand, word)
        # Update the hand 
        word = comp_choose_word(hand, word_list)
    
    # Display the hand

    if calculate_handlen(hand) > 0:
        print("Current Hand:")
        for letter in hand.keys():
            for j in range(hand[letter]):
                print (letter)            # print all on the same line
        print()
    else:
        pass
    print ("Total score: " + str(score) + " points." )
    
#
# Problem #6C: Playing a game
#
#

def play_game(word_list):
    """Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
    * If the user inputs 'n', play a new (random) hand.
    * If the user inputs 'r', play the last hand again.
    * If the user inputs 'e', exit the game.
    * If the user inputs anything else, ask them again.

    2) Ask the user to input a 'u' or a 'c'.
    * If the user inputs 'u', let the user play the game as before using play_hand.
    * If the user inputs 'c', let the computer play the game using comp_play_hand (created above).
    * If the user inputs anything else, ask them again.

    3) After the computer or user has played the hand, repeat from step 1

    word_list: list (string)
    """
    # TO DO...
    choose = input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")
    while choose != "e":
        if choose == "r":
            print ("You have not played a hand yet. Please play a new hand first!")
            choose = input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")
        while choose == "n":
            hand = deal_hand(HAND_SIZE)
            manual_or_computer = input("Enter u to have yourself play, c to have the computer play: ")
            while manual_or_computer not in ['u','c']:
                print("Invalid command.")
                manual_or_computer = input("Enter u to have yourself play, c to have the computer play: ")
            if manual_or_computer == "u":
                play_hand(hand, word_list)
            else:
                comp_play_hand(hand, word_list)
            choose = input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")
            while choose == "r":
                manual_or_computer = input("Enter u to have yourself play, c to have the computer play: ")
                while manual_or_computer not in ['u','c']:
                    print ("Invalid command.")
                    manual_or_computer = raw_input("Enter u to have yourself play, c to have the computer play: ")
                if manual_or_computer == "u":
                    play_hand(hand, word_list)
                else:
                    comp_play_hand(hand, word_list)
                choose = input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")
        if choose not in ['n','r','e']:
            print ("Invalid command." )
            choose =input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")  

#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)

    
