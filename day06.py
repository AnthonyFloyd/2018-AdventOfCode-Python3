'''
Advent of Code 2018
Day 6: Chronal Coordinates

'''

DAY = '6'
NAME = 'Chronal Coordinates'
INPUT_FILE = 'day06-input.txt'

def manhattan_distance(thing1, thing2):
    '''Returns the Manhattan distance between two objects with .x and .y attributes.

    '''
    return abs(thing1.x - thing2.x) + abs(thing1.y - thing2.y)

class Coordinate():
    '''A class that contains an (x,y) location, an optional name, and a certain area associated with it on the map.

    '''
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
    '''A subclass of a Coordinate that corresponds to a location on the map, and includes references to its closest
    coordinate, and metadata whether it is on the edge of the map.'''

    def __init__(self, coordinates):
        Coordinate.__init__(self, coordinates)

        self.closestDistance = 1E30
        self.closestCoordinate = None
        self.isOnEdge = False

    def __repr__(self):
        return f'Location ({self.x},{self.y})'

    def findClosestCoordinate(self, coordinates):
        '''Finds the Coordinate that is closest to this map location. If two coordinates
        are the same distance away, then the closest coordinate is set to None.

        '''
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
    '''A convenience class that is essentially a list, but contains "minY" which is an offset such that
    the index of the list is not the index position but the map coordinate. This way a map location can
    be identifyied by map[x][y] and magically get the right location. '''

    def __init__(self, sequence=None, minY=0):
        if sequence:
            self.__list = list(sequence)
        else:
            self.__list = []

        self.__minY = minY

    def __getitem__(self, y):
        return self.__list[y - self.__minY]

    def append(self, sequence):
        '''Equivalent to the list append method.

        '''
        self.__list.append(sequence)

class CoordinateMap():
    '''A representation of a map, with coordinate points on it.

    Automatically creates the map, with the coordinates, and then finds out, for each
    map location, what the closest coordinates are. Each coordinate gets assigned an area
    that corresponds to its closest map locations. However, these areas could be unbounded
    in which case they are set to None.

    '''
    def __init__(self, coordinateList):
        self.coordinates = []
        self.__mapColumns = []

        self.__map_minX = None
        self.__map_maxX = None

        self.__map_minY = None
        self.__map_maxY = None

        self.maxArea = 0
        self.maxAreaCoordinate = None

        self.setCoordinates(coordinateList)

    def __getitem__(self, x):
        return self.__mapColumns[x - self.__map_minX]

    def setCoordinates(self, coordinateList):
        '''Enters the "Coordinates" into the map.

        '''
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
        """Generates the map, with the already established coordinates, and calculates the
        distances to closest coordinates for each map location, and calculates the area
        associated with each coordinate ... for those areas that are bounded.

        """
        self.__map_minX = max(0, self.__coordinate_minX - 1)
        self.__map_maxX = self.__coordinate_maxX + 1

        self.__map_minY = max(0, self.__coordinate_minY - 1)
        self.__map_maxY = self.__coordinate_maxY + 1

        self.__mapColumns = []

        # Loop through each location, creating an entry for it in the map.
        # Check to see if it's on the map edge or not.
        # Find the closest coordinate for this location

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

        # now go around and count the remaining (ie bounded) area
        # and assign it to the appropriate coordinate

        for y in range(self.__map_minY, self.__map_maxY + 1):
            for x in range(self.__map_minX, self.__map_maxX + 1):
                closestCoordinate = self[x][y].closestCoordinate
                if closestCoordinate:
                    if closestCoordinate.allocatedArea is not None:
                        areaCounter[closestCoordinate] = areaCounter.get(closestCoordinate, 0) + 1

        # might as well find the maximum area while we're at it
        self.maxArea = 0
        self.maxAreaCoordinate = None

        for (coordinate, area) in areaCounter.items():
            coordinate.allocatedArea = area
            if area > self.maxArea:
                self.maxArea = area
                self.maxAreaCoordinate = coordinate

    def findSafeRegionSize(self, safeDistance=32):
        '''Finds the safe region size. The safe region is defined as those locations that have
        a total distance to all coordinates less than the given threshold.

        '''
        safeRegionSize = 0

        # Brute force. Loop through each location and then loop through each coordinate and sum up
        # the distances.

        for y in range(self.__map_minY, self.__map_maxY + 1):
            for x in range(self.__map_minX, self.__map_maxX + 1):
                distanceSum = 0
                location = self[x][y]
                for coordinate in self.coordinates:
                    distanceSum += manhattan_distance(location, coordinate)
                if distanceSum < safeDistance:
                    safeRegionSize += 1

        return safeRegionSize

    def printMap(self):
        '''Returns an ASCII representation of the map.

        '''

        outputString = ''

        # Loop through each location
        for y in range(self.__map_minY, self.__map_maxY + 1):
            for x in range(self.__map_minX, self.__map_maxX + 1):
                # Lookup the closest coordinate
                closestCoordinate = self[x][y].closestCoordinate

                if closestCoordinate is not None:
                    # If there is a closest coordinate
                    if self[x][y].location == closestCoordinate.location:
                        # ... that is the coordinate, put a 'C'
                        outputString += 'C'
                    elif self[x][y].isOnEdge:
                        # ... that is on the edge, put an 'E'
                        outputString += 'E'
                    else:
                        if closestCoordinate.allocatedArea is None:
                            # ... that has an unbounded area, put an 'i'
                            outputString += 'i'
                        else:
                            if closestCoordinate.name is not None:
                                # ... that has a name, put its name
                                outputString += closestCoordinate.name
                            else:
                                # ... otherwise, put an 'o'
                                outputString += 'o'
                else:
                    # If there's no closest coordinate, it's shared between more than one
                    # Put an '*'
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

def main():
    '''Run Advent of Code Day 6

    '''
    from advent_of_code import readFileToList, printBoilerPlate

    printBoilerPlate(DAY, NAME)

    # part 1

    def xform(x):
        bits = x.split(',')
        return (int(bits[0]), int(bits[1]))

    coordinateList = readFileToList(INPUT_FILE, xform)

    part1Map = CoordinateMap(coordinateList)

    print('Part 1:')
    print(f'The maximum bounded area is {part1Map.maxArea}')

    print('Part 2:')
    safeRegionSize = part1Map.findSafeRegionSize(10000)
    print(f'The safe region size is {safeRegionSize}')

if __name__ == '__main__':
    main()
