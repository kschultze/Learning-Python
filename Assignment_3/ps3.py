from string import *

"""
first 2 functions are iterative and recursive versions to find all instances of
a key string inside a target string.  Overall should be pretty straightforward 
and robust

the next 2 functions, constrainedMatchPair and subStringMatchOneSub, are a 
stupid way to find all instances of a key string inside of a target string with
one or zero char mismatches.  This is the general method the class notes wanted
us to use.  It works and I learned a lot doing it, but I came up with a MUCH 
simpler method of doing it which can be found in the sub1Match.py script.

one improvement I could make is that I don't have good type discipline for 
match1 and match2 (string in one case, tuple in another).  I should make a 
separate "flag" variable that passes to constrainedMatchPair and is only ever a
string, leaving match 1 and 2 to be always tuples (or None).  Not going to
bother changing it at this time, just wanted to make note.
"""

target1 = 'atgacatgcacaagtatgcat'
target2 = 'atgaatgcatggatgtaaatgcag'

# key strings

key10 = 'a'
key11 = 'atg'
key12 = 'atgc'
key13 = 'atgca'
key14 = ''
key15 = 7



def findAll(target, key, start = 0):
    """
    Returns tuple of indeces of substring locations in a string.
    Returns None if no instances found or key is empty string.   
    """
    import string
    assert isinstance(target,basestring), 'target must be a string'
    assert isinstance(key,basestring), 'key must be a string'
    if key == '': return None
    
    index = string.find(target,key,start)
    if index == -1:
        return None
    indexList = ()
    while index != -1:
        indexList += (index,)
        index = string.find(target,key,index + 1) #will find instances of overlapping key strings in target
    return indexList
    
##test code
#print(findAll(target1,key10))
#print(findAll(target1,key11))
#print(findAll(target1,key12))
#print(findAll(target1,key13))
#print(findAll(target1,key14))
#print(findAll(target1,key15))
#print(findAll(target1,'xyz'))
#
#print(findAll(target2,key10))
#print(findAll(target2,key11))
#print(findAll(target2,key12))
#print(findAll(target2,key13))

def findAllRecursive(target, key, start = 0):
    """
    Returns tuple of indeces of substring locations in a string.
    Returns None if no instances found or key is an empty string.
    """
    import string
    assert isinstance(target,basestring), 'target must be a string'
    assert isinstance(key,basestring), 'key must be a string'
    if key == '': return None
    
    if string.find(target, key,start) == -1:  #base case
         return None
         
    else:                               #recursive step
        index = string.find(target,key,start)
        indexList = findAllRecursive(target, key,index + 1)  #recursion     
        
        if indexList == None:  #gets rid of the 'None' passed in the base case
               indexList = ()
        return (index,) + (indexList)

##test code
#print(findAllRecursive(target1,key10))
#print(findAllRecursive(target1,key11))
#print(findAllRecursive(target1,key12))
#print(findAllRecursive(target1,key13))
#print(findAllRecursive(target1,key14))
#print(findAllRecursive(target1,key15))
#print(findAllRecursive(target1,'xyz'))
#
#
#print(findAllRecursive(target2,key10))
#print(findAllRecursive(target2,key11))
#print(findAllRecursive(target2,key12))
#print(findAllRecursive(target2,key13))
#print(findAllRecursive(target2,key14))
#print(findAllRecursive(target2,key15))


def constrainedMatchPair(firstMatch,secondMatch,length,target):
    """ for use in subStringMatchOneSub
        takes in two tuples from matching 2 halves of a possible string match 
        with 1 substitution along with the length of first string section and 
        returns tuple with values that are actually matches"""
    print('constrainedMatchPair starting')
    matchedPairs = ()
    
    if firstMatch == None or secondMatch == None: return ()
    if firstMatch == 'firstMiss': #substitution is the first char of key
        matchedPairs = [x-1 for x in secondMatch]
        if -1 in matchedPairs: matchedPairs.remove(-1) #removes false match at beginning
        return tuple(matchedPairs)
    if secondMatch == 'lastMiss': # substituiton is last char of key
        matchedPairs = firstMatch
        if len(target)-length in matchedPairs: matchedPairs = matchedPairs[:-1] #removes false match at end
        return matchedPairs
    for i in firstMatch:
        for j in secondMatch:
            if i + length + 1 == j: 
                matchedPairs += (i,)
    return matchedPairs

##test code
#print(constrainedMatchPair(None,(1,6,58),5))
#print(constrainedMatchPair((1,6,58),None,5))
#print(constrainedMatchPair((1,5,43,52,64), (2,3,45,66),1))

def subStringMatchOneSub(target,key):
    """search for all locations of key in target, with one substitution"""
    assert isinstance(target,basestring), 'target must be string'
    assert isinstance(key,basestring), 'key must be string'
    if key == '': return None
    if len(key) == 1: return tuple(range(len(target))) #technically everything is a match
    allAnswers = ()
    for miss in range(0,len(key)):
        # miss picks location for missing element
        # key1 and key2 are substrings to match
        key1 = key[:miss]
        key2 = key[miss+1:]
#        print 'breaking key',key,'into',key1,key2
        # match1 and match2 are tuples of locations of start of matches
        # for each substring in target
        if key1 == '': match1 = 'firstMiss' #flag this special case for later
        else:
            match1 = findAll(target,key1)
        if key2 == '': match2 = 'lastMiss' #flag this special case for later
        else:
            match2 = findAll(target,key2)
        # when we get here, we have two tuples of start points
        # need to filter pairs to decide which are correct
        filtered = constrainedMatchPair(match1,match2,len(key1),target)
        allAnswers = allAnswers + filtered
#        print 'match1',match1
#        print 'match2',match2
#        print 'possible matches for',key1,key2,'start at',filtered
    if allAnswers == (): return None
    allAnswers = sorted(set(allAnswers)) #remove duplicates and sort
    return allAnswers
        
#print(subStringMatchOneSub(target1,key10))
#print(subStringMatchOneSub(target1,key11))
#print(subStringMatchOneSub(target1,key12))
#print(subStringMatchOneSub(target1,key13))
#print(subStringMatchOneSub(target1,'xyz'))
#print(subStringMatchOneSub(target1,key14))
#print(subStringMatchOneSub(target1,key15))
#
#print(subStringMatchOneSub(target2,key10))
#print(subStringMatchOneSub(target2,key11))
#print(subStringMatchOneSub(target2,key12))
#print(subStringMatchOneSub(target2,key13))


    







            



