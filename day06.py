'''
Advent of Code 2018
Day 6: Chronal Coordinates

'''

DAY = '6'
NAME = 'Chronal Coordinates'
INPUT_FILE = 'day06-input.txt'

def manhattan_distance(thing1, thing2):
    return abs(thing1.x - thing2.x) + abs(thing1.y - thing2.y)

class Coordinate():
    def __init__(self, coordinates, name=None):
        self.x = coordinates[0]
        self.y = coordinates[1]
        self.allocatedArea = 0
        self.name = name

    def __repr__(self):
        return f'Coordinate ({self.x},{self.y})'

    @property
    def location(self):
        return (self.x, self.y)

class MapLocation(Coordinate):
    def __init__(self, coordinates):
        Coordinate.__init__(self, coordinates)

        self.closestDistance = 1E30
        self.closestCoordinate = None
        self.isOnEdge = False

    def __repr__(self):
        return f'Location ({self.x},{self.y})'

    def findClosestCoordinate(self, coordinates):
        self.closestDistance = 1E30
        self.closestCoordinate = None

        # If this location is on the edge of the map
        # then the closest coordinate's area will be infinite

        for coordinate in coordinates:
            distance = manhattan_distance(coordinate, self)
            if distance < self.closestDistance:
                self.closestDistance = distance
                self.closestCoordinate = coordinate

            elif distance == self.closestDistance:
                self.closestCoordinate = None
                #break

class MapColumn():
    def __init__(self, sequence=None, minY=None):
        if sequence:
            self.__list = list(sequence)
        else:
            self.__list = []

        if minY:
            self.__minY = minY
        else:
            self.__minY =  0

    def __getitem__(self, y):
        return self.__list[y - self.__minY]

    def append(self, sequence):
        self.__list.append(sequence)

class CoordinateMap():
    def __init__(self, coordinateList):
        self.coordinates = []

        self.setCoordinates(coordinateList)

    def __getitem__(self, x):
        return self.__mapColumns[x - self.__map_minX]

    def setCoordinates(self, coordinateList):
        self.__coordinate_minX = 1E30
        self.__coordinate_maxX = 0
        self.__coordinate_minY = 1E30
        self.__coordinate_maxY = 0

        for (coordinateLabel, coordinatePair) in enumerate(coordinateList):
            self.coordinates.append(Coordinate(coordinatePair, str(coordinateLabel)))

            # check bounds
            self.__coordinate_minX = min(self.__coordinate_minX, coordinatePair[0])
            self.__coordinate_maxX = max(self.__coordinate_maxX, coordinatePair[0])
            self.__coordinate_minY = min(self.__coordinate_minY, coordinatePair[1])
            self.__coordinate_maxY = max(self.__coordinate_maxY, coordinatePair[1])

        self.__generateMap()

    def __generateMap(self):
        self.__map_minX = max(0, self.__coordinate_minX - 1)
        self.__map_maxX = self.__coordinate_maxX + 1

        self.__map_minY = max(0, self.__coordinate_minY - 1)
        self.__map_maxY = self.__coordinate_maxY + 1

        self.__mapColumns = []

        for x in range(self.__map_minX, self.__map_maxX + 1):
            currentColumn = MapColumn([], minY=self.__map_minY)
            for y in range(self.__map_minY, self.__map_maxY + 1):
                newLocation = MapLocation((x, y))
                if (x == self.__map_minX) or (x == self.__map_maxX) \
                   or (y == self.__map_minY) or (y == self.__map_maxY):
                    newLocation.isOnEdge = True

                newLocation.findClosestCoordinate(self.coordinates)
                currentColumn.append(newLocation)
            self.__mapColumns.append(currentColumn)

        # go around and invalidate any coordinate with area on the edge
        # or add the location to the area count for any given coordinate

        areaCounter = dict()

        for y in range(self.__map_minY, self.__map_maxY + 1):
            for x in range(self.__map_minX, self.__map_maxX + 1):
                closestCoordinate = self[x][y].closestCoordinate
                if closestCoordinate:
                    if self[x][y].isOnEdge:
                        closestCoordinate.allocatedArea = None

        # now go around and count the remaining area
        for y in range(self.__map_minY, self.__map_maxY + 1):
            for x in range(self.__map_minX, self.__map_maxX + 1):
                closestCoordinate = self[x][y].closestCoordinate
                if closestCoordinate:
                    if closestCoordinate.allocatedArea is not None:
                        areaCounter[closestCoordinate] = areaCounter.get(closestCoordinate, 0) + 1

        # might as well calculate the maximum area while we're at it
        self.maxArea = 0
        self.maxAreaCoordinate = None

        for (coordinate, area) in areaCounter.items():
            coordinate.allocatedArea = area
            if area > self.maxArea:
                self.maxArea = area
                self.maxAreaCoordinate = coordinate

    def printMap(self):
        outputString = ''

        for y in range(self.__map_minY, self.__map_maxY + 1):
            for x in range(self.__map_minX, self.__map_maxX + 1):
                closestCoordinate = self[x][y].closestCoordinate
                if closestCoordinate is not None:
                    if self[x][y].location == closestCoordinate.location:
                        outputString += 'C'
                    elif self[x][y].isOnEdge:
                        outputString += 'E'
                    else:
                        if closestCoordinate.allocatedArea is None:
                            outputString += 'i'
                        else:
                            if closestCoordinate.name is not None:
                                outputString += closestCoordinate.name
                            else:
                                outputString += 'o'
                else:
                    outputString += '*'
            outputString += '\n'

        print(outputString)

    @property
    def maxX(self):
        return self.__map_maxX

    @property
    def minX(self):
        return self.__map_minX

    @property
    def maxY(self):
        return self.__map_maxY

    @property
    def minY(self):
        return self.__map_minY

def createCoordinateMap(coordinateList):
    return CoordinateMap(coordinateList)

def main():
    '''Run Advent of Code Day 6

    '''
    from advent_of_code import readFileToList

    # part 1

    def xform(x):
        bits = x.split(',')
        return (int(bits[0]), int(bits[1]))

    coordinateList = readFileToList(INPUT_FILE, xform)

    part1Map = createCoordinateMap(coordinateList)

    print('Part 1:')
    print(f'The maximum bounded area is {part1Map.maxArea}')

if __name__ == '__main__':
    main()
