# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 19:54:00 2017

@author: kschultze

function to solve the tower of hanoi problem
you have 3 towers and need to move a stack of disks from one tower to the other
Can only move one disk at a time
Can never place a larger disk onto a smaller one
"""

def towerOfHanoi(size, fromStack, toStack, spareStack):
    """
    function takes in the size of the stack you want to move, the number tower
    the stack is currently on, the number of the tower you want to move it to, 
    and the number of the spare tower. Prints steps needed to complete and 
    returns total number of steps
    """
    
    if size == 1:
        print('move from stack', fromStack, 'to stack', toStack)
        return 1
    else:
        return (towerOfHanoi(size-1, fromStack, spareStack, toStack) + 
                towerOfHanoi(1, fromStack, toStack,spareStack) + 
                towerOfHanoi(size-1, spareStack, toStack, fromStack))