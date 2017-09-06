# Problem Set 5: Ghost
# Name: 
# Collaborators: 
# Time: 
#

import random

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
#    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
#    print "  ", len(wordlist), "words loaded."
    return wordlist

def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq


# (end of helper code)
# -----------------------------------

# Actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program.
wordList = load_words()

def checkWordMatch(fragment):
    '''takes in an all lowercase string and tests if it matches a word in wordList'''
    if len(fragment) > 3 and fragment in wordList:
        return True
    else:
        return False
        
def wordPossible(fragment):
    '''
    takes in a possible word fragment (lowercase string) and tests to see if it
    is possible to make a word in wordList by appending letters to it.
    '''
    for word in wordList:
        if fragment == word[:len(fragment)]:
            return True
    return False


print """
Welcome to Ghost, a 2 player game
Take turns adding to the word fragment with a single letter
Don't make a valid word greater than 3 letters or add a letter that makes a future word impossible
Enter single . to exit
Good Luck!\n\n""" 

letterAdd = ''
while letterAdd != '.':   #loops back on new game
    fragment = ''
    currentPlayer = 'Player 1'
    playAgain = 'n'
    
    while playAgain == 'n' and letterAdd != '.':    #loops back every round of game
        letterAdd = string.lower(raw_input(currentPlayer + "'s turn, Please enter a letter: "))
        while letterAdd not in string.ascii_letters + '.' or len(letterAdd) > 1:
            letterAdd = string.lower(raw_input('Invalid entry, please try again: '))
        fragment += letterAdd
        
        print 'Current word fragment:', fragment
        if letterAdd == '.':
            print 'Game ended by player'
        elif checkWordMatch(fragment) or not wordPossible(fragment):
            if checkWordMatch(fragment):
                print currentPlayer, ' made a word over 3 letters, you lose!'
            else:
                print currentPlayer, ' loses because no word begins with ', fragment
            playAgain = string.lower(raw_input('Play Again? (Y/N): '))
            if playAgain == 'n':
                letterAdd = '.'
                print 'Thanks for playing!'
        else:
            if currentPlayer == 'Player 1':
                currentPlayer = 'Player 2'
            else: currentPlayer = 'Player 1'
        