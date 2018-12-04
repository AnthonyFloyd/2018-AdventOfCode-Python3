'''
Advent of Code 2018
Day 3: No Matter How You Slice It

'''
import numpy as np

DAY = '3'
NAME = 'No Matter How You Slice It'
INPUT_FILE = 'day03-input.txt'


class ClaimMap():
    '''A convenient data object for holding the claim map.

    '''
    def __init__(self, claimList=None):
        self.width = 0
        self.height = 0
        self.claimList = claimList

        if claimList is not None:
            self.processClaims()

    def processClaims(self, claimList=None):
        '''Takes a list of claim strings and creates a full map.

        '''

        if claimList is not None:
            self.claimList = claimList

        self.claimDict = {}
        self.width = 0
        self.height = 0

        # Use a numpy zeros array as a heat map
        for line in self.claimList:
            #
            # A claim looks like this: #1 @ 37,526: 17x23
            #
            (claimID, _, upperLeft, size) = line.split(' ')
            claimID = claimID[1:]
            upperLeftX, upperLeftY = [int(i) for i in upperLeft[:-1].split(',')]
            width, height = [int(i) for i in size.split('x')]
            self.claimDict[claimID] = (upperLeftX, upperLeftY, width, height)

            # find the bounds of the map
            self.width = max([self.width, upperLeftX + width])
            self.height = max([self.height, upperLeftY + height])

        # Avoid off-by-one error
        self.width += 1
        self.height += 1

        # Make the heat map
        self.claim_map = np.zeros((self.width, self.height))
        for (claimID, claimDetails) in self.claimDict.items():
            (upperLeftX, upperLeftY, width, height) = claimDetails
            self.claim_map[upperLeftY:upperLeftY + height, upperLeftX:upperLeftX + width] += 1

    def findOverlappingClaims(self):
        '''Find the area of overlapping claims.

        '''
        #
        # Count all the entries that have 2 or more claims
        #

        return np.count_nonzero(self.claim_map >= 2)

    def findOnlyNonOverlappingID(self):
        '''Find the ID of the only non-overlapping claim.

        '''

        # Loop over each claim and check the already-processed map to see if there are any overlaps
        # for this claim. There can be only one.

        for (claimID, claimDetails) in self.claimDict.items():
            (upperLeftX, upperLeftY, width, height) = claimDetails
            if np.count_nonzero(self.claim_map[upperLeftY:upperLeftY + height, upperLeftX:upperLeftX + width] >= 2) == 0:
                return claimID

        return None

    def printMap(self):
        '''Print the claim map in ASCII.

        '''
        for row in range(self.height):
            rowString = ''
            for column in range(self.width):
                rowString += str(int(self.claim_map[row, column]))
            print(rowString)


def run():
    '''Run both part 1 and part 2 for AoC2018 Day 3.

    '''

    from advent_of_code import printBoilerPlate, readFileToList

    printBoilerPlate(DAY, NAME)

    # gather inputs
    inputList = readFileToList(INPUT_FILE)

    # Part 1
    print('\nPart 1')
    myMap = ClaimMap(inputList)
    overlappingClaimCount = myMap.findOverlappingClaims()
    print(f'Number of overlapping claims: {overlappingClaimCount}')

    # Part 2
    print('\nPart 2')
    nonOverlappingID = myMap.findOnlyNonOverlappingID()
    print(f'Only non-overlapping ID: {nonOverlappingID}')

if __name__ == '__main__':
    run()
