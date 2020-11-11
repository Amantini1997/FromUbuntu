# mdpAgents.py
# parsons/20-nov-2017
#
# Version 1
#
# The starting point for CW2.
#
# Intended to work with the PacMan AI projects from:
#
# http://ai.berkeley.edu/
#
# These use a simple API that allow us to control Pacman's interaction with
# the environment adding a layer on top of the AI Berkeley code.
#
# As required by the licensing agreement for the PacMan AI we have:
#
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).

# The agent here is was written by Simon Parsons, based on the code in
# pacmanAgents.py

from pacman import Directions
from game import Agent
import api
import random
import game
import math
import itertools
import copy

class MDPAgent(Agent):

    # Constructor: this gets run when we first invoke pacman.py
    def __init__(self):
        print "Starting up MDPAgent!"
        name = "Pacman"

    # Gets run after an MDPAgent object is created and once there is
    # game state to access.
    def registerInitialState(self, state):
        print "Running registerInitialState for MDPAgent!"
        print "I'm at:"
        print api.whereAmI(state)
        
    # This is what gets run in between multiple games
    def final(self, state):
        print "Looks like the game just ended!"

    # For now I just move randomly
    def getAction(self, state):
        # Get the actions we can try, and remove "STOP" if that is one of them.
        legal = api.legalActions(state)
        if Directions.STOP in legal:
            legal.remove(Directions.STOP)
        # Random choice between the legal options.
        return api.makeMove(random.choice(legal), legal)









