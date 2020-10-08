import itertools
import numpy as np

walls = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (0, 9), (0, 10), (1, 0), (1, 10), (2, 0), (2, 2), (2, 3), (2, 4), (2, 6), (2, 7), (2, 8), (2, 10), (3, 0), (3, 2), (3, 8), (3, 10), (4, 0), (4, 4), (4, 6), (4, 10), (5, 0), (5, 1), (5, 2), (5, 4), (5, 6), (5, 8), (5, 9), (5, 10), (6, 0), (6, 10), (7, 0), (7, 2), (7, 4), (7, 5), (7, 6), (7, 8), (7, 10), (8, 0), (8, 2), (8, 4), (8, 6), (8, 8), (8, 10), (9, 0), (9, 2), (9, 4), (9, 8), (9, 10), (10, 0), (10, 2), (10, 4), (10, 8), (10, 10), (11, 0), (11, 2), (11, 4), (11, 6), (11, 8), (11, 10), (12, 0), (12, 2), (12, 4), (12, 5), (12, 6), (12, 8), (12, 10), (13, 0), (13, 10), (14, 0), (14, 1), (14, 2), (14, 4), (14, 6), (14, 8), (14, 9), (14, 10), (15, 0), (15, 4), (15, 6), (15, 10), (16, 0), (16, 2), (16, 8), (16, 10), (17, 0), (17, 2), (17, 3), (17, 4), (17, 6), (17, 7), (17, 8), (17, 10), (18, 0), (18, 10), (19, 0), (19, 1), (19, 2), (19, 3), (19, 4), (19, 5), (19, 6), (19, 7), (19, 8), (19, 9), (19, 10)]


def getFullWall(wall, selectedWallPiece):
    '''
    Given a cell that belongs to a wall, return all the cells
    belonging to that wall, including the initial one
    '''

    # possible cells shifter around a wall block
    surroundings = []
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            surroundings.append((i, j))
    surroundings.remove((0, 0))

    perimeter = set()
    for block in wall:
        for surrounding in surroundings:
            perimeter.add(sumTuples(block, surrounding))
    
    # the perimeter right now includes all the perimeter cells plus
    # the ones forming the wall, which have to be removed
    for block in wall:
        perimeter.remove(block)
    return perimeter
    

    # newWallPieces = [selectedWallPiece]
    # knownWallPieces = []
    # while (len(newWallPieces)):
    #     print newWallPieces, "---\n", knownWallPieces, " === "
    #     currentWallPiece = newWallPieces.pop(0)
    #     if currentWallPiece not in knownWallPieces and currentWallPiece not in newWallPieces:
    #         print "$$$", currentWallPiece
    #         knownWallPieces.append(currentWallPiece)
    #     for surrounding in surroundings:
    #         newPosition = sumTuples(surrounding, currentWallPiece)
    #         if newPosition in walls:
    #             newWallPieces.append(newPosition)
    #     raw_input("----------------------------------")
    # return knownWallPieces
    

def getPerimeterAroundWall(pacmanPosition, foodPosition, wall):
    perimeter = getWallPerimeter(wall)
    path1, path2 = getPathsAroundTheWall(pacmanPosition, foodPosition, perimeter)


def getWallPerimeter(wall):
    surroundings = []
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            surroundings.append((i, j))
    surroundings.remove((0, 0))
    
    perimeter = []
    for block in wall:
        for surrounding in surroundings:
            position = sumTuples(surrounding, block)
            if position not in wall and position not in perimeter:
                perimeter.append(position)
    return perimeter
    

def getPathsAroundTheWall(startPosition, goalPosition, perimeter):
    path1 = [startPosition, goalPosition]
    path2 = [startPosition, goalPosition]
    perimeter.remove(startPosition)
    perimeter.remove(goalPosition)
    directions = [
        (1, 0),     # North
        (0, 1),     # East
        (-1, 0),    # South
        (0, -1)     # West
    ] # North
    directionPointer = 0
    while True:
        newPosition = sumTuples(startPosition, directions[directionPointer])
        if newPosition in perimeter:
            path1.append(newPosition)
            perimeter.remove(newPosition)
        else:
            directionPointer %= directionPointer + 1

        if newPosition == goalPosition:
            return path1, path2 + perimeter


## TEST PASSED
def sumTuples(tuple1, tuple2):
    return tuple([(i + j) for i, j in zip(tuple1, tuple2)])


## TEST PASSED
def getFullWallAndPerimeterFromWallBlock(block, walls):
    ''' 
    Given a block and the walls map,
    return perimeter and full wall of the block
    '''
    print block
    surroundings = []
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            surroundings.append((i, j))
    surroundings.remove((0, 0))
    surroundings = np.array(surroundings)
    
    perimeter = set()
    knownWall = set()
    newWall = set([block])

    while len(newWall) > 0:
        print newWall
        currentBlock = newWall.pop()
        if currentBlock in knownWall:
            continue
        else:
            knownWall.add(currentBlock)

        currentSurroundings = surroundings + currentBlock
        for currentSurrounding in currentSurroundings:
            if (currentSurrounding[0], currentSurrounding[1]) in walls:
                newWall.add((currentSurrounding[0], currentSurrounding[1]))
            else:
                perimeter.add((currentSurrounding[0], currentSurrounding[1]))
    return knownWall, perimeter
                



print getFullWallAndPerimeterFromWallBlock((4,4), walls)


    # for block in wall:
    #     for surrounding in surroundings:
    #         position = sumTuples(surrounding, block)
    #         if position not in wall and position not in perimeter:
    #             perimeter.append(position)
    # return perimeter
    