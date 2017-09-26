# Problem Set 5: 6.00 Word Game
# Name: 
# Collaborators: 
# Time: 
#

import random
import string
import time

VOWELS = 'aaaaaaaaaeeeeeeeeeeeeiiiiiiiiioooooooouuuu'
CONSONANTS = 'bbccddddffggghhjkllllmmnnnnnnppqrrrrrrssssttttttvvwwxyyz'
HAND_SIZE = 10

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print "  ", len(wordlist), "words loaded."
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

#
# Problem #1: Scoring a word
#
def get_word_score(word, n):
    """
    Returns the score for a word. Assumes the word is a
    valid word.

    The score for a word is the sum of the points for letters
    in the word, plus 50 points if all n letters are used on
    the first go.

    Letters are scored as in Scrabble; A is worth 1, B is
    worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.

    word: string (lowercase letters)
    returns: int >= 0
    """
    word = word.lower()
    score = 0
    for letter in word:
        score += SCRABBLE_LETTER_VALUES.get(letter)
    if len(word) == n:
        return score + 50
    else:
        return score
#
# Make sure you understand how this function works and what it does!
#
def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    for letter in hand.keys():
        for j in range(hand[letter]):
            print letter,              # print all on the same line
    print                              # print an empty line

#
# Make sure you understand how this function works and what it does!
#
def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    At least n/3 the letters in the hand should be VOWELS.

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    hand={}
    num_vowels = n / 3
    
    for i in range(num_vowels):
        x = VOWELS[random.randrange(0,len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1
        
    for i in range(num_vowels, n):    
        x = CONSONANTS[random.randrange(0,len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1
        
    return hand

#
# Problem #2: Update a hand by removing letters
#
def update_hand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not mutate hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
             or None if word can't be made from hand
    """
#    display_hand(hand)
    handCopy = hand.copy()  #so as not to mutate hand
    for letter in word:
        if handCopy.get(letter) == None:
            return None
        elif handCopy[letter] == 1:
            del handCopy[letter]
        else:
            handCopy[letter] = handCopy[letter] - 1
#    display_hand(hand)
    return handCopy


#
# Problem #3: Test word validity
#
def is_valid_word(word, hand, word_list):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.
    
    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    """
    #test if word is composed of letters in hand
    if update_hand(hand,word) == None:
        matchHand = False
    else: matchHand = True
    #test if word in list
    validWord = word in points_dict
    return matchHand and validWord
        

#
# Problem #4: Playing a hand
#
def play_hand(hand, word_list):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    
    * The user may input a word.

    * An invalid word is rejected, and a message is displayed asking
      the user to choose another word.

    * When a valid word is entered, it uses up letters from the hand.

    * After every valid word: the score for that word and the total
      score so far are displayed, the remaining letters in the hand 
      are displayed, and the user is asked to input another word.

    * The sum of the word scores is displayed when the hand finishes.

    * The hand finishes when there are no more unused letters.
      The user can also finish playing the hand by inputing a single
      period (the string '.') instead of a word.

    * The final score is displayed.

      hand: dictionary (string -> int)
      word_list: list of lowercase strings
    """
    totalScore = 0
    word = ''
    timeLeft = float(raw_input('Enter a time limit for a hand in seconds: '))
    while len(hand) > 0 and word != '.':
        print('The letters in your hand are: ')
        display_hand(hand)
        
        validWord = False
        startTime = time.time()
        while not validWord:
            #word = str(raw_input('enter a word from your hand or a . to end turn:  '))
            word = pick_best_word(hand,points_dict)
            endTime = time.time()
            answerTime = endTime-startTime
            timeLeft = timeLeft - answerTime
            validWord = is_valid_word(word,hand,word_list)
            if word == '.':
                validWord = True
                print "I guess you can't find any more words"
            elif timeLeft < 0:
                validWord = True
                word = '.'
                print 'Time limit elapsed. Hand ended.' 
            elif not validWord:
                print 'Invalid word, try again.'
                print 'You have %0.2f seconds left.' %timeLeft
            else:
                currentScore = get_word_score(word,HAND_SIZE)
                currentScore = currentScore/answerTime
                totalScore += currentScore
                print "'%s' is worth %0.2f points" %(word, currentScore)
                print 'Round score so far = %0.2f' %totalScore
                print 'You took %0.2f seconds to answer' %answerTime
                print 'You have %0.2f seconds left on timer' %timeLeft
                hand = update_hand(hand,word)
    print '\nTotal Round Score = %0.2f' %totalScore
    if totalScore == 0:
        print '\nYou suck, loser.'
    if len(hand) == 0:
        print '\nGood Job! you used all the letters!'
 
#TODO: don't reset timer in between answers and have a better/less harsh time function  

def get_words_to_points(word_list):
    """
    assigns point values to all words in word list according to get_word_score()
    and generates a dictionary
    
    word_list: list of lowercase strings
    return: dictionary {string:int}
    """
    
    points_dict = {}
    for word in word_list:
        points_dict[word] = get_word_score(word,HAND_SIZE)
    return points_dict

def pick_best_word(hand,points_dict):
    """
    finds the highest point total word that can be made from a given hand
    
    hand: dictionary {string:int}
    points_dict: dictionary {string:int}
    """
    currentBest = 0
    currentWord = '.'  #submits period if no words possible
    for word in points_dict:
        #don't bother checking if word is worth fewer points than one already found
        if points_dict[word] > currentBest:  
            handCopy = hand.copy()  #so as not to mutate hand
            possibleWord = True
            for letter in word:
                if handCopy.get(letter) == None:
                    possibleWord = False
                elif handCopy[letter] == 1:
                    del handCopy[letter]
                else:
                    handCopy[letter] = handCopy[letter] - 1
            if possibleWord:
                currentBest = points_dict[word]
                currentWord = word
    return currentWord

                
    

    
#
# Problem #5: Playing a game
# Make sure you understand how this code works!
# 
def play_game(word_list):
    """
    Allow the user to play an arbitrary number of hands.

    * Asks the user to input 'n' or 'r' or 'e'.

    * If the user inputs 'n', let the user play a new (random) hand.
      When done playing the hand, ask the 'n' or 'e' question again.

    * If the user inputs 'r', let the user play the last hand again.

    * If the user inputs 'e', exit the game.

    * If the user inputs anything else, ask them again.
    """
    # TO DO ...
#    print "play_game not implemented."         # delete this once you've completed Problem #4
#    play_hand(deal_hand(HAND_SIZE), word_list) # delete this once you've completed Problem #4
    
    ## uncomment the following block of code once you've completed Problem #4
    hand = deal_hand(HAND_SIZE) # random init
    while True:
        cmd = raw_input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
        if cmd == 'n':
            hand = deal_hand(HAND_SIZE)
            play_hand(hand.copy(), word_list)
            print
        elif cmd == 'r':
            play_hand(hand.copy(), word_list)
            print
        elif cmd == 'e':
            break
        else:
            print "Invalid command."

#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    word_list = load_words()
    points_dict = get_words_to_points(word_list)
    play_game(word_list)

#hand = deal_hand(7)
#display_hand(hand)
#startTime = time.time()
#print pick_best_word(hand, points_dict)
#endTime = time.time()
#print get_word_score(pick_best_word(hand, points_dict),7)
#print endTime - startTime