class BetterHungryAgent(Agent):

    oppositeDirections = {
        Directions.SOUTH: Directions.NORTH,
        Directions.NORTH: Directions.SOUTH,
        Directions.EAST: Directions.WEST,
        Directions.WEST: Directions.EAST     
    }

    moves = [
        (1, 0),     # East
        (-1, 0),    # West
        (0, 1),     # North
        (0, -1)     # South
    ]

    traversalMoves = {
        (1, 0):  [(0, 1), (0, -1)],    # East
        (-1, 0): [(0, 1), (0, -1)],    # West
        (0, 1):  [(1, 0), (-1, 0)],    # North
        (0, -1): [(1, 0), (-1, 0)]     # South
    }

    moveToDirection = {
        (1, 0)  : Directions.EAST,
        (-1, 0) : Directions.WEST,
        (0, 1)  : Directions.NORTH,
        (0, -1) : Directions.SOUTH,
        (0, 0)  : Directions.STOP
    }

    # directionToMove = {
    #     Directions.EAST : (1, 0),
    #     Directions.WEST : (-1, 0),
    #     Directions.NORTH : (0, 1),
    #     Directions.SOUTH : (0, -1)
    # }

    def __init__(self):

        self.firstIteration = True
        
        # STATIC ELEMENTS
        self.accessibleMap = []
        # the type is { cell: moves[] }
        self.movesMap = {}  
        self.walls = []
        # this is an iterable used to iterate over ghosts and 
        # see if changes happened such that the value iteration map
        # has to be updated
        self.ghostsRange = None
        
        # DYNAMIC ELEMENTS
        self.ghostsStates = []
        # includes capsules
        self.food = []
        # the type is { cell: score }
        self.valueIterationMap = {} 


    def getAccessibleMap(self):
        return self.accessibleMap
    

    def getMovesMap(self):
        return self.movesMap


    def getAction(self, state):
        
        updateValueIterationMap = False

        # One time operations
        if self.firstIteration:
            self.firstIteration = False

            food = api.food(state)
            capsules = api.capsules(state)
            self.food = food + capsules
            self.walls = api.walls(state)
            self.accessibleMap = getNonWallCells(self.walls, state)
            self.ghostsRange = range(len(api.ghosts(state)))
            self.ghostsStates = api.ghostStates(state)
            self.movesMap = getMapMoves(self.accessibleMap)
            # print "$$$ ", self.movesMap
            # raw_input()

            self.valueIterationMap = { location : 0 for location in self.accessibleMap }
            updateValueIterationMap = True

        # Operations to be performed at every action iteration


        # Updates related to pacman
        pacman = api.whereAmI(state)
        if pacman in self.food: 
            self.food.remove(pacman)
            updateValueIterationMap = True

        # Ghosts related updates
        ghostsStates = api.ghostStates(state)
        for ghostIndex in self.ghostsRange:
            # ghostsStates returns a tuple ((x,y), 1 or 0) where 1 indicates
            # a scared ghost
            if ghostsStates[ghostIndex][1] != self.ghostsStates[ghostIndex][1]:
                updateValueIterationMap = True
                break
        self.ghostsStates = ghostsStates


        # print "PERIMETER", getPerimeterOfUnvisitedAndFoodCells(self.accessibleMap, self.visitedCells, self.movesMap)

        # NO MORE FOOD nearby, looking for 
        #   non eaten registered food first
        #   and non visited locations second 

        ######## THERE SHOULD ALWAYS BE FOOD ON THE MAP...
        
        # if len(food) == 0:
        #     message = "NO FOOD FOUND NEARBY, "
        #     if len(self.uneatenFood) > 0:
        #         print message, "reaching previously seen food"
        #         food = [food for food in self.uneatenFood]
        #     else:
        #         print message, "reaching unvisited locations"
        #         food = self.unvisitedCells


        # CLOSEST TARGET
        # foodDistances = [(manhattanDistance(pacman, point), index) for index, point in enumerate(food)]
        # sortedFoodDistances = sorted(foodDistances)
        # FOOD_INDEX = 1

        # firstFood = sortedFoodDistances[0]
        # closestFood = food[firstFood[FOOD_INDEX]]
        # xyDistanceToClosestFood = tupleDistance(closestFood, pacman)

        # # UPDATE PACMAN TARGET Data
        # self.lastBestFoodPosition = closestFood

        if updateValueIterationMap:
            # Do not count edible ghosts
            ghosts = map(lambda ghost: ghost[0], 
                        filter(lambda ghost: ghost[1] != 1, self.ghostsStates)
                    )
            # print "__________", self.accessibleMap
            # print "__________", self.movesMap
            # print "__________", self.valueIterationMap
            # print "__________", self.food
            # print "__________", ghosts
            self.valueIterationMap = getNewValueIterationMap(self.accessibleMap, self.movesMap, self.valueIterationMap, self.food, ghosts)

        # CALCULATE BEST MOVES
        bestMove = self.moveToDirection[ getBestNextMove(self.moves, pacman, self.valueIterationMap, self.movesMap) ]


        # print "PAC: ", pacman, "CLOSEST TARGET: ", closestFood, "  DISTANCE FROM IT: ", xyDistanceToClosestFood
        # print "LAST POSITION: ", self.lastPosition
        # print "LEGAL: ", legal
        # print "BEST MOVES:", bestMoves

        # # NO BEST MOVE, REVERT TO ALL POSSIBLE
        # if len(bestMoves) == 0:
        #     bestMoves = legal
        # else:
            
        #     # IMMEDIATE BEST MOVE
        #     if bestMoves[-1] is True:
        #         bestMoves.pop(-1)
        #     else:
        #         # best move takes more than 3 steps, so
        #         # prevent coming back (AVOID LOOP)
        #         if self.lastPosition in bestMoves:
        #             if len(bestMoves) > 1:
        #                 print "== OLD BEST MOVES IS ====> ", bestMoves
        #                 bestMoves.remove(self.lastPosition)
        #                 print "== REMOVED LAST POSITION: ", self.lastPosition
        #                 print "== NEW BEST MOVES: ", bestMoves
        #             else:
        #                 if len(legal) > 1:
        #                     legal.remove(self.lastPosition)
        #                     bestMoves = legal


        # pick = random.choice(bestMoves)
        # self.lastPosition = self.oppositeDirections[pick]
        # print "SELECTED MOVE: ", pick
        # raw_input()
        # print "\n====================================\n"
        legal = api.legalActions(state)
        return api.makeMove(bestMove, legal)




















 








