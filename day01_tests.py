# tests for AoC day1

import unittest
from advent_of_code import accumulateFromList, findFirstDuplicate

class TestAccumulate(unittest.TestCase):
    def test(self):

        testCases = [[[1, -2, 3, 1], 3],
                     [[1, 1, 1], 3],
                     [[1, 1, -2], 0],
                     [[-1, -2, -3], -6],
                     ]

        for (inputList, result) in testCases:
            self.assertEqual(accumulateFromList(inputList), result)

class TestFindDuplicates(unittest.TestCase):
    def test(self):

        testCases = [[[1, -2, 3, 1], 2],
                     [[1, -1], 0],
                     [[3, 3, 4, -2, -4], 10],
                     [[-6, 3, 8, 5, -6], 5],
                     [[7, 7, -2, -7, -4], 14],
                     ]

        for (inputList, result) in testCases:
            self.assertEqual(findFirstDuplicate(inputList), result)
