# -*- coding: utf-8 -*-
"""
Created on Thu Aug 11 22:10:52 2016

@author: Schultze
"""

def MatchPairOneSub(target, key):
    """
    returns list of instances of key string inside of target string
    includes exact matches and matches that are off by 1 char
    returns None if no matches
    """
    
    indexList = []
    for i in range(0,len(target)-len(key)+1):
        
        charMatch = 0
        for j in range(len(key)):
            if target[i + j] == key[j]:
                charMatch += 1
        if charMatch == len(key)-1:  #change to:  charMatch >= len(key)- 1 to include exact matches
            indexList += [i]
        charMatch = 0
        
    if indexList == []:
        return None
    return indexList