###############
#             #   
#  FUNCTIONS  #
#             #   
###############

def tupleDistance( xy1, xy2 ):
    """
    Returns the distance between points xy1 and xy2 as a tuple.
    The order of the inputs matters as the values returned are not absolute.
    e.g. 
        xy1 = (1, 2)
        xy2 = (0, -1)
        return => (1, -3)
    """
    return ( xy1[0] - xy2[0], xy1[1] - xy2[1] )


def manhattanDistance( xy1, xy2 ):
    return abs( xy1[0] - xy2[0]) + abs(xy1[1] - xy2[1] )


def sumTuples(tuple1, tuple2):
    return tuple([(i + j) for i, j in zip(tuple1, tuple2)])


def getBestNextMove(moves, pacman, valueIterationMap, movesMap, minThreshold = -4, selectingProcess = "max"):
    '''
        Given the legal moves and the valueIterationMap,
        Calculates and return the best moves in the for (x, y).
        e.g. If the best move is go NORTH the function returns (0, 1)
    '''
    policies = [(getValuesFromMapGivenUndeterminism(pacman, move, valueIterationMap, movesMap), move) for move in moves]
    
    # include the option not to move
    policies.append((valueIterationMap[pacman]), (0, 0))

    # if selectingProcess != "max":
    bestMove = sorted(policies)[0]
    return bestMove


def getNewValueIterationMap(accessibleMap,       movesMap,              oldValueIterationMap,     
                            food,                ghosts = [],           movePenalty = 0.04,  
                            foodReward = 2,      ghostPenalty = -5,      
                            epsilon = 0.1,      discountFactor = 0.91
                        ):
    '''
        The input parameters are, (beside the obvious ones)
        epsilon -> this is the value below which we stop iterating (to improve performance)
        penalty -> the cost to make a move
        discountFactor -> the lambda factor that reduces the value of further away elements
        foodReward -> the reward for getting food
        unvisitedReward -> the reward for getting on unvisited locations
        ghostPenalty -> the reward (negative) for bumping into a ghost
    '''

    # Step 1: remove the fixed object from the map. clone accessibleMap but filter food and ghost locations
    scoreableMap = [location for location in accessibleMap if not(location in food or location in ghosts)]

    # Create the next value iteration map variable
    newValueIterationMap = {}

    # Update the old one in food and ghosts cells
    # drop the reward of food less than 2 steps away from ghosts
    # TODO ...  

    for foodCell in food: oldValueIterationMap[foodCell] = foodReward

    for ghostCell in ghosts: oldValueIterationMap[ghostCell] = ghostPenalty

    # Step 2: Create a while that terminates when no change is bigger than epsilon
    iterate = True
    while iterate:
        maxEpsilon = 0
        iterate = False
        # for each cell which can change value
        for scoreableCell in scoreableMap:
            score = []
            for move in BetterHungryAgent.moves:
                score.append(sum(getValuesFromMapGivenUndeterminism(scoreableCell, move, oldValueIterationMap, movesMap)))
            
            maxScore = max(score)

            # At least one values has been updated enough to having to re-iterate
            difference = abs(maxScore - oldValueIterationMap[scoreableCell])
            maxEpsilon = max(maxEpsilon, difference)  
            if difference > epsilon: iterate = True

            print maxScore
            # update value in the new map
            newValueIterationMap[scoreableCell] = maxScore

        for newValue in newValueIterationMap:
            print newValue, "  ", oldValueIterationMap[newValue], "  -  ",  newValueIterationMap[newValue]
        raw_input()

        for key, newValue in newValueIterationMap.items():
            oldValueIterationMap[key] = newValue

        oldValueIterationMap = newValueIterationMap
        newValueIterationMap = {}
        print(maxEpsilon)

    # Step 4: Taking into account the .8 .1 .1 rule, calculate the outcome for each location [remember to take into account the Direction.STOP move]

    # Step 5: update and return the value map
    for foodCell in food: scoreableMap[foodCell] = foodReward 
    for ghostCell in ghosts: scoreableMap[ghostCell] = ghostPenalty 

    return scoreableMap


