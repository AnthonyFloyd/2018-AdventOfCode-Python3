'''
Advent of Code 2018
Day 4: Repose Record

'''
from collections import Counter

DAY = '4'
NAME = 'Repose Record'
INPUT_FILE = 'day04-input.txt'

STRATEGY1 = 1
STRATEGY2 = 2

def parseSleepRecord(sleepRecord):
    '''Parse a specially-formated sleep record. Counts the number of times a guard
    is asleep in each minute in the midnight hour. Returns a dict of guardID: Counter
    where guardID is a string, and Counter is a collections.Counter of minute strings
    and counts.

    '''
    sleepLog = dict()

    # state machine
    currentGuard = None
    sleepMinute = None

    for record in sleepRecord:

        lineBits = record.split()
        if len(lineBits) == 6:
            #
            # [1518-07-07 23:58] Guard #983 begins shift
            # Only important info in this is the guard ID
            #
            (_, _, _, guardID, _, _) = lineBits
            currentGuard = guardID[1:]
            if currentGuard not in sleepLog.keys():
                sleepLog[currentGuard] = Counter()
        else:
            #
            # [1518-09-23 00:59] wakes up
            # (or "falls asleep")
            #
            (_, time, _, state) = lineBits
            if state == 'asleep':
                # falls asleep
                sleepMinute = int(time.split(':')[1][:-1])
            else:
                # wakes up
                wakeMinute = int(time.split(':')[1][:-1])
                for minuteCounter in [str(item) for item in range(sleepMinute, wakeMinute)]:
                    sleepLog[currentGuard].update([minuteCounter,])

    return sleepLog

def assessSleepLog(sleepLog, strategy):
    '''Assesses a sleep log using the provided strategy.

    Strategy1 looks to see which guard sleeps the longest, and reports the guard ID, how long
    they slept, and which minute was their most likely to be asleep.

    Strategy 2 looks to see which minute was most likely to have a guard asleep, and reports
    the most typical guardID, what the most likely minute was, and how many times they were asleep
    on that minute.

    '''

    longestSleep = 0
    frequentMinute = None
    sleepiestGuard = None

    if strategy == STRATEGY1:
        for (guardID, sleepCounter) in sleepLog.items():
            totalSleep = sum(sleepCounter.values())
            if totalSleep > longestSleep:
                longestSleep = totalSleep
                frequentMinute = int(sleepCounter.most_common(1)[0][0])
                sleepiestGuard = guardID
    elif strategy == STRATEGY2:
        for (guardID, sleepCounter) in sleepLog.items():
            if sleepCounter:
                minute, minuteCount = sleepCounter.most_common(1)[0]
                if minuteCount > longestSleep:
                    longestSleep = minuteCount
                    frequentMinute = int(minute)
                    sleepiestGuard = guardID
    else:
        raise RuntimeError('Unknown solution strategy')

    return (sleepiestGuard, longestSleep, frequentMinute)


def main():
    '''Run Advent of Code Day 4

    '''
    from advent_of_code import readFileToList, printBoilerPlate

    printBoilerPlate(DAY, NAME)

    # part 1
    sleepRecord = sorted(readFileToList(filename=INPUT_FILE))
    sleepLog = parseSleepRecord(sleepRecord)
    (sleepiestGuard, longestSleep, frequentMinute) = assessSleepLog(sleepLog, STRATEGY1)

    print('Part 1:')
    print(f'Guard {sleepiestGuard} slept {longestSleep} minutes')
    print(f'Their sleepiest minute was {frequentMinute}')
    print('The solution, then, is: {0:d}'.format(int(sleepiestGuard) * frequentMinute))

    # part 2
    (sleepiestGuard, longestSleep, frequentMinute) = assessSleepLog(sleepLog, STRATEGY2)

    print('\nPart 2:')
    print(f'Guard {sleepiestGuard} slept {longestSleep} times on minute {frequentMinute}')
    print('The solution, then, is: {0:d}'.format(int(sleepiestGuard) * frequentMinute))

if __name__ == '__main__':
    main()
