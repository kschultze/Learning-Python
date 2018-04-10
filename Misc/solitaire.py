# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 17:47:24 2018

@author: kschultze

program to determine how often a game of solitaire is dealt in which no initial
moves can be made
"""

class card(object):
    def __init__(self,value,suit):
        """
        value: type int
        suit: type string in form hearts,diamonds,spades,clubs
        """
        self.value = value
        self.suit = suit
        if self.suit == 'hearts' or self.suit == 'diamonds':
            self.color = 'red'
        else: self.color = 'black'
    
    def __str__(self):
        return str(self.value) + ' of ' + self.suit

    def higherCard(self,otherCard):
        if self.value > otherCard.value:
            return self
        elif self.value < otherCard.value:
            return otherCard
        else: return None

def newStandardDeck():
    """
    creates a list of card objects of the standard 52 card deck w/o jokers
    first card in list is top of deck
    ace assumed low (i.e. value of 1)
    """
    values = [1,2,3,4,5,6,7,8,9,10,11,12,13]
    deck = []
    for i in values:
        deck.append(card(i,'hearts'))
    for i in values:
        deck.append(card(i,'clubs'))
    values.reverse()
    for i in values:
        deck.append(card(i,'diamonds'))
    for i in values:
        deck.append(card(i,'spades'))
    return deck

def printDeck(deck):
    for card in deck:
        print card

import random

def shuffle(deck):
    deckCopy = deck[:]
    shuffledDeck = []
    for i in range(len(deck)):
        randIndex = random.randint(0,len(deckCopy)-1)
        randCard = deckCopy.pop(randIndex)
        shuffledDeck.append(randCard)
    return shuffledDeck

def validMove(moveCard,ontoCard):
    """
    can the first card be moved onto the second card in solitaire?
    """
    return moveCard.value + 1 == ontoCard.value and moveCard.color != ontoCard.color
        
def tryToPlay():
    """
    deals out a game of solitaire and tests to see if any moves can be made
    note: since it's all random, I just take the first 15 cards in the deck to test this
    returns 1 if a move can be made
    returns 0 if no move can be made
    """
    deck = shuffle(newStandardDeck())
    faceUp = deck[0:7]
    playerHand = deck[7:15]

#    for i in faceUp: print i
#    print ' '
#    for i in playerHand: print i
    
    #tests whether there are any aces, which can be moved immediately to the top row
    for card in deck[0:15]:
        if card.value == 1:
            return 1
    
    for card in faceUp:
        for otherCard in faceUp:
            if validMove(card,otherCard):
#                print ' '
#                print card
#                print otherCard
                return 1

    for card in playerHand:
        for otherCard in faceUp:
            if validMove(card,otherCard):
#                print 'X'
#                print card
#                print otherCard
                return 1
    return 0

numGames = 1000000
winCount = 0
for i in range(numGames):
    winCount += tryToPlay()

unWinnable = 1 - winCount/float(numGames)
print unWinnable
    
    