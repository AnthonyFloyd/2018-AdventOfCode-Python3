'''
Advent of Code 2018
Day 7: The Sum of Its Parts

'''

DAY = '7'
NAME = 'The Sum of Its Parts'
INPUT_FILE = 'day07-input.txt'

class Instruction():
    '''An "Instruction" node, which keeps track of its predecessors and
    successors.

    '''
    def __init__(self, name):
        self.name = name

        self.predecessors = []
        self.successors = []

    def __repr__(self):
        return f'Instruction {self.name}'

class Factory():
    '''A factory that processes instructions.

    '''
    def __init__(self):
        self.noPredecessors = []

    def readInstructions(self, instructionList):
        '''Read the instruction list into the factory.

        '''
        # Step N must be finished before step Q can begin.

        instructions = {}

        for instructionString in instructionList:
            (_, predecessorName, _, _, _, _, _, instructionName, _, _) = instructionString.split()

            # If we've never seen this instruction name, create an Instruction
            if instructionName not in instructions:
                instructions[instructionName] = Instruction(instructionName)

            # If we've never seen this predecessor name, create an Instruction
            if predecessorName not in instructions:
                instructions[predecessorName] = Instruction(predecessorName)

            # Create the predecessor/successor links
            instructions[instructionName].predecessors.append(instructions[predecessorName])
            instructions[predecessorName].successors.append(instructions[instructionName])

            # If this instruction has no predecessors, add it to the master noPredecessors list
            if instructions[predecessorName] not in self.noPredecessors and not instructions[predecessorName].predecessors:
                self.noPredecessors.append(instructions[predecessorName])

            # But if this instruction is in no predecessors list, remove it
            if instructions[instructionName] in self.noPredecessors:
                self.noPredecessors.remove(instructions[instructionName])

    def processInstructions(self):
        '''Process all the instructions, satisfying the build instructions, using a single elf.

        '''
        instructionList = ''

        while self.noPredecessors:
            # do the right instruction (first alphabetical)
            firstInstruction = sorted(self.noPredecessors, key=lambda x: x.name)[0]
            instructionList += firstInstruction.name

            # remove it from the NP list
            self.noPredecessors.remove(firstInstruction)

            # remove it from the predecessor list of its successors
            for successor in firstInstruction.successors:
                successor.predecessors.remove(firstInstruction)
                # if no predeccors left, add it to the NP list
                if not successor.predecessors:
                    self.noPredecessors.append(successor)

        # that should be it?

        return instructionList

    def processInstructionsParallel(self, number_of_helpers=1, time_penalty=0):
        '''Process the build instructions using many elves. There is a base
        time penalty associated with each instruction. Return the total time to
        complete. '''

        # The helper pool keeps track of when assigned instructions will be completed
        # and the associated task pool keeps track of the specific tasks being
        # worked on

        helper_pool_completion_times = [0,] * (number_of_helpers + 1)
        helper_pool_tasks = [None,] * (number_of_helpers + 1)

        # tick tock
        current_time = 0

        # A list of current jobs so that we can remove them from the no predecessors list
        # but before we entirely throw it out. This is essentially helper_pool_tasks without
        # the None placeholders

        currentJobs = []

        while self.noPredecessors or currentJobs:
            # remove completed tasks
            # loop through existing tasks, see if any have completed on this tick
            for (index, time) in enumerate(helper_pool_completion_times):
                if time == current_time and helper_pool_tasks[index]:
                    # remove it from the current jobs list
                    currentJobs.remove(helper_pool_tasks[index])

                    # remove it from the predecessor list of its successors
                    for successor in helper_pool_tasks[index].successors:
                        successor.predecessors.remove(helper_pool_tasks[index])
                        # if no predeccors left, add it to the NP list
                        if not successor.predecessors:
                            self.noPredecessors.append(successor)

                    # clear the helper pool
                    helper_pool_tasks[index] = None

            # How many helpers are available?
            nAvailableHelpers = helper_pool_tasks.count(None)

            # Try to give everyone a task
            for _ in range(nAvailableHelpers):
                # if nothing to do at the moment, break out
                if not self.noPredecessors:
                    break

                # grab an instruction, assign it to an available helper
                firstInstruction = sorted(self.noPredecessors, key=lambda x: x.name)[0]
                completion_time = time_penalty + ord(firstInstruction.name) - ord('A') + 1 # add one b/c 'A' is 1

                # try to assign the task
                # this is crude but we don't have a big list of helpers
                for (index, time) in enumerate(helper_pool_completion_times):
                    if helper_pool_tasks[index] is None:
                        helper_pool_completion_times[index] = completion_time + current_time
                        helper_pool_tasks[index] = firstInstruction

                        # move the instruction from the no predecessors list to the current jobs list
                        currentJobs.append(firstInstruction)
                        self.noPredecessors.remove(firstInstruction)
                        break

            # tick tock
            current_time += 1

        return current_time - 1 # we were actually done before ticking the time

def main():
    '''Run Advent of Code Day 7

    '''
    from advent_of_code import readFileToList, printBoilerPlate

    printBoilerPlate(DAY, NAME)

    instructionList = readFileToList(INPUT_FILE)

    # part 1
    factory = Factory()
    factory.readInstructions(instructionList)
    build_order = factory.processInstructions()

    print('Part 1:')
    print(f'Build order {build_order}')

    # part 2
    factory = Factory()
    factory.readInstructions(instructionList)
    time_to_complete = factory.processInstructionsParallel(number_of_helpers=5, time_penalty=60)

    print('Part 2:')
    print(f'Time to complete: {time_to_complete}')

if __name__ == '__main__':
    main()
