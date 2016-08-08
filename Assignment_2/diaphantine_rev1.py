# -*- coding: utf-8 -*-
"""
07/26/16

@Schultze

Script to calculate chicken nuggets combinations
If nuggets are sold in packs of 6, 9, and 20, what combinations are required to
get exactly n nuggets.  AKA, all solutions to the diopnantene equation:
6x + 9y + 20z = n     for a given n
"""

n = 21

A = 6
B = 9
C = 20

maxA = n//A
maxB = n//B
maxC = n//C

for numA in range(0,maxA + 1):

    for numB in range(0,maxB + 1):
        
        for numC in range(0,maxC + 1):
            total = numA*A + numB*B + numC*C
            if total == n:
                print(' ')
                print('A = ' + str(numA))
                print('B = ' + str(numB))
                print('C = ' + str(numC))