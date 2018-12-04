# tests for AoC day3

import unittest
from advent_of_code import ClaimMap

class TestClaimMap(unittest.TestCase):
    def test(self):

        test1 = ['#1 @ 1,3: 4x4',
                 '#2 @ 3,1: 4x4',
                 '#3 @ 5,5: 2x2']
        testCases = [(test1, 4),
                     ]

        for (inputList, result) in testCases:
            testMap = ClaimMap(inputList)
            self.assertEqual(testMap.findOverlappingClaims(), result)

