# multiAgents.py
# --------------
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


from util import manhattanDistance
from game import Directions
import random
import util

from game import Agent


class ReflexAgent(Agent):
    """
    A reflex agent chooses an action at each choice point by examining
    its alternatives via a state evaluation function.

    The code below is provided as a guide.  You are welcome to change
    it in any way you see fit, so long as you don't touch our method
    headers.
    """

    def getAction(self, gameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {NORTH, SOUTH, WEST, EAST, STOP}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions as per evaluation method and choosen action
        scores = [self.evaluationFunction(
            gameState, action) for action in legalMoves]
        # It will pic the max score as best score
        bestScore = max(scores)
        bestIndices = [index for index in range(
            len(scores)) if scores[index] == bestScore]
        # Pick randomly among the best
        chosenIndex = random.choice(bestIndices)

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        stopAction = 'Stop'
        distanceXY = []

        # It will find pacman in game state
        pacmanSuccessorGameState = currentGameState.generatePacmanSuccessor(
            action)

        # It will fetch pacman postions in the game state
        newPos = pacmanSuccessorGameState.getPacmanPosition()
        pacmanPos = list(newPos)

        # IT will fetch the food postions in the current game state
        currentGSFoodList = currentGameState.getFood().asList()

        newGhostStates = pacmanSuccessorGameState.getGhostStates()

        # It will iterate the ghost and match with pacman postions and check if ghost are scared. IT
        # wiil return of ghost position is same as pacmand and ghose are not scared.
        for ghostState in newGhostStates:
            currentGhostScaredTimer = ghostState.scaredTimer
            ghostPos = ghostState.getPosition()
            if ghostPos == tuple(pacmanPos) and currentGhostScaredTimer == 0:
                return -float("inf")

        # Code will execute this block if legal action is not stop and will return the max distanced food from pacman

        if action != stopAction:
            for foodItem in currentGSFoodList:
                distance_x = -1*abs(foodItem[0] - pacmanPos[0])
                distance_y = -1*abs(foodItem[1] - pacmanPos[1])
                distanceXY.append(distance_x+distance_y)  # append the distance
            # Set distance that is maximum to maxDistacne variable
            maxDistance = max(distanceXY)
            return maxDistance
        elif action == stopAction:  # If action is Stop, it will return
            return -float("inf")


def scoreEvaluationFunction(currentGameState):
    """
    This default evaluation function just returns the score of the state.
    The score is the same one displayed in the Pacman GUI.

    This evaluation function is meant for use with adversarial search agents
    (not reflex agents).
    """
    return currentGameState.getScore()


class MultiAgentSearchAgent(Agent):
    """
    This class provides some common elements to all of your
    multi-agent searchers.  Any methods defined here will be available
    to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

    You *do not* need to make any changes here, but you can if you want to
    add functionality to all your adversarial search agents.  Please do not
    remove anything, however.

    Note: this is an abstract class: one that should not be instantiated.  It's
    only partially specified, and designed to be extended.  Agent (game.py)
    is another abstract class.
    """

    def __init__(self, evalFn='scoreEvaluationFunction', depth='2'):
        self.index = 0  # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)


class MinimaxAgent(MultiAgentSearchAgent):
    """
    Your minimax agent (question 2)
    """

    def getAction(self, gameState):
        """
        Returns the minimax action from the current gameState using self.depth
        and self.evaluationFunction.

        Here are some method calls that might be useful when implementing minimax.

        gameState.getLegalActions(agentIndex):
        Returns a list of legal actions for an agent
        agentIndex=0 means Pacman, ghosts are >= 1

        gameState.generateSuccessor(agentIndex, action):
        Returns the successor game state after an agent takes an action

        gameState.getNumAgents():
        Returns the total number of agents in the game

        gameState.isWin():
        Returns whether or not the game state is a winning state

        gameState.isLose():
        Returns whether or not the game state is a losing state
        """
        "*** YOUR CODE HERE ***"
        import math

        def TofindPlayer(chance, noOfAgents):
            """
            This function which decide which player to play game that is pacman or ghost

            """
            rem = chance-noOfAgents*(chance//noOfAgents)
            return rem

        def MIN_MAX_VALUE(gameState, chance):
            """
            This function is main function where different state is generated for respective  action  which take input respective 
            gamestate and chance is nothing but move given to player

            """
            # This list stores all scores of each player for that move
            Utility_Score = []
            # To find total no of agent in the game
            noOfAgent = gameState.getNumAgents()
            # depth of game tree is calculated in this step
            depth = math.floor(chance/noOfAgent)
            # To call evaluation function if game is won or loss or game is reched to deapth as given by command
            if gameState.isWin() or gameState.isLose() or depth == self.depth:
                return self.evaluationFunction(gameState)
            # To find which player is playing game that is o means pacman and > 0 means ghost
            player = TofindPlayer(chance, noOfAgent)
            # This step iterate the action by getting getAction function
            for action in gameState.getLegalActions(player):
                # This will store each utility score for indivual action and player(0 or >0) by  calling recursive function(MIN_MAX_VALUE)
                Individual_Score = MIN_MAX_VALUE(
                    gameState.generateSuccessor(player, action), chance+1)
                # Each individual score is stored in Utility_Score list
                Utility_Score.append(Individual_Score)
            # If player >0 it calls min vakue function to find minimum vakue
            if player > 0:

                return min_value(Utility_Score)
            # Else it will call max function to get max value
            else:

                return max_value(Utility_Score)

        def min_value(Utility_Score):
            """
            This function will find minimum from the list

            """
            mini = Utility_Score[0]
            for index in range(len(Utility_Score)):
                if Utility_Score[index] < mini:
                    mini = Utility_Score[index]
            return mini

        def max_value(Utility_Score):
            """
            This function will find maximum  from the list

            """
            maxi = Utility_Score[0]
            for index in range(len(Utility_Score)):
                if Utility_Score[index] > maxi:
                    maxi = Utility_Score[index]
            return maxi

        actions = gameState.getLegalActions(0)

        def element(x):
            """
            This function will call recursively  to MIN_MAX_VALUE function for given action

            """
            return MIN_MAX_VALUE(gameState.generateSuccessor(0, x), 1)
        # This will return pacman move that is max score for depth 0
        return max(actions, key=element)
        # util.raiseNotDefined()


class AlphaBetaAgent(MultiAgentSearchAgent):
    """
    Your minimax agent with alpha-beta pruning (question 3)
    """

    def getAction(self, gameState):
        """
        Returns the minimax action using self.depth and self.evaluationFunction
        """
        "*** YOUR CODE HERE ***"
        alphaScore = float("-INFINITY")
        betaScore = float("INFINITY")

        def max_agent(gameState, depth, alpha, beta):

            if gameState.isWin() or gameState.isLose() or depth == self.depth:
                return self.evaluationFunction(gameState)

            high_score = alphaScore
            score = high_score

            for action in gameState.getLegalActions(0):
                score = min_agent(gameState.generateSuccessor(
                    0, action), depth, 1, alpha, beta)

                if score > high_score:
                    high_score = score
                    move = action
                alpha = max(alpha, high_score)
                if high_score > beta:
                    return high_score

            if depth == 0:
                return move
            else:
                return high_score

        def min_agent(gameState, depth, player, alpha, beta):
            if gameState.isLose() or gameState.isWin() or depth == self.depth:
                return gameState.getScore()

            next_player = player + 1
            if player == gameState.getNumAgents() - 1:

                next_player = 0
            high_score = betaScore
            score = high_score

            for action in gameState.getLegalActions(player):
                if next_player == 0:

                    if depth == self.depth - 1:
                        score = self.evaluationFunction(
                            gameState.generateSuccessor(player, action))
                    else:
                        score = max_agent(gameState.generateSuccessor(
                            player, action), depth + 1, alpha, beta)
                else:
                    score = min_agent(gameState.generateSuccessor(
                        player, action), depth, next_player, alpha, beta)

                if score < high_score:
                    high_score = score
                beta = min(beta, high_score)

                if high_score < alpha:
                    return high_score

            return high_score

        return max_agent(gameState, 0, alphaScore, betaScore)
        util.raiseNotDefined()


class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """

    def getAction(self, gameState):
        """
        Returns the expectimax action using self.depth and self.evaluationFunction

        All ghosts should be modeled as choosing uniformly at random from their
        legal moves.
        """
        "*** YOUR CODE HERE ***"
        import math

        def TofindPlayer(chance, noOfAgents):
            """
            This function which decide which player to play game that is pacman or ghost

            """
            rem = chance-noOfAgents*(chance//noOfAgents)
            return rem

        def MIN_MAX_VALUE(gameState, chance):
            """
            This function is main function where different state is generated for respective  action  which take input respective 
            gamestate and chance is nothing but move given to player

            """
            # This list stores all scores of each player for that move
            Utility_Score = []
            # To find total no of agent in the game
            noOfAgent = gameState.getNumAgents()
            # depth of game tree is calculated in this step
            depth = math.floor(chance/noOfAgent)
            # To call evaluation function if game is won or loss or game is reched to deapth as given by command
            if gameState.isWin() or gameState.isLose() or depth == self.depth:
                return self.evaluationFunction(gameState)
            # To find which player is playing game that is o means pacman and > 0 means ghost
            player = TofindPlayer(chance, noOfAgent)

            for action in gameState.getLegalActions(player):
                # This will store each utility score for indivual action and player(0 or >0) by  calling recursive function(MIN_MAX_VALUE)
                Individual_Score = MIN_MAX_VALUE(
                    gameState.generateSuccessor(player, action), chance+1)
                # Each individual score is stored in Utility_Score list
                Utility_Score.append(Individual_Score)
            # This will find average all the score stored in Utility Score
            average = sum(Utility_Score)/len(Utility_Score)
            # If player >0 it will return average instead of min in minmax algorithm
            if player > 0:
                return float(average)
            # Else it will call max function to get max value
            else:
                return max_value(Utility_Score)

        def max_value(Utility_Score):
            """
            This function will find maximum  from the list

            """
            maxi = Utility_Score[0]
            for index in range(len(Utility_Score)):
                if Utility_Score[index] > maxi:
                    maxi = Utility_Score[index]
            return maxi

        actions = gameState.getLegalActions(0)

        def element(x):
            """
            This function will call recursively  to MIN_MAX_VALUE function for given action

            """
            return MIN_MAX_VALUE(gameState.generateSuccessor(0, x), 1)
        # This will return pacman move that is max score for depth 0
        return max(actions, key=element)
        util.raiseNotDefined()


def betterEvaluationFunction(currentGameState):
    """
    Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
    evaluation function (question 5).

    DESCRIPTION: We are returning values for Win and lose and after that we are stting food to food state from player, agentState to the state of the ghost and move to the position of pacman
    and all_food distance is a array of manhattan of all the food from pacman, nearest ghost for ghosts and scared ghost for all the ghost 
    when there scared time is zero and in the end we are returning a sort of score for the weightage of all the things 
    """
    "*** YOUR CODE HERE ***"
    if currentGameState.isWin():
        return 100000
    if currentGameState.isLose():
        return -100000

    foods = currentGameState.getFood()

    agentStates = currentGameState.getGhostStates()

    move = currentGameState.getPacmanPosition()

    all_food_distance = []

    for food in foods.asList():

        indi_food_dis = manhattanDistance(move, food)

        all_food_distance.append(indi_food_dis)

    nearestGobble = min(all_food_distance)
    Nearest_ghost = []

    for ghost in agentStates:

        pacman_in_danger = manhattanDistance(move, ghost.getPosition())

        if pacman_in_danger < 3:

            Nearest_ghost.append(pacman_in_danger)

    cover_me = sum(Nearest_ghost)
    scared_ghost = []

    for ghost in agentStates:
        if ghost.scaredTimer == 0:
            scared_ghost.append(ghost.scaredTimer)
        caught = sum(scared_ghost)

    weightage_position = currentGameState.getScore() * 20.0 + 2.0 / nearestGobble + \
        2.0 * float(cover_me) + 2.0 / (caught + 0.02)
    return weightage_position
    util.raiseNotDefined()


# Abbreviation
better = betterEvaluationFunction
