# -*- coding: utf-8 -*-
"""
Code to simulate a game of old maid
Practice on classes and inheretance
Some code copied from my solitaire.py script

@author: kschultze
"""
import random

class Card():
    #define attribute list for suit and rank, aces low
    rankList = ['foo', 'Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']
    suitList = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
            
    def __init__(self,rank,suit):
        """
        rank: int... 4 = 4, King = 13, Ace = 14
        suit: int... 0 = clubs, 1 = diamonds, 2 = hearts, 3 = spades
        """
        self.rank = rank
        self.suit = suit
        if self.suit == 1 or self.suit == 2:
            self.color = 'red'
        else: self.color = 'black'
        
    def __str__(self):
        return self.rankList[self.rank] + ' of ' + self.suitList[self.suit]

    def __eq__(self, other):
        return self.rank == other.rank and self.suit == other.suit

# what if I would have started with Deck(list) and gotten all the list methods for free? 
# all that would be left is __init__, __str__, shuffle.  probably would be good to add addCard and removeCard for clarity
# can you add additional attributes then?  like deck.numCards?
class Deck():
    """
    Creates an instance of deck, populated with an orderd, standard 52-card deck
    dealing done from 'bottom' of the deck (end of the list)
    adding to the deck done to 'top' of the deck (beginning of the list)
    """
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                self.cards.append(Card(rank, suit))
    
    def __str__(self):
        cardString = 'A deck of cards containing: \n'
        for card in self.cards:
            cardString = cardString + card.__str__() + '\n'
        return cardString
        
    def __iter__(self):
        self.n = 0
        return self
    def next(self):
        if self.n >= len(self.cards):
            raise StopIteration
        self.n += 1
        return self.cards[self.n - 1]

    def __getitem__(self, index):
        return self.cards[index]
    
    def __len__(self):
        return len(self.cards)
    
    def shuffle(self):
        for i in range(len(self.cards)):
            randIndex = random.randint(0,len(self.cards)-1)
            randCard = self.cards[randIndex]
            tempCard = self.cards[i]
            self.cards[i] = randCard
            self.cards[randIndex] = tempCard

    #add list of cards or an individual card
    def addCards(self, cards):
        if type(cards) != list:
            self.cards = [cards] + self.cards
        else:
            self.cards = cards + self.cards
            
    def popCard(self):
        return self.cards.pop()
        
    def removeCard(self, cardToRemove):
        #currently doesn't do anything if the requested card isn't present
#        print '\t removeCard'
        for i in range(len(self.cards)):
            if self.cards[i] == cardToRemove:
                del self.cards[i]
                return
        print 'WARNING: card for removal not present'
        
    def dealCards(self, hands, numCards = 999):
        """
        hands (list of Hands): list with the number of Hand objects to deal to
        numCards (int): number of cards to each player.  Deals entire deck by default
        """
        numCards = numCards*len(hands)
        numPlayers = len(hands)
        playerID = 0
        while True:
            if numCards == 0 or self.cards == []:
                break
            currentHand = hands[playerID % numPlayers]
            currentHand.addCards(self.popCard())
            numCards -= 1
            playerID += 1            
    
class Hand(Deck):
    def __init__(self, name = '', cards = []):
        cards = list(cards)
        self.cards = cards
        self.name = name
    
    def __str__(self):
        cardString = Deck.__str__(self)[6:]
        if self.name != '':
            return self.name + ': Hand' + cardString
        return 'Hand' + cardString

class CardGame():
    """
    creates CardGame object:
        creates a standard, shuffled deck and deals out numCards to each hand
        playerHands: list of Hand objects with names 'hand1, hand2, etc'
        deck: leftover cards (if any) after dealing a shuffled deck
    """
    stdDeck = Deck()
    
    def __init__(self, numPlayers, numCards = 999, deck = stdDeck):
        self.numPlayers = numPlayers
        self.numCards = numCards
        self.deck = deck
        
        self.playerHands = []
        for i in range(self.numPlayers):            
            self.playerHands.append(Hand('hand' + str(i)))

        self.deck.shuffle()
        self.deck.dealCards(self.playerHands, self.numCards)
    
    def __str__(self):
        if self.deck.cards == []:
            return "CardGame object: " + str(self.numPlayers) + ' hands with all cards dealt from deck'
        else:
            return ("CardGame object: " + str(self.numPlayers) + ' hands with ' + str(self.numCards) +
                ' cards; ' + str(52 - self.numCards*self.numPlayers) + ' cards left in deck')

#Everything above should be pretty general to most card games, below is specific to Old Maid
        

class OldMaidGame(CardGame):
    
    def __init__(self, numPlayers):
        oldMaidDeck = Deck()
        oldMaidDeck.removeCard(Card(12,0))
        CardGame.__init__(self, numPlayers, 999, oldMaidDeck)
        self.removedPairs = 0
        
    def __str__(self):
        return 'OldMaidGame' + CardGame.__str__(self)[8:]
        
    def removeMatches(self, hand):
        handCopy = hand[:]
        for card in handCopy:
            cardMatch = Card(card.rank, 3 - card.suit)
            if cardMatch in hand:
                self.removedPairs += 1
                print str(self.removedPairs) + ' pairs removed'
                hand.removeCard(card)
                hand.removeCard(cardMatch)
    
    def playGame(self):
        for hand in self.playerHands: self.removeMatches(hand)
        print '\n-------- initial discard done\n'
        currentPlayer = 0
        drawFrom = self.numPlayers - 1
        while True:
            if len(self.playerHands[currentPlayer]) != 0:
                while len(self.playerHands[drawFrom]) == 0:
                    drawFrom = (drawFrom - 1) % self.numPlayers
                if drawFrom == currentPlayer:
                    print 'Player with ' + str(self.playerHands[currentPlayer].name) + ' loses!'
                    return currentPlayer
                
                self.playerHands[drawFrom].shuffle()
                drawnCard = self.playerHands[drawFrom].popCard()
                self.playerHands[currentPlayer].addCards(drawnCard)
                self.removeMatches(self.playerHands[currentPlayer])

            currentPlayer = (currentPlayer + 1) % self.numPlayers
            drawFrom = (currentPlayer - 1) % self.numPlayers

#here is the syntax for creating a modified version of list while populating it in __init__
class NewList(list):
    def __init__(self, item = [], name = 'generic name'):
        list.__init__(self, item)
        self.name = name
        