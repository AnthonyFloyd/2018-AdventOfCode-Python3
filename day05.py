'''
Advent of Code 2018
Day 5: Alchemical Reduction

'''

DAY = '5'
NAME = 'Alchemical Reduction'
INPUT_FILE = 'day05-input.txt'

PROGRESS_FACTOR = 100000

def reducePolymer(initialPolymer, progress=True):
    '''Reduce a polymer by removing matching pairs from the polymer chain.

    Returns the fully reacted polymer.
    '''

    doneFlag = False
    progressCounter = 0

    currentPolymer = initialPolymer

    while not doneFlag:
        currentPolymerLength = len(currentPolymer)

        # search for a matching pair
        foundPair = False
        cursorPosition = 0

        while (not foundPair and cursorPosition < currentPolymerLength - 1):
            if abs(ord(currentPolymer[cursorPosition]) - ord(currentPolymer[cursorPosition + 1])) == 32:
                # found a matching pair, remove it
                currentPolymer = currentPolymer[0:cursorPosition] + currentPolymer[cursorPosition + 2:]
                foundPair = True
            else:
                # no matching pair, go to the next position
                cursorPosition += 1
                progressCounter += 1
                if progress:
                    if progressCounter % PROGRESS_FACTOR == 0:
                        print('.', end='')
                    if progressCounter % (40 * PROGRESS_FACTOR) == 0:
                        print('')

        if not foundPair:
            # if there are no more pairs to match, bail out
            # otherwise, go again
            doneFlag = True

    if progress:
        print('')

    return currentPolymer

def countUnits(polymer):
    '''Counts the number of units in the given polymer.

    '''

    # Dude, this is just the length of the polymer
    return len(polymer)

def optimizePolymer(polymer):
    '''Optimize the polymer by dropping a single pair of units and then processing the remains.

    Loops through all letters, measuring the result. Skips any pair that didn't exist in the
    original polymer.

    '''

    shortestPolymer = polymer
    removedPair = None

    # All the letters
    polymer_pairs = [('A', 'a'), ('B', 'b'), ('C', 'c'), ('D', 'd'),
                     ('E', 'e'), ('F', 'f'), ('G', 'g'), ('H', 'h'),
                     ('I', 'i'), ('J', 'j'), ('K', 'k'), ('L', 'l'),
                     ('M', 'm'), ('N', 'n'), ('O', 'o'), ('P', 'p'),
                     ('Q', 'q'), ('R', 'r'), ('S', 's'), ('T', 't'),
                     ('U', 'u'), ('V', 'v'), ('W', 'w'), ('X', 'x'),
                     ('Y', 'y'), ('Z', 'z')]

    # Loop through all the letters
    for (upper, lower) in polymer_pairs:
        # strip out the pair
        currentPolymer = polymer.replace(upper, '')
        currentPolymer = currentPolymer.replace(lower, '')

        # only run the reduction if we actually stripped out some units
        if len(currentPolymer) < len(polymer):
            print('Removing {0},{1}'.format(upper, lower))
            reducedPolymer = reducePolymer(currentPolymer)

            if countUnits(reducedPolymer) < countUnits(shortestPolymer):
                shortestPolymer = reducedPolymer
                removedPair = (upper, lower)

    return (shortestPolymer, removedPair)

def main():
    '''Run Advent of Code Day 5

    '''
    from advent_of_code import readFileToList, printBoilerPlate

    printBoilerPlate(DAY, NAME)

    # part 1
    initialPolymer = readFileToList(filename=INPUT_FILE)[0]
    reactedPolymer = reducePolymer(initialPolymer)
    remainingUnits = countUnits(reactedPolymer)

    print('Part 1:')
    print(f'{remainingUnits} units remain in the fully-reacted polymer')

    (shortestPolymer, (upper, lower)) = optimizePolymer(initialPolymer)

    print('Part 2:')
    print('The length of the shortest polymer is: {0}, created by removing {1}, {2}'.format(countUnits(shortestPolymer), upper, lower))

if __name__ == '__main__':
    main()
