# tests for AoC day4

import unittest
from advent_of_code import assessSleepLog, parseSleepRecord
from day04 import STRATEGY1, STRATEGY2

__TEST = '''[1518-11-01 00:00] Guard #10 begins shift
[1518-11-01 00:05] falls asleep
[1518-11-01 00:25] wakes up
[1518-11-01 00:30] falls asleep
[1518-11-01 00:55] wakes up
[1518-11-01 23:58] Guard #99 begins shift
[1518-11-02 00:40] falls asleep
[1518-11-02 00:50] wakes up
[1518-11-03 00:05] Guard #10 begins shift
[1518-11-03 00:24] falls asleep
[1518-11-03 00:29] wakes up
[1518-11-04 00:02] Guard #99 begins shift
[1518-11-04 00:36] falls asleep
[1518-11-04 00:46] wakes up
[1518-11-05 00:03] Guard #99 begins shift
[1518-11-05 00:45] falls asleep
[1518-11-05 00:55] wakes up'''

TESTLIST = __TEST.split('\n')

class TestSleepingGuards(unittest.TestCase):
    def test1(self):

        testCases = [(TESTLIST, 240),
                     ]

        for (inputList, result) in testCases:
            sleepRecord = sorted(inputList)
            sleepLog = parseSleepRecord(sleepRecord)
            (sleepiestGuard, longestSleep, frequentMinute) = assessSleepLog(sleepLog, STRATEGY1)
            solution = int(sleepiestGuard) * frequentMinute
            self.assertEqual(solution, result)

    def test2(self):

        testCases = [(TESTLIST, 4455),
                     ]

        for (inputList, result) in testCases:
            sleepRecord = sorted(inputList)
            sleepLog = parseSleepRecord(sleepRecord)
            (sleepiestGuard, longestSleep, frequentMinute) = assessSleepLog(sleepLog, STRATEGY2)
            solution = int(sleepiestGuard) * frequentMinute
            self.assertEqual(solution, result)

