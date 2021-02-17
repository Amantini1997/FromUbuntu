# classifierAgents.py
# parsons/07-oct-2017
#
# Version 1.0
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
import sys
import os
import csv
import numpy as np
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
from sklearn.model_selection import train_test_split, KFold

from math import log, floor
from collections import Counter

# ClassifierAgent
#
# An agent that runs a classifier to decide what to do.
class ClassifierAgent(Agent):

    counter = 0

    # Constructor. This gets run when the agent starts up.
    def __init__(self):
        print "Initialising"

    # Take a string of digits and convert to an array of
    # numbers. Exploits the fact that we know the digits are in the
    # range 0-4.
    #
    # There are undoubtedly more elegant and general ways to do this,
    # exploiting ASCII codes.
    def convertToArray(self, numberString):
        numberArray = []
        for i in range(len(numberString) - 1):
            if numberString[i] == '0':
                numberArray.append(0)
            elif numberString[i] == '1':
                numberArray.append(1)
            elif numberString[i] == '2':
                numberArray.append(2)
            elif numberString[i] == '3':
                numberArray.append(3)
            elif numberString[i] == '4':
                numberArray.append(4)

        return numberArray
                
    # This gets run on startup. Has access to state information.
    #
    # Here we use it to load the training data.
    def registerInitialState(self, state):

        # open datafile, extract content into an array, and close.
        self.datafile = open('good-moves.txt', 'r')
        content = self.datafile.readlines()
        self.datafile.close()

        # Now extract data, which is in the form of strings, into an
        # array of numbers, and separate into matched data and target
        # variables.
        self.data = []
        self.target = []
        # Turn content into nested lists
        for i in range(len(content)):
            lineAsArray = self.convertToArray(content[i])
            dataline = []
            for j in range(len(lineAsArray) - 1):
                dataline.append(lineAsArray[j])

            self.data.append(dataline)
            targetIndex = len(lineAsArray) - 1
            self.target.append(lineAsArray[targetIndex])

        # data and target are both arrays of arbitrary length.
        #
        # data is an array of arrays of integers (0 or 1) indicating state.
        #
        # target is an array of imtegers 0-3 indicating the action
        # taken in that state.
        self.classifier = RandomForestClassifier()
        self.classifier.fit(X_train, y_train)

        
    # Tidy up when Pacman dies
    def final(self, state):

        print "I'm done!"
        
        # *********************************************
        #
        # Any code you want to run at the end goes here.
        #
        # *********************************************

    # Turn the numbers from the feature set into actions:
    def convertNumberToMove(self, number):
        if number == 0:
            return Directions.NORTH
        elif number == 1:
            return Directions.EAST
        elif number == 2:
            return Directions.SOUTH
        elif number == 3:
            return Directions.WEST

    # Here we just run the classifier to decide what to do
    def getAction(self, state):

        # How we access the features.
        features = api.getFeatureVector(state)
        
        # *****************************************************
        #
        # Here you should insert code to call the classifier to
        # decide what to do based on features and use it to decide
        # what action to take.
        #
        # *******************************************************

        # Get the actions we can try.
        legal = api.legalActions(state)

        move = self.classifier.predict(features)
        move1 = self.sklearn_classifier.predict([features])
        move = self.convertNumberToMove(move)
        # move = self.convertNumberToMove(move[0])
        # getAction has to return a move. Here we pass "STOP" to the
        # API to ask Pacman to stay where they are. We need to pass
        # the set of legal moves to teh API so it can do some safety
        # checking.
        return api.makeMove(move, legal)




