# -*- coding: utf-8 -*-
"""
07/26/16

@Schultze

Script to calculate chicken nuggets combinations
Using an iterated version of diaphantine2_rev1.py, this code finds the largest
value for n for which no combination of A, B, and C exist.
"""

A = 6
B = 9
C = 20

isPossible = ()

for n in range(1,200):
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
        
    if sum(isPossible[-6:]) == 6:
        print ('Largest number of McNuggets that cannot be bought in exact quantity: ' + str(n-6))
        break