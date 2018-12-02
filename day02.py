'''
Advent of Code 2018
Day 2: Inventory Management System

'''

DAY = '2'
NAME = 'Inventory Management System'
INPUT_FILE = 'day02-input.txt'

class NoMatchError(Exception):
    '''Exception to be raised when no match can be found.'''

    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)

def generateCheckSum(inputList, requiredCounts=(2, 3)):
    '''
    Generates a checksum by counting letters in each word of inputList,
    counting those words with duplicate letter counts equal to requiredCounts,
    and then multiplying those word counts together.

    '''

    from collections import Counter
    from advent_of_code import multiplyListElements

    totalCount = Counter()

    for word in inputList:
        # count the number of each letters in the word
        letterCount = Counter(word)

        # count the number of occurances of each count
        occuranceCount = Counter(letterCount.values())

        # Check to see if this word has exactly one of each required count
        # Not quite. Multiple occurances only count as one.

        wordCount = Counter()
        for requiredCount in requiredCounts:
            if occuranceCount.get(requiredCount, 0) > 0:
                wordCount.update([requiredCount,])

        totalCount = totalCount + wordCount

    checkSum = multiplyListElements(totalCount.values())

    return checkSum

def findWordsDifferringByOneLetter(inputList):
    '''Takes a word list, finds two words which only differ by a single
    character in the same position and returns the common letters.

    The difference in that single character can be anything, it is not
    limited to an off-by-one.
    '''

    setKnownWords = set()

    #
    # Create a set of word signatures
    # Loop over all the words
    # For each word, create several signature words that have each
    # letter in the word replaced by a special character (like _)
    # Check to see if each signature is already in the set
    # If it is, then there is a word that differs from this word by one
    # character! If not, then add the signature to the set and keep
    # going.
    #

    for word in inputList:
        for index in range(len(word)):
            newString = word[:index] + '_' + word[index + 1:]
            if newString in setKnownWords:
                return word[:index] + word[index + 1:]
            setKnownWords.add(newString)

    raise NoMatchError

def run():
    '''Run both part 1 and part 2 for AoC2018 Day 2.

    '''

    from advent_of_code import printBoilerPlate, readFileToList

    printBoilerPlate(DAY, NAME)

    # gather inputs
    inputList = readFileToList(INPUT_FILE)

    # Part 1
    print('\nPart 1')
    checksum = generateCheckSum(inputList, [2, 3])
    print(f'Checksum: {checksum}')

    # Part 2
    print('\nPart 2')
    try:
        commonLetters = findWordsDifferringByOneLetter(inputList)
    except NoMatchError:
        print('No words were found that differ by one character')
    else:
        print(f'Common letters: {commonLetters}')

if __name__ == '__main__':
    run()
