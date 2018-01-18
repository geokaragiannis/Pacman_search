# search.py
# ---------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

"""
In search.py, you will implement generic search algorithms which are called 
by Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
  """
  This class outlines the structure of a search problem, but doesn't implement
  any of the methods (in object-oriented terminology: an abstract class).
  
  You do not need to change anything in this class, ever.
  """
  
  def startingState(self):
    """
    Returns the start state for the search problem 
    """
    util.raiseNotDefined()

  def isGoal(self, state): #isGoal -> isGoal
    """
    state: Search state

    Returns True if and only if the state is a valid goal state
    """
    util.raiseNotDefined()

  def successorStates(self, state): #successorStates -> successorsOf
    """
    state: Search state
     For a given state, this should return a list of triples, 
     (successor, action, stepCost), where 'successor' is a 
     successor to the current state, 'action' is the action
     required to get there, and 'stepCost' is the incremental 
     cost of expanding to that successor
    """
    util.raiseNotDefined()

  def actionsCost(self, actions): #actionsCost -> actionsCost
    """
      actions: A list of actions to take
 
     This method returns the total cost of a particular sequence of actions.  The sequence must
     be composed of legal moves
    """
    util.raiseNotDefined()
           

def tinyMazeSearch(problem):
  """
  Returns a sequence of moves that solves tinyMaze.  For any other
  maze, the sequence of moves will be incorrect, so only use this for tinyMaze
  """
  from game import Directions
  s = Directions.SOUTH
  w = Directions.WEST
  return  [s,s,w,s,w,w,s,w]

def depthFirstSearch(problem):
  """
  Search the deepest nodes in the search tree first [p 85].
  
  Your search algorithm needs to return a list of actions that reaches
  the goal.  Make sure to implement a graph search algorithm [Fig. 3.7].
  
  To get started, you might want to try some of these simple commands to
  understand the search problem that is being passed in:
  
  print "Start:", problem.startingState()
  print "Is the start a goal?", problem.isGoal(problem.startingState())
  print "Start's successors:", problem.successorStates(problem.startingState())
  """

  from game import Directions
  s = Directions.SOUTH
  w = Directions.WEST
  e = Directions.EAST
  n = Directions.NORTH

  print "Start:", problem.startingState()
  print "Is the start a goal?", problem.isGoal(problem.startingState())
  print "Start's successors:", problem.successorStates(problem.startingState())

  explored = []
  fringe = util.Stack()
  pathDict = dict()

  fringe.push(problem.startingState())
  returnList = []

  while not fringe.isEmpty():
    if problem.isGoal(parentState):
      returnList = getSolutionDfs(pathDict, parent, problem.startingState())

    parent = fringe.pop()

    if len(parent) == 3:
      parentState = parent[0]
    else:
      parentState = parent

    # print 'fringe ', fringe.list
    # print 'explored ', explored

    

    if parentState not in explored:
      print 'parent state ', parentState
      explored.append(parentState)

      for child in problem.successorStates(parentState):

        if child[0] not in explored:
          fringe.push(child)
          pathDict[child[0]] = parent

  print 'path dict: ', pathDict
  print 'return list ', returnList

  #util.raiseNotDefined()

  return formatSolution(returnList)


def getSolutionDfs(pathDict, goal, startState):
  sol = []
  temp = goal
  while temp is not None:
    sol.insert(0,temp)
    temp = pathDict[temp[0]] if pathDict[temp[0]] else None
    if temp == startState:
      break
    
  return sol



def formatSolution(frontier):

  from game import Directions
  s = Directions.SOUTH
  w = Directions.WEST
  e = Directions.EAST
  n = Directions.NORTH

  sol = []
  for item in frontier:
    if item[1] == 'South':
      sol.append(s)
    elif item[1] == 'North':
      sol.append(n)
    elif item[1] == 'West':
      sol.append(w)
    elif item[1] == 'East':
      sol.append(e)

  #print 'lala ', sol

  return sol


def breadthFirstSearch(problem):
  "Search the shallowest nodes in the search tree first. [p 81]"
  util.raiseNotDefined()
      
def uniformCostSearch(problem):
  "Search the node of least total cost first. "
  util.raiseNotDefined()

def nullHeuristic(state, problem=None):
  """
  A heuristic function estimates the cost from the current state to the nearest
  goal in the provided SearchProblem.  This heuristic is trivial.
  """
  return 0

def aStarSearch(problem, heuristic=nullHeuristic):
  "Search the node that has the lowest combined cost and heuristic first."
  util.raiseNotDefined()
    

  
# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
