# Advent of Code "Library"
'''Omnibus library for Advent of Code 2018'''

from typing import List, Callable, Any

from day01 import accumulateFromList, findFirstDuplicate
from day02 import generateCheckSum, findWordsDifferringByOneLetter
from day03 import ClaimMap
from day04 import parseSleepRecord, assessSleepLog
from day05 import reducePolymer, countUnits,  optimizePolymer
from day06 import CoordinateMap
from day07 import Factory

def printBoilerPlate(day:str, description:str) -> None:
    '''Write out a boilerplate header for the Advent of Code trials.

    '''

    dayString:str = f'Day {day}: {description}'
    separator:str = '~' * len(dayString)
    print('Advent of Code 2018')
    print(dayString)
    print(separator)

def readFileToList(filename:str, transformation=lambda x: x) -> List[Any]:
    '''Reads an AoC input file into a list, performing the optional transformation
    on each list element, after stripping the element.

    '''

    with open(filename) as inputFile:
        inputLines:List[str] = inputFile.readlines()
        inputList:List[Any] = [transformation(i.strip()) for i in inputLines]

    return inputList

def multiplyListElements(myList):
    '''
    Multiply the elements of the list together.

    '''

    total = 1

    for item in myList:
        total *= item

    return total
