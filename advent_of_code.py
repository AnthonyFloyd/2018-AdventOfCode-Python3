# Advent of Code "Library"
'''Omnibus library for Advent of Code 2018'''

from typing import List, Callable, Any

from day01 import accumulateFromList, findFirstDuplicate

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
