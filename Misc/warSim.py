# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 17:47:24 2018

@author: kschultze

simulates a game of war with standard 52 card deck
"""
import random
import copy

standardDeck = [2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,11,11,11,11,12,12,12,12,13,13,13,13,14,14,14,14]

def shuffle(deck):
    deckCopy = deck[:]
    shuffledDeck = []
    for i in range(len(deck)):
        randIndex = random.randint(0,len(deckCopy)-1)
        randCard = deckCopy.pop(randIndex)
        shuffledDeck.append(randCard)
    return shuffledDeck

def dealDeck(deck,numPlayers = 2):
    """
    input a deck (list of card values) and number of players and it will deal them out to the players.
    output dictionary playerNum:list of card values
    """
    players = {}
    for i in range(numPlayers):
        players[i] = []
    playerNum = 0
    for card in deck:
        players[playerNum].append(card)
        playerNum = (playerNum +1)%numPlayers
    return players

def tieCard(hands,card0,card1):
    """
    finds the winner of a tied turn of war and appends cards to the correct hand
    """
    try:
        card0.append(hands[0].pop(0))
        card0.append(hands[0].pop(0))
        card0.append(hands[0].pop(0))
    except IndexError:
        hands[1] += card0  #put all cards in player 0's hand.  not really necessary but makes it so cards don't 'dissapear'
        hands[0] = []   #remove all cards and player 0 loses
        return hands
        
    try:
        card1.append(hands[1].pop(0))
        card1.append(hands[1].pop(0))
        card1.append(hands[1].pop(0))
    except IndexError:
        hands[1] = []   #remove all cards and player 1 loses
        hands[0] += card1  #put all cards in player 0's hand.  not really necessary but makes it so cards don't 'dissapear'
        hands[0] += card0  
        return hands

    #compare last card of the 3
    cards = shuffle(card0 + card1)
    if card0[-1] > card1[-1]:
        hands[0] += cards
    elif card1[-1] > card0[-1]:
        hands[1] += cards
    else: tieCard(hands,card0,card1)
    return hands
    
def playWar(players):
    hands = copy.copy(players)
    for i in range(100000):
        #each player lays down a card
        try: card0 = [hands[0].pop(0)]    #remove first card in hand           
        except IndexError:
            #print 'Player 1 Wins!'
            return 1,i
        try: card1 = [hands[1].pop(0)]    #remove first card in hand           
        except IndexError:
            #print 'Player 0 Wins!'
            return 0,i
        
        #compare cards
        cards = shuffle(card0 + card1)
        if card0[0] > card1[0]:
            hands[0] += cards
        elif card1[0] > card0[0]:
            hands[1] += cards
        else: hands = tieCard(hands,card0,card1)

#pit one player with only the 4 aces against another with a random shuffle of the remaining cards        
noAces = standardDeck[0:-4]
numGames = 1000
acesLose = 0
turns = []
for i in range(numGames):
    players = {}
    players[0] = [14,14,14,14]  #all aces
    players[1] = shuffle(noAces)
    winner,cycles = playWar(players)
    turns.append(cycles)
    acesLose += winner
    
winPercent = 1 - acesLose/float(numGames)
print winPercent

#fair shuffle
#numGames = 10000
#playerLose = 0
#turns = []
#for i in range(numGames):
#    players = dealDeck(shuffle(standardDeck))
#    winner,cycles = playWar(players)
#    turns.append(cycles)
#    playerLose += winner
#    
#winPercent = 1 - playerLose/float(numGames)
#print winPercent

#a standard game where player0 ends up with all aces
#noAces = standardDeck[0:-4]
#numGames = 10000
#acesLose = 0
#for i in range(numGames):
#    players = {}
#    deck = shuffle(noAces)
#    players = dealDeck(deck)            #deal with no aces
#    players[1] += players[0][0:4]       #add 4 from Aces to noAces
#    players[0][0:4] = [14,14,14,14]     #replace those 4 with Aces in Aces
#    players[0] = shuffle(players[0])    #reshuffle Aces
#    players[1] = shuffle(players[1])    #reshuffle noAces
#    winner = playWar(players)
#    acesLose += winner
#winPercent = 1 - acesLose/float(numGames)
#print winPercent
    

            
#deck = shuffle(standardDeck)
#players = dealDeck(deck)
#players = {}
#players[0] = [5,4,3,9,5,6,6,3,4,5]
#players[1] = [5,5,8,9,5,2,6,7,4,3]
#playWar(players)

