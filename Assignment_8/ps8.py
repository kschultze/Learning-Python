# 6.00 Problem Set 8
#
# Intelligent Course Advisor
#
# Name:
# Collaborators:
# Time:
#

import time

SUBJECT_FILENAME = "subjects.txt"
VALUE, WORK = 0, 1
maxWork = 7
bruteForceTime()
dpTime()    

#
# Problem 1: Building A Subject Dictionary
#
def loadSubjects(filename):
    """
    Returns a dictionary mapping subject name to (value, work), where the name
    is a string and the value and work are integers. The subject information is
    read from the file named by the string filename. Each line of the file
    contains a string of the form "name,value,work".

    returns: dictionary mapping subject name to (value, work)
    """
    inputFile = open(filename)
    subDict = {}
    for line in inputFile:
        line = line.strip()
        splitList = line.split(',')
        
        subDict[splitList[0]] = (int(splitList[1]),int(splitList[2]))
       
    return subDict        

def printSubjects(subjects):
    """
    Prints a string containing name, value, and work of each subject in
    the dictionary of subjects and total value and work of all subjects
    """
    totalVal, totalWork = 0,0
    if len(subjects) == 0:
        return 'Empty SubjectList'
    res = 'Course\tValue\tWork\n======\t====\t=====\n'
    subNames = subjects.keys()
    subNames.sort()
    for s in subNames:
        val = subjects[s][VALUE]
        work = subjects[s][WORK]
        res = res + s + '\t' + str(val) + '\t' + str(work) + '\n'
        totalVal += val
        totalWork += work
    res = res + '\nTotal Value:\t' + str(totalVal) +'\n'
    res = res + 'Total Work:\t' + str(totalWork) + '\n'
    print res

def cmpValue(subInfo1, subInfo2):
    """
    Returns True if value in (value, work) tuple subInfo1 is GREATER than
    value in (value, work) tuple in subInfo2
    """
    val1 = subInfo1[VALUE]
    val2 = subInfo2[VALUE]
    return  val1 > val2

def cmpWork(subInfo1, subInfo2):
    """
    Returns True if work in (value, work) tuple subInfo1 is LESS than than work
    in (value, work) tuple in subInfo2
    """
    work1 = subInfo1[WORK]
    work2 = subInfo2[WORK]
    return  work1 < work2

def cmpRatio(subInfo1, subInfo2):
    """
    Returns True if value/work in (value, work) tuple subInfo1 is 
    GREATER than value/work in (value, work) tuple in subInfo2
    """
    val1 = subInfo1[VALUE]
    val2 = subInfo2[VALUE]
    work1 = subInfo1[WORK]
    work2 = subInfo2[WORK]
    return float(val1) / work1 > float(val2) / work2

#
# Problem 2: Subject Selection By Greedy Optimization
#
def greedyAdvisor(subjects, maxWork, comparator):
    """
    Returns a dictionary mapping subject name to (value, work) which includes
    subjects selected by the algorithm, such that the total work of subjects in
    the dictionary is not greater than maxWork.  The subjects are chosen using
    a greedy algorithm.  The subjects dictionary should not be mutated.

    subjects: dictionary mapping subject name to (value, work)
    maxWork: int >= 0
    comparator: function taking two tuples and returning a bool
    returns: dictionary mapping subject name to (value, work)
    """
    subCopy = subjects.copy() #don't mutate subjects
    subNames = subCopy.keys()
    subNames.sort() #not strictly needed, just easier to debug if ordered
    selected = {}
    totalWork = 0
    while totalWork <= maxWork:
        currentChamp = subNames[0]
        for i in range(1,len(subNames)):
            challenger = subNames[i]
            champWins = comparator(subCopy[currentChamp],subCopy[challenger])
            if not champWins:
                currentChamp = challenger
        totalWork += subCopy[currentChamp][WORK]
        if totalWork <= maxWork:
            selected[currentChamp] = subCopy[currentChamp]
            subNames.remove(currentChamp)
    printSubjects(selected)
    return selected         


def bruteForceAdvisor(subjects, maxWork):
    """
    Returns a dictionary mapping subject name to (value, work), which
    represents the globally optimal selection of subjects using a brute force
    algorithm.

    subjects: dictionary mapping subject name to (value, work)
    maxWork: int >= 0
    returns: dictionary mapping subject name to (value, work)
    """
    nameList = subjects.keys()
    tupleList = subjects.values()
    bestSubset, bestSubsetValue = \
            bruteForceAdvisorHelper(tupleList, maxWork, 0, None, None, [], 0, 0)
            #note that we're passing the tupleList for the 'subjects' input into bruteForceAdvisorHelper
            #so the context of subjects changes from what is input into this function
    outputSubjects = {}
    for i in bestSubset: 
        outputSubjects[nameList[i]] = tupleList[i] #reconstruct dictionary for best classes from bestSubset index list
    printSubjects(outputSubjects)
    return outputSubjects

