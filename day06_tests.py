# tests for AoC day6

import unittest
from advent_of_code import CoordinateMap

TEST_COORDINATES = [(1, 1),
                    (1, 6),
                    (8, 3),
                    (3, 4),
                    (5, 5),
                    (8, 9),
                    ]

class TestChronalCoordinates(unittest.TestCase):
    def test1(self):

        testMap = CoordinateMap(TEST_COORDINATES)
        testMap.printMap()

        self.assertEqual(testMap.maxArea, 17)
        self.assertEqual(testMap.findSafeRegionSize(32), 16)




