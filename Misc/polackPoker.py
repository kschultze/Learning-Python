# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 17:34:25 2017

@author: kschultze
"""
import numpy
import random
import copy

def rollDice(player, playerNames, numPlayers, quarters):
    """
    prompt user to input the roll and adjust everyone's quarters
    
    inputs
        player - int = index of player rolling
        quarters - list = list of quarters each player has
    returns
        quarters2 - list = updated quarters list
    """
    quarters2 = copy.copy(quarters)
    leftPlayer = (player + 1)%numPlayers
    rightPlayer = (player - 1)%numPlayers
    roll = raw_input("Enter %s's roll (no spaces)\n" %playerNames[player])
    for i in roll:
        if i == '4':
            quarters2[player] = quarters2[player] - 1
        elif i == '5':
            quarters2[player] = quarters2[player] - 1
            quarters2[leftPlayer] = quarters2[leftPlayer] + 1
        elif i == '6':
            quarters2[player] = quarters2[player] - 1
            quarters2[rightPlayer] = quarters2[rightPlayer] + 1
        else:
            pass
        return quarters2


def playPP(numPlayers, playerNames = 'default'):
    """
    input player names as a list of strings in the order they will play
    """
    if playerNames == 'default':
        playerNames = [str(x + 1) for x in range(numPlayers)]

    quarters = [3]*numPlayers
    playersLeft = len([x for x in quarters if x > 0])
    player = numPlayers - 1
    while True:
        while playersLeft > 1:
            player = (player + 1)%numPlayers #modular division - cycles through players
            if quarters[player] > 0:
                #rollDice(player, playerNames, numPlayers, quarters)
                quarters = autoRoll(player, numPlayers, quarters)
            playersLeft = len([x for x in quarters if x > 0])
            
        player = int(numpy.nonzero(quarters)[0]) #select player with quarter(s) remaining
        #rollDice(player, playerNames, numPlayers, quarters)  #final roll for win
        quarters = autoRoll(player, numPlayers, quarters)
        playersLeft = len([x for x in quarters if x > 0])
        if playersLeft <= 0:
            #print 'no Winner'  #todo, restart game for 'double pot' scenario
            return -1
        elif playersLeft == 1 and player == int(numpy.nonzero(quarters)[0]): #player rolled safe and wins
            #print 'Player %s wins!' %playerNames[player]
            return player
        else:
            #passes to next player for final roll or back to while loop if more than 1 person has quarters
            pass


def autoRoll(player, numPlayers, quarters):
    
    quarters2 = copy.copy(quarters) #avoid mutating original
    leftPlayer = (player + 1)%numPlayers
    rightPlayer = (player - 1)%numPlayers
    roll = []
    #only roll the same number of dice as quarters player has
    for i in range(quarters2[player]):
        roll.append(random.randint(1,6))
    #print roll    
    for i in roll:
        if i == 4:
            quarters2[player] = quarters2[player] - 1
        elif i == 5:
            quarters2[player] = quarters2[player] - 1
            quarters2[leftPlayer] = quarters2[leftPlayer] + 1
        elif i == 6:
            quarters2[player] = quarters2[player] - 1
            quarters2[rightPlayer] = quarters2[rightPlayer] + 1
        else:
            pass
    return quarters2
    
def singleQuarter(numPlayers, numRounds):
    
    numWins = (numPlayers + 1)*[0] #last entry is when no player wins
    for i in range(numRounds):
        winner = None
        quarters = [0]*numPlayers
        quarters[0] = 1
        player = 0
        while winner == None:
            currentQuarters = copy.copy(quarters)
            quarters = autoRoll(player, numPlayers, quarters)
            #safe roll
            if quarters == currentQuarters:
                winner = player
            #rolled a 4
            elif len([x for x in quarters if x > 0]) == 0:
                winner = -1
            else: 
                player = int(numpy.nonzero(quarters)[0])
        numWins[winner] += 1
    for i in range(len(numWins)):
        numWins[i] = numWins[i]/float(numRounds) #convert to win fraction
    return numWins

#result of simulating 100 million rounds: 
#[0.53124785, 0.09370925, 0.03124571, 0.09378041, 0.25001678]
#[0.53049691, 0.09149945, 0.01828357, 0.01827123, 0.09147946, 0.24996938]
#[0.53034319, 0.09105486, 0.01605794, 0.00535664, 0.01607882, 0.09110872, 0.24999983]
#[0.53040645, 0.09099703, 0.01572068, 0.00313416, 0.00313112, 0.01568113, 0.0910056, 0.24992383]
#[0.53033638, 0.09099488, 0.01563257, 0.00275938, 0.0009247, 0.00275334, 0.01562248, 0.09095831, 0.25001796]

def repeatFullGames(numPlayers,numRounds):
    numWins = (numPlayers + 1)*[0] #last entry is when no player wins
    winner = None
    for i in range(numRounds):
        winner = playPP(numPlayers)
        numWins[winner] += 1
    for i in range(len(numWins)):
        numWins[i] = numWins[i]/float(numRounds) #convert to win fraction
    return numWins


#for numPlayers in [3,4,5,6,7,8]:
#    results = repeatFullGames(numPlayers, 1000000)
#    print numPlayers
#    print results
