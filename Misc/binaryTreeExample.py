# -*- coding: utf-8 -*-
"""
Created on Thu Feb 01 19:20:54 2018

This is intended to be a general example of how you do a recursive implementation
of a binary tree (depth first).  Here we have a set of numbers and want to output all the combinations
of those numbers that add up to 7.  Binary trees can be amenable to dynamic programming,
especially if you're trying to optimize a condition rather than exhaustively search
through combinations as in this case.

It should be noted that it is not strictly necessary for searchCombos2 to return comboSets and currentCombo.
These are both created in the top level call of searchCombos2 in searchCombos and are simply mutated
in lower recursive calls.  However, explicitly passing those instances through the recursive calls makes
it clearer as to what is happening in the function.

Also, the top-level searchCombos function is not strictly needed either but hides several needed variables
making the function call cleaner.  You could also add in control for what 'sum' you want to look for. Then
the function call would look like 'searchCombos(numberPool,7)' and be a bit more generalized

@author: kschultze
"""

def searchCombos(numberPool):
    i = 0  #level of tree
    comboSets = []
    currentCombo = []
    comboSets,currentCombo = searchCombos2(numberPool,i,comboSets,currentCombo)
    return comboSets
    
def searchCombos2(numberPool,i,comboSets,currentCombo):
#    print comboSets
#    print currentCombo
    #check if you've hit your end condition
    if goodCombo(currentCombo):
        comboSets.append(currentCombo[:]) #create copy!! or lose during currentCombo.pop() line
        return comboSets,currentCombo
    #check if you've reached the bottom of the tree
    if i >= len(numberPool):
        if goodCombo(currentCombo):  #don't acutally think I need this if-statement but haven't fully thought it through yet
            comboSets.append(currentCombo[:]) #create copy!! or lose during currentCombo.pop() line
            return comboSets
        return comboSets,currentCombo
    #probe branch #1    
    if addOK(currentCombo,numberPool[i]):
        currentCombo.append(numberPool[i])
        comboSets,currentCombo = searchCombos2(numberPool,i+1,comboSets,currentCombo)
        currentCombo.pop()
    #probe branch #2
    comboSets,currentCombo = searchCombos2(numberPool,i+1,comboSets,currentCombo)
    return comboSets,currentCombo

def goodCombo(combo):
    return sum(combo) == 7

def addOK(currentCombo,newEntry):
    newSum = sum(currentCombo) + newEntry
    return newSum <= 7

numberPool = [1,2,3,4,5]
x = searchCombos(numberPool)