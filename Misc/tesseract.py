# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 18:38:34 2018

@author: kschultze

meant to solve the 01/26/18 fivethirtyeight.com puzzler
summary: it's a 12x12 square that is broken up into 14 shapes of different areas.
Need to figure out all the ways in which the shapes can be colored in with 4 
colors such that no touching shapes have the same color and each group of shapes
that are the same color add up to equal areas (36)

To solve it, I first created a couple new classes, shape and shapeSet to better
organize the data stored in both and create some methods to manipulate them.

First I wrote a recursive function using a binary tree method that finds all 
sets of shapes that add up to 36 and don't touch.  Then the second recursive 
function again uses a binary tree to find all combinations of these sets that 
use all 14 shapes (i.e. colors in all shapes in the original 12x12 square)
"""
import copy

"""
Section to define some custom classes that pertain to the shapes themselves and sets of shapes.
"""

class shape():
    def __init__(self,ID,area,neighbors):
        self.ID  = ID 
        self.area = area
        self.neighbors = neighbors
    def __str__(self):
        return 'Shape #' + str(self.ID) + '\nArea: ' + str(self.area) + ' \nNeighbors: ' + str(self.neighbors)

class shapeSet():
    def __init__(self):
        self.areaSum = 0
        self.neighborList = []
        self.IDs = []
        self.shapeList = []
    def __add__(self,other):      
        self.areaSum += other.area
        self.neighborList += list(other.neighbors)
        self.IDs.append(other.ID)
        self.shapeList.append(other)
        return self
    def pop(self):
        self.areaSum -= self.shapeList[-1].area
        self.IDs.pop()
        popShape = self.shapeList[-1]
        for i in range(len(popShape.neighbors)):
            self.neighborList.pop()
        self.shapeList.pop()
    def __str__(self):
        return str(self.IDs) + '\t' + str(self.areaSum)

"""
set of functions to find all sets of shapes whose areas both add up to 36 and have no shapes in the 
set that touch any other in the set
note: would be more explicit if I returned currentSet along with setList in findSets
"""

def addOK(currentSet,newShape):
    totalArea = currentSet.areaSum + newShape.area
    touching = newShape.ID in currentSet.neighborList
    return totalArea <= 36 and not touching

def findSets(shapes,i,currentSet,setList):
    #reached the end of the shapeList
    if i >= len(shapes):
        if currentSet.areaSum == 36:
            setList.append(copy.deepcopy(currentSet))
            return setList
        else: return setList
    if currentSet.areaSum == 36:
        setList.append(copy.deepcopy(currentSet))
        return setList

    if addOK(currentSet,shapes[i]):
        currentSet = currentSet + copy.deepcopy(shapes[i])
        setList = findSets(shapes, i+1, currentSet,setList)
        currentSet.pop()
    setList = findSets(shapes, i+1, currentSet,setList)
    return setList
    
"""
set of functions to take in all the sets of valid shapes found above and figure out which combinations
of those fit together to use all 14 shapes
note: would be more explicit if I returned currentSet along with fullSets in testSets
"""
    
def goodSet(sets):
    correctSet = range(14)
    setList = [item for sublist in sets for item in sublist]
    setList.sort()
    return setList == correctSet

def addOK2(currentSet,testSet):
    overlap = False
    flatSet = [item for sublist in currentSet for item in sublist]
    for item in testSet:
        if item in flatSet:
            overlap = True
    return not overlap

def testSets(possibleSets,i,currentSet,fullSets):
#    print currentSet
    if i >= len(possibleSets):
        if goodSet(currentSet):
            fullSets.append(currentSet[:])
            return fullSets
        else: return fullSets
        
    if goodSet(currentSet):
        fullSets.append(currentSet[:])
        return fullSets
    
    if addOK2(currentSet,possibleSets[i]):
        currentSet.append(possibleSets[i])
        testSets(possibleSets,i+1,currentSet,fullSets)
        currentSet.pop()
    testSets(possibleSets,i+1,currentSet,fullSets)
    return fullSets

"""
start of script
"""

areas = (21,6,3,12,12,12,6,12,6,12,6,9,3,24)
neighbors = ((2,3,6,8),(2,3),(0,1,3),(0,1,2,4,5),(3,5),(3,4,6),(0,5,7),(6,8,10,13),(0,7,9),(8,10),(7,9,11),(10,12),(11,13),(7,12))

#areas = (10,10,26,26)
#neighbors = ((1,2),(0,3),(0,3),(1,2))

#generate shape objects from areas and neighbors lists    
shapes = ()
for i in range(len(areas)):
    shapes += (shape(i,areas[i],neighbors[i]),)
setList = findSets(shapes,0,shapeSet(),[])

possibleSets = ()
for i in setList:
    possibleSets += (i.IDs,)
    
fullSets = testSets(possibleSets,0,[],[])
for i in fullSets:
    print i