def bruteForceAdvisorHelper(subjects, maxWork, i, bestSubset, bestSubsetValue,
                            subset, subsetValue, subsetWork):
    #subjects is a list of tuples of value-work pairs
    #subset is the list of indexes of included 'subjects'
    # Hit the end of the list.
    if i >= len(subjects):
        if bestSubset == None or subsetValue > bestSubsetValue:
            # Found a new best.
            return subset[:], subsetValue #copy subset to avoid mutation of bestSubset
        else:
            # Keep the current best.
            return bestSubset, bestSubsetValue
    else:
        s = subjects[i]
        # Try including subjects[i] in the current working subset.
        if subsetWork + s[WORK] <= maxWork:
            subset.append(i)
            bestSubset, bestSubsetValue = bruteForceAdvisorHelper(subjects,
                    maxWork, i+1, bestSubset, bestSubsetValue, subset,
                    subsetValue + s[VALUE], subsetWork + s[WORK])
            subset.pop() #pop
        bestSubset, bestSubsetValue = bruteForceAdvisorHelper(subjects,
                maxWork, i+1, bestSubset, bestSubsetValue, subset,
                subsetValue, subsetWork)
        return bestSubset, bestSubsetValue

def bruteForceTime():
    """
    Runs tests on bruteForceAdvisor and measures the time required to compute
    an answer.
    """
    subjects = loadSubjects(SUBJECT_FILENAME)
    startTime = time.time()
    bruteForceAdvisor(subjects,maxWork)
    endTime  = time.time()
    print 'bfTime'
    print endTime - startTime


#
def dpAdvisor(subjects, maxWork):
    """
    Returns a dictionary mapping subject name to (value, work) that contains a
    set of subjects that provides the maximum value without exceeding maxWork.
    Uses a dynamic programming algorithm.

    subjects: dictionary mapping subject name to (value, work)
    maxWork: int >= 0
    returns: dictionary mapping subject name to (value, work)
    """
    subjectNames = subjects.keys()
    subjectTuple = subjects.values()
    memo = set()
    bestSubset, bestSubsetValue = dpAdvisorHelper(subjectTuple, maxWork, 0, [], 
                                                  0, 0, None, 0, memo)
    outputSubjects = {}
    for i in bestSubset:
        outputSubjects[subjectNames[i]] = subjectTuple[i]
    printSubjects(outputSubjects)
    return outputSubjects

def dpAdvisorHelper(valueWork, maxWork, i, subset, 
                    subsetValue, subsetWork, bestSubset, bestSubsetValue, memo):
    #valueWork is tuple of value-work for each class, i is level of tree
    #subset/bestSubset are lists of indeces referring back to subjectNames/subjectTuple lists
    
    #made it to bottom of tree
    if i >= len(valueWork):
        #found new best
        if bestSubset == None or subsetValue > bestSubsetValue:
            return subset[:], subsetValue #important to copy subset to avoid mutating bestSubset
        #not better, keep current best
        else:
            return bestSubset,bestSubsetValue
    #subproblem already solved and optimized, can skip lower branches of tree
    elif (i,subsetWork, subsetValue) in memo: 
        return bestSubset, bestSubsetValue
            
    #continue down tree by adding valueWork(i) in one branch and not in the other
    else:
        s = valueWork[i]
        if s[WORK] + subsetWork <= maxWork:
            subset.append(i)
            memo.add((i,subsetWork, subsetValue))
            bestSubset, bestSubsetValue = dpAdvisorHelper(valueWork, maxWork, i+1, subset, 
                            subsetValue + s[VALUE], subsetWork + s[WORK], bestSubset, bestSubsetValue, memo)
            subset.pop()
        memo.add((i,subsetWork,subsetValue))
        bestSubset, bestSubsetValue = dpAdvisorHelper(valueWork, maxWork, i+1, subset,
                        subsetValue, subsetWork, bestSubset, bestSubsetValue, memo)
        #print bestSubset, bestSubsetValue
        return bestSubset, bestSubsetValue

#
# Problem 5: Performance Comparison
#
def dpTime():
    """
    Runs tests on dpAdvisor and measures the time required to compute an
    answer.
    """
    subjects = loadSubjects(SUBJECT_FILENAME)
    startTime = time.time()
    dpAdvisor(subjects,maxWork)
    endTime  = time.time()
    print 'dpTime'
    print endTime - startTime
