'''
Advent of Code 2018
Day 1: Chronal Calibration

'''

from typing import List, Dict

DAY = '1'
NAME = 'Chronal Calibration'
INPUT_FILE = 'day01-input.txt'

def accumulateFromList(intList:List[int]) -> int:
    '''Sum a list of ints.

    Takes a list of positive and negative ints, returns an int.
    '''

    total:int = 0
    for i in intList:
        total += i

    return total

def findFirstDuplicate(intList:List[int]) -> int:
    '''Find the first repeated value in the process of summing a list of ints.

    The int list may be repeated until a duplicate is found.

    Takes a list of positive and negative ints, returns an int.
    '''

    totals:Dict[int, int] = {}
    total:int = 0

    totals[total] = 1
    noDuplicate:bool = True

    while noDuplicate:
        for i in intList:
            total += i
            totals[total] = totals.get(total, 0) + 1

            if totals[total] == 2:
                break
        if totals[total] == 2:
            break

    return total

def run() -> None:
    '''Run both part 1 and part 2 for AoC2018 Day 1.

    '''

    from advent_of_code import printBoilerPlate, readFileToList

    printBoilerPlate(DAY, NAME)

    # gather inputs
    inputList:List[int] = readFileToList(INPUT_FILE, transformation=int)

    # Part 1
    print('\nPart 1')
    finalFrequency:int = accumulateFromList(inputList)
    print(f'Final frequency: {finalFrequency}')

    # Part 2
    print('\nPart 2')
    firstDuplicate:int = findFirstDuplicate(inputList)
    print(f'First duplicate frequency: {firstDuplicate}')

if __name__ == '__main__':
    run()
