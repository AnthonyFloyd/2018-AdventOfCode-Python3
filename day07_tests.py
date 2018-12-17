# tests for AoC day7

import unittest
from advent_of_code import Factory

TEST_INSTRUCTIONS = '''Step C must be finished before step A can begin.
Step C must be finished before step F can begin.
Step A must be finished before step B can begin.
Step A must be finished before step D can begin.
Step B must be finished before step E can begin.
Step D must be finished before step E can begin.
Step F must be finished before step E can begin.'''

class TestFactory(unittest.TestCase):
    def test1(self):
        factory = Factory()
        factory.readInstructions(TEST_INSTRUCTIONS.splitlines())
        build_order = factory.processInstructions()

        self.assertEqual(build_order, 'CABDFE')

    def test2(self):
        factory = Factory()
        factory.readInstructions(TEST_INSTRUCTIONS.splitlines())
        build_time = factory.processInstructionsParallel()

        self.assertEqual(build_time, 15)





