# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 14:08:39 2018

@author: kschultze

Code to determine which 2 card holdem hand is most likely to result in having 'the nuts'
aka the best possible hand using the 5 community cards
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

def findNuts(commCards):
    if straightFlush(commCards) != None:
        return straightFlush(commCards)
    if fourOfKind(commCards) != None:
        return fourOfKind(commCards)
    if fullHouse(commCards) != None:
        return fullHouse(commCards)
    if flush(commCards) != None:
        return flush(commCards)
    if straight(commCards) != None:
        return straight(commCards)
    if threeOfKind(commCards) != None:
        return threeOfKind(commCards)
    return "error: didn't find the nuts"
    
def straightFlush(commCards):
    #test for flush possibility
    hearts = []
    diamonds = []
    clubs = []
    spades = []
    for card in commCards:
        if card.suit == 'hearts': hearts.append(card.value)
        if card.suit == 'diamonds': diamonds.append(card.value)
        if card.suit == 'clubs': clubs.append(card.value)
        if card.suit == 'spades': spades.append(card.value)
    flushCards = None
    if len(hearts) > 2:
        flushCards = hearts
    if len(diamonds) > 2:
        flushCards = diamonds
    if len(clubs) > 2:
        flushCards = clubs
    if len(spades) > 2:
        flushCards = spades
    if flushCards == None:
        return None
    
    printDeck(flushCards)
    
    
    
def straightPossible(highCard,commCards):
    """
    takes a range (usually 5 cards) and finds out if any of the community cards
    can make a straight with any hole cards.  i.e. 3,5,7,10,10 can make a straight
    with hole cards of 4 and 6.  Return hole cards for highest straight or None
    """
    inRange = 0
    for card in commCards:
        if card <= highCard and card >= highCard - 5:
            inRange += 1
    print inRange


    
