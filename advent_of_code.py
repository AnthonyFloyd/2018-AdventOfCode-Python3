# Advent of Code "Library"

from day01 import accumulateFromList, findFirstDuplicate

def printBoilerPlate(day, description):
    '''Write out a boilerplate header for the Advent of Code trials.

    '''

    dayString = f'Day {day}: {description}'
    separator = '~' * len(dayString)
    print('Advent of Code 2018')
    print(dayString)
    print(separator)

def readFileToList(filename, transformation=lambda x: x):
    '''Reads an AoC input file into a list, performing the optional transformation
    on each list element, after stripping the element.

    '''

    with open(filename) as inputFile:
        inputLines = inputFile.readlines()
        inputList = [transformation(i.strip()) for i in inputLines]

    return inputList

