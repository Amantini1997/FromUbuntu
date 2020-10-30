# sampleAgents.py
# parsons/07-oct-2017
#
# Version 1.1
#
# Some simple agents to work with the PacMan AI projects from:
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

# The agents here are extensions written by Simon Parsons, based on the code in
# pacmanAgents.py

from pacman import Directions
from game import Agent
import api
import random
import game
import util

import numpy as np
import itertools

# RandomAgent
#
# A very simple agent. Just makes a random pick every time that it is
# asked for an action.
class RandomAgent(Agent):

    def getAction(self, state):
        # Get the actions we can try, and remove "STOP" if that is one of them.
        legal = api.legalActions(state)
        if Directions.STOP in legal:
            legal.remove(Directions.STOP)
        # Random choice between the legal options.
        return api.makeMove(random.choice(legal), legal)

# RandomishAgent
#
# A tiny bit more sophisticated. Having picked a direction, keep going
# until that direction is no longer possible. Then make a random
# choice.
class RandomishAgent(Agent):

    # Constructor
    #
    # Create a variable to hold the last action
    def __init__(self):
         self.last = Directions.STOP
    
    def getAction(self, state):
        # Get the actions we can try, and remove "STOP" if that is one of them.
        legal = api.legalActions(state)
        if Directions.STOP in legal:
            legal.remove(Directions.STOP)
        # If we can repeat the last action, do it. Otherwise make a
        # random choice.
        if self.last in legal:
            return api.makeMove(self.last, legal)
        else:
            pick = random.choice(legal)
            # Since we changed action, record what we did
            self.last = pick
            return api.makeMove(pick, legal)

# SensingAgent
#
# Doesn't move, but reports sensory data available to Pacman
class SensingAgent(Agent):

    def getAction(self, state):

        # Demonstrates the information that Pacman can access about the state
        # of the game.

        # What are the current moves available
        legal = api.legalActions(state)
        print "Legal moves: ", legal

        # Where is Pacman?
        pacman = api.whereAmI(state)
        print "Pacman position: ", pacman

        # Where are the ghosts?
        print "Ghost positions:"
        theGhosts = api.ghosts(state)
        for i in range(len(theGhosts)):
            print theGhosts[i]

        # How far away are the ghosts?
        print "Distance to ghosts:"
        for i in range(len(theGhosts)):
            print util.manhattanDistance(pacman,theGhosts[i])

        # Where are the capsules?
        print "Capsule locations:"
        print api.capsules(state)
        
        # Where is the food?
        print "Food locations: "
        print api.food(state)

        # Where are the walls?
        print "Wall locations: "
        print api.walls(state)
        
        # getAction has to return a move. Here we pass "STOP" to the
        # API to ask Pacman to stay where they are.
        return api.makeMove(Directions.STOP, legal)







# ============== My Agents ====================
# GoWestAgent
#
# Tries to go WEST, when this is not possible.
class GoWestAgent(Agent):

    # Constructor
    #
    # Create a variable to hold the last action
    def __init__(self):
         self.last = Directions.STOP
         self.preferred = Directions.WEST
    
    def getAction(self, state):
        # Get the actions we can try, and remove "STOP" if that is one of them.
        legal = api.legalActions(state)
        if Directions.STOP in legal:
            legal.remove(Directions.STOP)
        # If we can repeat the last action, do it. Otherwise make a
        # random choice.
        if self.preferred in legal:
            self.last = self.preferred
            return api.makeMove(self.preferred, legal)
        elif self.last in legal:
            return api.makeMove(self.last, legal)
        elif Directions.NORTH in legal or Directions.SOUTH in legal:
            non_EAST_directions = []
            if Directions.NORTH in legal: 
                non_EAST_directions.append(Directions.NORTH)
            if Directions.SOUTH in legal: 
                non_EAST_directions.append(Directions.SOUTH)
            pick = random.choice(non_EAST_directions)
            # Since we changed action, record what we did
            self.last = pick
            return api.makeMove(pick, legal)
            # return api.makeMove(pick, non_EAST_directions)

        else:
            self.last = Directions.EAST
            return api.makeMove(self.last, legal)


