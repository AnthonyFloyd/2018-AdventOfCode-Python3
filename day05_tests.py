# tests for AoC day4

import unittest
from advent_of_code import reducePolymer, countUnits, optimizePolymer

class TestPolymerReduction(unittest.TestCase):
    def test1(self):

        testCases = [('aA', 0),
                     ('abBA', 0),
                     ('abAB', 4),
                     ('aabAAB', 6),
                     ('dabAcCaCBAcCcaDA', 10),
                     ]

        for (inputPolymer, result) in testCases:
            reducedPolymer = reducePolymer(inputPolymer)
            self.assertEqual(countUnits(reducedPolymer), result)

    def test2(self):
        testCases =[('dabAcCaCBAcCcaDA', 4),]

        for (inputPolymer, result) in testCases:
            (shortestPolymer, (upper, lower)) = optimizePolymer(inputPolymer)
            self.assertEqual(countUnits(shortestPolymer), result)


