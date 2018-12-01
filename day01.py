'''
Advent of Code 2018
Day 1: Chronal Calibration

'''

def accumulateFromList(intList):
    '''Sum a list of ints.

    Takes a list of positive and negative ints, returns an int.
    '''

    total = 0
    for i in intList:
        total += i

    return total

def findFirstDuplicate(intList):
    '''Find the first repeated value in the process of summing a list of ints.

    The int list may be repeated until a duplicate is found.

    Takes a list of positive and negative ints, returns an int.
    '''

    totals = {}
    total = 0

    totals[total] = 1
    noDuplicate = True

    while noDuplicate:
        for i in intList:
            total += i
            totals[total] = totals.get(total, 0) + 1

            if totals[total] == 2:
                break
        if totals[total] == 2:
            break

    return total

if __name__ == '__main__':

    print('Advent of Code')
    print('Day 1: Chronal Calibration')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~')

    # gather inputs
    inputFilename = 'day01-input.txt'
    with open(inputFilename) as inputFile:
        inputLines = inputFile.readlines()
        inputList = [int(i.strip()) for i in inputLines]

    # Part 1
    print('\nPart 1')
    finalFrequency = accumulateFromList(inputList)
    print('Final frequency: {}'.format(finalFrequency))

    # Part 2
    print('\nPart 2')
    firstDuplicate = findFirstDuplicate(inputList)
    print('First duplicate frequency: {}'.format(firstDuplicate))