class Node(object):

    # the set of values that each feature may assume
    FEATURES_VALUES_SET = {0, 1}

    def __init__(self, 
                 feature_value=None, 
                 max_depth=100, 
                 depth=0,
                 parent=None,
                 X = [],
                 y = []):
                 
        # the index of the feature used to make the split is stored
        # in feature_index_used_to_split. 
        self.feature_index_used_to_split = None
        # each entry uses as key the respective value 
        # of the feature used to make the split.
        self.children = {}
        
        self.max_depth = max_depth
        self.depth = depth
        self.parent = parent
        self.prediction = None
        
        self.X = np.array(X)
        self.y = np.array(y)
        self.M = len(X)


    def add_element(self, element, label):
        self.M += 1
        self.X = np.append(self.X, element).reshape(self.M, len(element))
        self.y = np.append(self.y, label)


    def get_entropy(self):
        entropy = 0
        if self.M == 0:
            return entropy

        counter = Counter(self.y)
        for label_count in counter.itervalues():
            # If the count a label is 0, the entropy is not affected
            # and its update is skipped
            if label_count > 0:
                label_probability = float(label_count) / self.M
                entropy -= (label_probability * log(label_probability, 2))

        return entropy


    def get_information_gain(self, children):
        self_entropy = self.get_entropy()
        children_entropy = 0
        for child in children:
            children_entropy += child.M * child.get_entropy() / self.M 
        return self_entropy - children_entropy


    def train(self):
        if self.M == 4 and self.depth == 6:
            pass
        if len(set(self.y)) == 1:
            # there exists just one label in this node,
            # so the prediction will such label
            self.prediction = self.y[0]
        
        elif self.max_depth == self.depth:
            # the tree has reached the max_depth, so
            # prediction is based on the current labels
            self.prediction = self.get_most_frequent_label()

        elif self.M == 0:
            # no samples are contained in this node after the
            # split, so prediction is be based on parent
            # knowledge.
            self.prediction = self.parent.get_most_frequent_label() 

        elif len(self.X[0]) == 0:
            # all the features have been used and more than 
            # one label is still present in this node, so
            # prediction is based on the current labels
            self.prediction = self.get_most_frequent_label()

        else:
            # generate children and train them
            self.generate_children()
            for child in self.children.values():
                child.train()
        
    def generate_children(self):
        best_information_gain = -1
        best_children = []
        best_feature_index = None

        # TODO decide how many features to use
        n_features = len(self.X[0])
        features_used_to_split = int( max( 1, floor(float(n_features) / 3) ) )
        random_features_indexes = np.random.choice(n_features, size=features_used_to_split, replace=False)

        # identify the split with the best information gain
        for feature_index in random_features_indexes:
            children = self.split_node_by_feature(feature_index)
            information_gain = self.get_information_gain(children.values())
            if information_gain > best_information_gain:
                best_information_gain = information_gain
                best_children = children
                best_feature_index = feature_index
        

        # if any(child.M == 0 for child in best_children.values()):
        #     # any further split would not improve the information
        #     # gain, stop training here
        #     self.prediction = self.get_most_frequent_label()
        #     return

        self.children = best_children
        self.feature_index_used_to_split = best_feature_index



    def predict(self, X):
        if self.prediction != None:
            # the node is a leaf
            return self.prediction
        else:
            x = X[self.feature_index_used_to_split]
            next_node = self.children[x]
            
            # remove the feature used for the split of the current 
            # node from the datapoints passed to the children
            new_X = np.delete(X, self.feature_index_used_to_split)
            child_prediction = next_node.predict(new_X)

            if child_prediction == None:
                child_prediction = self.get_most_frequent_label()
            return child_prediction


    def split_node_by_feature(self, feature_index):
        # get the values of the training set of the 
        # feature indexed at feature_index
        feature_values = self.X[:, feature_index]

        feature_value_to_node = {}
        
        # for each value that a feature may assume, create a new node
        # and save an entry (value -> node) in the dict feature_value_to_node
        for feature_value in self.FEATURES_VALUES_SET:
            new_node = Node(max_depth=self.max_depth, 
                            depth=(self.depth+1),
                            feature_value=feature_value,
                            parent=self)
            feature_value_to_node[feature_value] = new_node

        # for each datapoint, populate the node which is generated
        # by the respective value of the feature used to split
        for i in range(self.M):
            current_feature_value = int(feature_values[i])
            node = feature_value_to_node[current_feature_value]
            X = np.delete(self.X[i], feature_index)
            y = self.y[i]
            node.add_element(X, y)

        return feature_value_to_node


    def get_most_frequent_label(self):
        labels_counter = Counter(self.y)
        # find how many times the most frequent label occurs
        most_frequent_label_count = labels_counter.most_common(1)[0][-1] 
        # more than one label could appear with the most frequency
        # so we include all of them and then randomly select one
        most_frequent_labels = [
            label 
            for label, count in labels_counter.iteritems() 
            if count == most_frequent_label_count
        ]
        return np.random.choice(most_frequent_labels)

    