# HungryAgent
#
# A tiny bit more sophisticated. Having picked a direction, keep going
# until that direction is no longer possible. Then make a random
# choice.
class HungryAgent(Agent):

    def __init__(self):
        self.lastPosition = Directions.NORTH
        self.oppositeDirections = {
            Directions.SOUTH: Directions.NORTH,
            Directions.NORTH: Directions.SOUTH,
            Directions.EAST: Directions.WEST,
            Directions.WEST: Directions.EAST     
        }
        self.lastBestFoodPosition = None
        self.lastMinimumDistance = None

    def getAction(self, state):

        # What are the current moves available
        legal = api.legalActions(state)
        if Directions.STOP in legal:
            legal.remove(Directions.STOP)

        # # Where is Pacman?
        pacman = api.whereAmI(state)

        # # Where are the ghosts?
        theGhosts = api.ghosts(state)

        # # How far away are the ghosts?
        # print "Distance to ghosts:"
        # for i in range(len(theGhosts)):
        #     print util.manhattanDistance(pacman,theGhosts[i])

        # # Where are the capsules?
        # print "Capsule locations:"
        # print api.capsules(state)
        
        # # Where is the food?
        food = api.food(state)
        foodDistances = [(util.manhattanDistance(pacman, point), index) for index, point in enumerate(food)]
        sortedFoodDistances = sorted(foodDistances)
        DISTANCE = 0
        FOOD_INDEX = 1
        firstFood = sortedFoodDistances[0]
        secondFood = sortedFoodDistances[1]
        closestFood = food[firstFood[FOOD_INDEX]]

        # if firstFood[DISTANCE] == secondFood[DISTANCE]:
        #     closestFood = food[firstFood[FOOD_INDEX] if firstFood[FOOD_INDEX] < secondFood[FOOD_INDEX] else secondFood[FOOD_INDEX]]

        xyDistanceToClosestFood = manhattanNotAbsoluteDistance(closestFood, pacman)

        # if new closest food is not closer than the previous one
        # swipe it with the saved closest food
        if (self.lastMinimumDistance and
           sum(xyDistanceToClosestFood) > 1 and
           pacman != self.lastBestFoodPosition):

            if sum(xyDistanceToClosestFood) > sum(self.lastMinimumDistance):
                print "Last Min Distance: ", self.lastMinimumDistance
                print "Last Best Food: ", self.lastBestFoodPosition
                print "ActualDistToClosestFood: ", xyDistanceToClosestFood

                closestFood = self.lastBestFoodPosition
                print "CLOSEST_FOOD: ", closestFood
                xyDistanceToClosestFood = manhattanNotAbsoluteDistance(closestFood, pacman)
            
            elif sum(xyDistanceToClosestFood) == sum(self.lastMinimumDistance):
                pass

        # update pacman knowledge
        self.lastMinimumDistance = xyDistanceToClosestFood
        self.lastBestFoodPosition = closestFood

        print " PAC: ", pacman, "CLOSEST FOOD: ", closestFood, "  DISTANCE FROM IT: ", xyDistanceToClosestFood

        bestMoves = getBestNextMoves(legal, xyDistanceToClosestFood)
        
        # print "Food locations: "
        # print food

        # # Where are the walls?
        # print "Wall locations: "
        # print api.walls(state)

        # AVOID LOOP
        print "BEST MOVES", bestMoves, "  LEGAL: ", legal
        print "LAST POSITION: ", self.lastPosition

        # avoid ghost traplastPosition TODO
        # if self.lastPosition in bestMoves:
        #     return api.makeMove(self.lastPosition, legal)

        # prevent coming back (AVOID LOOP)
        if self.lastPosition in bestMoves and len(bestMoves) > 1:
            bestMoves.remove(self.lastPosition)
            print "REMOVED LAST POSITION: ", self.lastPosition
            print "NEW BEST MOVES: ", bestMoves



        pick = random.choice(bestMoves)
        self.lastPosition = self.oppositeDirections[pick]
        raw_input()
        print "\n====================================\n"
        return api.makeMove(pick, legal)


def manhattanNotAbsoluteDistance( xy1, xy2 ):
    "Returns the Manhattan distance between points xy1 and xy2"
    return ( xy1[0] - xy2[0], xy1[1] - xy2[1] )


def getBestNextMoves(legal, closestPointDistancesXY):
    '''
    Given the legal moves and the closes point to pacman,
    Calculates and return the best moves Direction wise
    as an array
    '''
    EAST_DISTANCE = closestPointDistancesXY[0]
    NORTH_DISTANCE = closestPointDistancesXY[1]

    bestMoves = []
    # x-axis move
    if EAST_DISTANCE >= 0 and Directions.EAST in legal:
        bestMoves.append(Directions.EAST)
    elif EAST_DISTANCE <= 0 and Directions.WEST in legal:
        bestMoves.append(Directions.WEST)
    # y-axis move
    if NORTH_DISTANCE >= 0 and Directions.NORTH in legal:
        bestMoves.append(Directions.NORTH)
    elif NORTH_DISTANCE <= 0 and Directions.SOUTH in legal:
        bestMoves.append(Directions.SOUTH)

    # print "EAST_D: ", EAST_DISTANCE, "  NORTH_D: ", NORTH_DISTANCE

    return bestMoves


# WORKING
def getFullWallAndPerimeterFromWallBlock(block, walls):
    ''' 
    Given a block and the walls map,
    return perimeter and full wall of the block
    '''
    # print block
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
        


def sumTuples(tuple1, tuple2):
    return tuple([(i + j) for i, j in zip(tuple1, tuple2)])


