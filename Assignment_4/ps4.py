# Problem Set 4
# Name: 
# Collaborators: 
# Time: 

#
# Problem 1
#

def nestEggFixed(salary, fracSave, growthRate, years):
    """
    - salary: the amount of money you make each year.
    - fracSave: the percent of your salary to save in the investment account each
      year (an fraction (float) between 0 and 1).
    - growthRate: the annual fractional(percent/100) increase in your investment
      (can be positive or negative).
    - years: the number of years to work.
    - return: a list whose values are the size of your retirement account at
      the end of each year.
    """
    assert salary >= 0, 'salary must be non-negative'
    assert fracSave >= 0 and fracSave <= 1, 'fracSave must be between 0 and 1'
    assert isinstance(growthRate,float) or isinstance(growthRate,int), 'growthRate must be int or float'
    assert isinstance(years,int) and years > 0, 'years must be a positive integer'
    
    valueList = [float(salary*fracSave)]
    for i in range(0, years - 1):
        valueList = valueList + [valueList[-1]*(1 + growthRate) + salary*fracSave]
    return valueList
    
    

def testNestEggFixed():
    salary     = 10000
    fracSave   = 0.1
    growthRate = 0.15
    years      = 5
    savingsRecord = nestEggFixed(salary, fracSave, growthRate, years)
    print savingsRecord
    # Output should have values close to:
    # [1000.0, 2150.0, 3472.5, 4993.375, 6742.3812499999995]
    salary     = 10000
    fracSave   = 0
    growthRate = 0.15
    years      = 5
    savingsRecord = nestEggFixed(salary, fracSave, growthRate, years)
    print savingsRecord
    # Output should have values close to:
    # [0.0,0.0,0.0,0.0,0.0]
    salary     = 10000
    fracSave   = 0.1
    growthRate = 0
    years      = 5
    savingsRecord = nestEggFixed(salary, fracSave, growthRate, years)
    print savingsRecord
    # Output should have values close to:
    # [1000.0, 2000.0, 3000.0, 4000.0, 5000.0]
    salary     = 10000
    fracSave   = 0.1
    growthRate = -0.1
    years      = 5
    savingsRecord = nestEggFixed(salary, fracSave, growthRate, years)
    print savingsRecord
    # Output should have values close to:
    # [1000.0, 1900.0, 2710.0, 3439.0, 4095.1]

#
# Problem 2
#

def nestEggVariable(salary, fracSave, growthRates):
    """
    - salary: the amount of money you make each year.
    - fracSave: the percent of your salary to save in the investment account each
      year (an fraction (float) between 0 and 1).
    - growthRates: a list or tuple of the annual fractional(percent/100) increase in your
      investment (can be positive or negative).
    - return: a list of your retirement account value at the end of each year.
    """
    assert salary >= 0, 'salary must be non-negative'
    assert fracSave >= 0 and fracSave <= 1, 'fracSave must be between 0 and 1'
#    assert isinstance(growthRates,float) or isinstance(growthRate,int), 'growthRate must be int or float'
    
    valueList = [float(salary*fracSave)]
    for yearlyRate in growthRates[1:]:
        valueList = valueList + [valueList[-1]*(1 + yearlyRate) + salary*fracSave]
    return valueList

def testNestEggVariable():
    salary      = 10000
    fracSave        = 0.1
    growthRates = [0.03, 0.04, 0.05, 0.0, 0.03]
    savingsRecord = nestEggVariable(salary, fracSave, growthRates)
    print savingsRecord
    # Output should have values close to:
    # [1000.0, 2040.0, 3142.0, 4142.0, 5266.2600000000002]

    salary      = 10000
    fracSave        = 0.1
    growthRates = ['a', -0.04, 0.05, 0.0, 100.03]
    savingsRecord = nestEggVariable(salary, fracSave, growthRates)
    print savingsRecord


#
# Problem 3
#

def postRetirement(savings, growthRates, expenses):
    """
    - savings: the initial amount of money in your savings account.
    - growthRates: a list or tuple of the annual fractional(percent/100) increase in your
      investment (can be positive or negative).
    - expenses: the amount of money you plan to spend each year during
      retirement.
    - return: a list of your retirement account value at the end of each year.
    """
    
    valueList = []
    for yearlyRate in growthRates:
        valueList = valueList + [savings*(1 + yearlyRate) - expenses]
        savings = valueList[-1]
    return valueList

def testPostRetirement():
    savings     = 100000
    growthRates = [0.1, 0.05, 0.0, 0.05, 0.01]
    expenses    = 30000
    savingsRecord = postRetirement(savings, growthRates, expenses)
    print savingsRecord
    # Output should have values close to:
    # [80000.000000000015, 54000.000000000015, 24000.000000000015,
    # -4799.9999999999854, -34847.999999999985]


#
# Problem 4
#

def findMaxExpenses(salary, fracSave, preRetireGrowthRates, postRetireGrowthRates,
                    epsilon):
    """
    - salary: the amount of money you make each year.
    - fracSave: the percent of your salary to save in the investment account each
      year (an integer between 0 and 100).
    - preRetireGrowthRates: a list of annual growth percentages on investments
      while you are still working.
    - postRetireGrowthRates: a list of annual growth percentages on investments
      while you are retired.
    - epsilon: an upper bound on the absolute value of the amount remaining in
      the investment fund at the end of retirement.
    """
    savingHistory = nestEggVariable(salary, fracSave, preRetireGrowthRates)
    
    expenses = savingHistory[-1]/2
    loLim = 0
    hiLim = savingHistory[-1]
    for i in range(0,500):
        spendingHistory = postRetirement(savingHistory[-1], postRetireGrowthRates, expenses)
        fundsRemain = spendingHistory[-1]
        if abs(fundsRemain) <= epsilon:
            return expenses
        elif fundsRemain > 0:
            loLim = expenses
            expenses = (expenses + hiLim)/2
        else:
            hiLim = expenses
            expenses = (expenses +loLim)/2
    raise ValueError('no optimum found within iteration limit, try different inputs, e.g. looser epsilon')

def testFindMaxExpenses():
    salary                = 10000
    fracSave              = 0.10
    preRetireGrowthRates  = [0.03, 0.04, 0.05, 0.0, 0.03]
    postRetireGrowthRates = [0.1, 0.05, 0.0, 0.05, 0.01]
    epsilon               = 0.01
    expenses = findMaxExpenses(salary, fracSave, preRetireGrowthRates,
                               postRetireGrowthRates, epsilon)
    print expenses
    # Output should have a value close to:
    # 1229.95548986

