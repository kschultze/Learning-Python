# -*- coding: utf-8 -*-
"""
Created on Sun Jun 17 14:41:59 2018

@author: kschultze
"""
import random
import numpy
import pylab

class Tile(object):
    def __init__(self, idNum, state = 'down'):
        if not((state == 'up') or (state == 'down')):  #there's got to be a better way to do this
            raise AttributeError("Tile state must be 'up' or 'down'")
        if type(idNum) != int:
            raise TypeError('Tile idNum must be of type int')
        self.idNum = idNum
        self.state = state
    
    def __str__(self):
        return 'Tile number ' + str(self.idNum) + ' facing ' + self.state

    def __eq__(self, other):
        return self.idNum == other.idNum

    def flipTile(self):
        if self.state == 'up': self.state = 'down'
        else: self.state = 'up'
        
class Board(list):
    def __init__(self, tilePairs):
        tileList = []
        for i in range(tilePairs):
            tileList.append(Tile(i))
            tileList.append(Tile(i))  #one for each in a pair
        list.__init__(self, tileList)
        
    def __str__(self):
        printStr = ''
        for tile in self:
            printStr += (str(tile) + '\n')
        return printStr
        
    #not necessary for the original problem but could be helpful in the future
    def shuffle(self):
        for i in range(len(self)):
            randIndex = random.randint(0,len(self)-1)
            randCard = self[randIndex]
            tempCard = self[i]
            self[i] = randCard
            self[randIndex] = tempCard
        
def playGameRandom(tilePairs):
    """
    plays a matching game where tiles are meant to be matched
    returns time in seconds to complete game when playing at random
    flipping 2 tiles takes one second
    analyzing takes 1 second (no time to flip back)
    """  
    runTime = 0
    matches = 0
    board = Board(tilePairs)
    while matches <= tilePairs - 1:
        runTime += 1 #time to flip a potential pair
        tempBoard = board[:]  #create temporary copy so you don't pick the same tile twice
        tile1 = random.choice(tempBoard)
        tempBoard.remove(tile1)
        tile2 = random.choice(tempBoard)
        if tile1 == tile2:
            board.remove(tile1)
            board.remove(tile2)
            matches += 1
        runTime += 1
#        print tile1.idNum, tile2.idNum, matches, runTime  #debuging
    return runTime
        
def simulateGame(numGames, tilePairs, gameType):
    runTimeList = []
    for i in range(numGames):
        gameTime = gameType(tilePairs)
        runTimeList.append(gameTime)
    medTime = pylab.median(runTimeList)
    meanTime = pylab.mean(runTimeList)
    pylab.hist(runTimeList,[x*2 for x in range(400)])
    print 'meanTime: ' + str(meanTime)
    print 'medianTime: ' + str(medTime)
    return meanTime, medTime

meanList = []
medList = []   
for i in range(10):
    mean, med = simulateGame(100000, 10, playGameRandom)
    meanList.append(mean)
    medList.append(med)
print pylab.mean(meanList), pylab.std(meanList)
print pylab.mean(medList), pylab.std(medList)