class Root(Node):

    def __init__(self, max_depth=100):
        super(Root, self).__init__(max_depth=max_depth, depth=0)


    def train(self, X, y):            
        # filter out the non-selected features
        self.X = X
        self.y = y
        self.M = len(X)

        super(Root, self).train()


class DecisionTreeClassifier(object):
    
    def __init__(self, max_depth=100, random_state=0):
        self.max_depth = max_depth
        np.random.seed(random_state)

    def fit(self, X, y):
        self.root = Root(max_depth=self.max_depth)
        self.root.train(X, y)

    def predict(self, X):
        return self.root.predict(X)


class RandomForestClassifier(object):

    def __init__(self, max_depth=100, random_state=0, n_estimators=10, probabilistic=False):
        '''
            A random forest classifier.
            

            Parameters
            ----------
            max_depth : integer, optional (default=100)
                The maximum depth of each tree.

            
            random_state : integer, optional (default=0)
                The number used to set the random seed.

            
            n_estimators : integer, optional (default=5)
                The number of trees in the forest.

            
            probabilistic : boolean, optional (default=False)
                The way the random forest decide on which prediction to 
                consider correct. If probabilistic is set to True, each 
                vote has equal probability of being picked as the final
                prediction. If False, the most voted prediction is used
                instead.
        '''
        self.max_depth = max_depth
        np.random.seed(random_state)
        self.n_estimators = n_estimators
        self.probabilistic = probabilistic
        # self.kf = KFold(n_splits=n_splits)


    def fit(self, X, y):
        # map input array to numpy arrays for the nodes
        X = np.array(X)
        y = np.array(y)
        M = len(X)

        self.trees = []
        # for k_fold_split, _ in self.kf.split(X):

        for i in range(self.n_estimators):

            # Bootstrap data
            bootstrapped_X = self.bootstrap(X, M)
            tree = Root(max_depth=self.max_depth)
            tree.train(bootstrapped_X, y)
            self.trees.append(tree)


    def predict(self, X):
        '''
        Select the prediction for each Tree and get the most
        frequent prediction. In case more one prediction share
        the same highest frequency, randomly pick one.
        '''

        '''
           Predict class for feature vector X.

            The predicted class of an input sample is a vote by the trees in
            the forest, weighted by their probability estimates. That is,
            the predicted class is the one with highest mean probability
            estimate across the trees.

            Parameters
            ----------
            X : array-like or sparse matrix of shape = [n_samples, n_features]
                The input samples. Internally, its dtype will be converted to
                ``dtype=np.float32``. If a sparse matrix is provided, it will be
                converted into a sparse ``csr_matrix``.

            Returns
            -------
            y : array of shape = [n_samples] or [n_samples, n_outputs]
                The predicted classes.
        '''
        X = np.array(X)
        predictions = [tree.predict(X) for tree in self.trees]

        if self.probabilistic:
            # prediction is taken randomly among all the votes
            # of the trees. Each vote has equal probability of 
            # being selected (note that this does not mean that
            # each prediction has the same probability).
            max_prediction = np.random.choice(predictions)
        else:
            # the final prediction is the most voted one (in case
            # of tie, a random one is selected with equal probability)

            predictions_counter = Counter(predictions)
            # find how many times the most frequent prediction occurs
            most_frequent_prediction_count = predictions_counter.most_common(1)[0][-1] 
            # more than one prediction could appear with the most frequency
            # so we include all of them and then randomly select one
            most_frequent_predictions = [
                prediction 
                for prediction, count in predictions_counter.iteritems() 
                if count == most_frequent_prediction_count
            ]
            max_prediction = np.random.choice(most_frequent_predictions)
        return max_prediction

    
    def bootstrap(self, X, n_samples):
        random_indexes = np.random.randint(len(X), size=n_samples)
        # random_indexes.sort()
        return X[random_indexes]