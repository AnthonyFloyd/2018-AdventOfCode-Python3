# tests for AoC day2

import unittest
from advent_of_code import generateCheckSum, findWordsDifferringByOneLetter

class TestCheckSum(unittest.TestCase):
    def test(self):

        test1 = ['abcdef',
                 'bababc',
                 'abbcde',
                 'abcccd',
                 'aabcdd',
                 'abcdee',
                 'ababab',
                 ]
        testCases = [(test1, 12),
                     ]

        for (inputList, result) in testCases:
            self.assertEqual(generateCheckSum(inputList, [2, 3]), result)

class TestCommonLetters(unittest.TestCase):
    def test(self):
        test1 = ['abcde',
                 'fghij',
                 'klmno',
                 'pqrst',
                 'fguij',
                 'axcye',
                 'wvxyz',
                 ]
        testCases = [(test1, 'fgij')]

        for (inputList, result) in testCases:
            self.assertEqual(findWordsDifferringByOneLetter(inputList), result)

    def test_fail(self):
        from day02 import NoMatchError

        test1 = ['abcde',
                 'fghij',
                 'klmno',
                 'pqrst',
                 'rguij',
                 'axcye',
                 'wvxyz',
                 ]

        with self.assertRaises(NoMatchError):
            result = findWordsDifferringByOneLetter(test1)
