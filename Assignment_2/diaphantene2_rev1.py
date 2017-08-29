# -*- coding: utf-8 -*-
"""
07/26/16

@Schultze

Script to calculate chicken nuggets combinations
If nuggets are sold in packs of 6, 9, and 20, what combinations are required to
get exactly n nuggets.  AKA, all solutions to the diopnantene equation:
6A + 9B + 20C = n     for a given n

This is an update to diahpantene_rev1.py in which it calculates the largest number
of nuggets that can't be bought with the combination 6, 9, and 20.
"""

A = 6
B = 9
C = 20
maxTest = 200

isPossible = ()

for n in range(1,maxTest+1):
    maxA = n//A
    maxB = n//B
    maxC = n//C
    match = False
    
    for numA in range(0,maxA + 1):
    
        for numB in range(0,maxB + 1):
            
            for numC in range(0,maxC + 1):
                total = numA*A + numB*B + numC*C
                if total == n:
                    match = True
    
    if match:
        isPossible += (1,)
    else:
        isPossible += (0,)  
        
    if sum(isPossible[-6:]) == 6: #as long as 6 in a row are found, any greater combination can be found
        print ('Largest number of McNuggets that cannot be bought in exact quantity: ' + str(n-6))
        break
    if n == maxTest:
        print('No result found up to ' + str(maxTest) + ' McNuggets, try increasing maxTest')