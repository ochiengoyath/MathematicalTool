# SetsOfRandomTxt.py

# This module returns a given set of random numbers from a pool
from StandardModule import Logo, ModuleReload
from InputModule import IntInput, Switch, Loop
from TxtDataProcessorSampling import FloatsOnly
from importlib import reload
import random
import statistics


# This module returns a given set of random numbers from a pool
print()
SampleSet = []


# 1.Sample Variance
def SVar(SampleSet):
    return statistics.variance(SampleSet)


# 2.Sample Standard Deviation
def SStD(SampleSet):
    return statistics.stdev(SampleSet)


# 3.Items integer checker
def Items(NoOfItems):
    NoOfItems = None
    while not NoOfItems:
        try:
            NoOfItems = int(input('  Enter the Number of Data Points in a Set. '))
        except ValueError:
            print('  Invalid Input! Please Enter a Whole Number')
    return NoOfItems


# 4.Sets integer checker
def Sets(NoOfSets):
    NoOfSets = None
    while not NoOfSets:
        try:
            NoOfSets = int(input('  Enter the Number of Sets: '))
        except ValueError:
            print('  Invalid Input! Please Enter a Whole Number')
    return NoOfSets


print('  To Get Random Set of Data Points ')

NoOfItems = Items(None)
l = len(FloatsOnly)
for x in Loop:
    if NoOfItems < 3:
        print('  Insufficient Data set')
        print('  Minimum Data set is 3')
        x = input('  Enter Any Key to Reload Module')
        import StatisticsMenu

        reload(StatisticsMenu)
        input('  ')
        import ExitMenu

for i in Loop:
    if NoOfItems > l - 1:
        print('  Data set out of Range')
        print('  Maximum Data set is', l - 1)
        x = input('  Enter Any Key to Reload Module')
        import StatisticsMenu

        reload(StatisticsMenu)
        import MainMenu
        reload(MainMenu)

NoOfSets = Sets(None)
Max = 100
for x in Loop:
    if 2 > NoOfSets or NoOfSets > Max:
        print(' ', NoOfSets, 'is Out of Range')
        print('  Sets should be at least 2 and not greater than 100 ')
        NoOfSets = Sets(None)

print()
print('  The Summary is as Follows')
print()
print(' ', NoOfSets, 'Sets of', NoOfItems, 'Random Data Points:')

# returns a given set of random numbers from a pool
index = 0
SampleSetList = []
for Sets in range(NoOfSets):
    index = index + 1
    SampleSet = random.sample(FloatsOnly, NoOfItems)
    SampleSetList.append(SampleSet)
    print('  Set', index)
    print(' ', SampleSet)

# print(SampleSetList)
print()
print('  Corresponding Variance and Standard Deviation')
print('  Index:''   ''Set Variance:''      ''Set Standard Deviation:')
index = 0
for SampleSet in SampleSetList:
    index = index + 1
    print('  ', index, '       ', round(SVar(SampleSet), 2), '             ', round(SStD(SampleSet), 2))

Logo()
ModuleReload()
n = None
n = IntInput(None)
Switch(n)
if n == 1:
    import StatisticsMenu

    reload(StatisticsMenu)

elif n == 2:
    import ExitMenu

    reload(ExitMenu)

import ExitMenu
reload(ExitMenu)
