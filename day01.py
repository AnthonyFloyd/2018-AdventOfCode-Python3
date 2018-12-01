'''
Advent of Code 2018
Day 1: Chronal Calibration

'''

DAY = '1'
NAME = 'Chronal Calibration'
INPUT_FILE = 'day01-input.txt'

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

def run():
    '''Run both part 1 and part 2 for AoC2018 Day 1.

    '''

    from advent_of_code import printBoilerPlate, readFileToList

    printBoilerPlate(DAY, NAME)

    # gather inputs
    inputList = readFileToList(INPUT_FILE, transformation=int)

    # Part 1
    print('\nPart 1')
    finalFrequency = accumulateFromList(inputList)
    print(f'Final frequency: {finalFrequency}')

    # Part 2
    print('\nPart 2')
    firstDuplicate = findFirstDuplicate(inputList)
    print(f'First duplicate frequency: {firstDuplicate}')

if __name__ == '__main__':
    run()