## TODO TEST
def getValuesFromMapGivenUndeterminism(location, move, valueIterationMap, movesMap):
    '''
        Given a location and a move, calculate the values you would obtain
        trying to perform that move keeping into account that you only have 80%
        of the chance to actually perform that move. 
        The list returned is a 3-value vectors wherein the elements in order are:
         1) 0.8 * expected value from making the decided move;
         2 & 3) 0.1 * expected value from making a perpendicular move.
    '''
    mainDirectionCell = sumTuples(location, move) 
    values = [valueIterationMap[mainDirectionCell if move in movesMap[location] else location] * .8]
    for traversalMove in BetterHungryAgent.traversalMoves[move]:
        faultyDirectionCell = sumTuples(location, traversalMove)
        values.append(valueIterationMap[faultyDirectionCell if traversalMove in movesMap[location] else location] * .1)
    return values

# == TESTED BY getNonWallCells()
def getVisitbaleWidthAndHeight(state):
    topRightCorner = max(api.walls(state))

    # the corners belong to the walls, so in a map 4 x 4
    # the top right corner is (3, 3), but it's a wall, so the map is
    # 2 x 2 from the agent perspective, so the width is 3 - 1
    return (topRightCorner[0] - 1, topRightCorner[1] - 1)


# == TESTED BY getNonWallCells()
def getMapCellsMatrix(mapWidth, mapHeight):
    widthArray = range(1, mapWidth + 1)
    heightArray = range(1, mapHeight + 1)
    return [element for element in itertools.product(heightArray, widthArray)]


# WORKING
def getNonWallCells(walls, state):
    width, height = getVisitbaleWidthAndHeight(state)
    mapCellsMatrix = getMapCellsMatrix(height, width)
    return [x for x in mapCellsMatrix if x not in walls]


# == TESTED BY getMapMoves()
def getLegalMoves(accessibleMap, location):
    '''
    Given a cell and the accessibleMap, 
    Return the moves that can be made from there
    e.g. [(1, 0), (-1, 0)]
    Pacman can only move EAST or WEST
    '''
    ## TODO rename the class to use the correct one
    return [move for move in BetterHungryAgent.moves if sumTuples(location, move) in accessibleMap]


# WORKING
def getMapMoves(accessibleMap):
    '''
    Return a dictionary in the form {cell: moves[]}
    e.g. { (6, 5): [(1, 0), (-1, 0)]} 
    the only moves are going either EAST or WEST
    '''
    return {location: getLegalMoves(accessibleMap, location) for location in accessibleMap}


# def getPerimeterOfUnvisitedAndFoodCells(accessibleMap, visitedCells, movesMap):
#     '''
#         Return the perimeter of the directly accessible map. This means
#         that if to reach a food cell "x" you MUST first reach another location
#         with a food "y" on it, "x" will not be included in the perimeter.
#     '''
#     perimeter = set()
#     notVisitedCells = accessibleMap.difference(visitedCells)
#     notVisitedCellsSurroundingCells = map(lambda cell: {cell: getSurroundingCells(cell, movesMap[cell], accessibleMap)}, notVisitedCells)

#     reachablePerimeter = filter(lambda cellEntry: isFirstReachable(notVisitedCells[cellEntry], notVisitedCells))
#     return set(reachablePerimeter.keys())


# def isFirstReachable(surroundingCells, notVisitedCells):
#     '''
#         Return True if any of the surrounding cells has been visited.
#         In other words, return True if the cell can be visited without passing
#         on unvisited cells.
#     '''
#     return any(cell not in notVisitedCells for cell in surroundingCells) 


# def getSurroundingCells(cell, cellMoves, accessibleMap):
#     '''
#         Given the accessible map, a cell position and the moves that can be taken
#         from that cell, return the position of the surrounding cells.
#     '''
#     newCells = [sumTuples(move, cell) for move in cellMoves]
#     return filter(lambda c: c in accessibleMap, newCells)
