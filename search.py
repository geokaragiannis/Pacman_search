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
import searchAgents

class Node:

  def __init__(self, state, parent):
    self.state = state
    self.parent = parent

  def getState(self):
    return self.state
  def getParent(self):
    return self.parent

  def getSolutionBfs(self):

    sol = []
    sol.insert(0, self.state)
    parent = self.parent
    while parent.getParent() is not None:
      sol.insert(0, parent.getState())
      parent = parent.getParent()
    # print 'solution: ', sol
    return sol

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

  #TODO if the init state is a solution, then return the empty list 
  from game import Directions
  s = Directions.SOUTH
  w = Directions.WEST
  e = Directions.EAST
  n = Directions.NORTH

  # list that holds the states already visited
  explored = set()
  # LIFO stack
  fringe = util.Stack()
  # Dict that for each node n pathDict[n] = parent of n + direction from parent->child
  pathDict = dict()

  startState = Node((problem.startingState(), 'None', 0), None)
  fringe.push(startState)
  returnList = []

  while not fringe.isEmpty():

    parent = fringe.pop()

    # if the parent is the init state, then parent = (x,y)
    # and not ((x,y), Direction, cost). So only get the (x,y)
    if len(parent) == 3:
      parentState = parent[0]
    else:
      parentState = parent

    if problem.isGoal(parentState):
      return formatSolution(getSolutionDfs(pathDict, parent, problem.startingState()))

    # add to explored if not already visited
    if parentState not in explored:
      # print 'parent state ', parentState
      explored.append(parentState)

      for child in problem.successorStates(parentState):
        if child[0] not in explored:
          fringe.push(child)
          # update the dict for a state that we visit for the 
          # first time
          pathDict[child[0]] = parent
          

  #util.raiseNotDefined()
  # return failure if the stack is empty
  return []

# go through the Dictionary, starting from the goal state and ending 
# in the first state. Returns a list
def getSolutionDfs(pathDict, goal, startState):
  sol = []
  sol.insert(0, goal)
  temp = pathDict[goal[0]]
  print 'goal ', goal[0]
  while temp[0] in pathDict:
    sol.insert(0,temp)
    # print pathDict[temp[0]]
    # if pathDict[temp[0]] is not None:
    #   temp = pathDict[temp[0]]
    # else:
    #   temp = None
    temp = pathDict[temp[0]]
    # temp = pathDict[temp[0]] if pathDict[temp[0]] else None
    # if temp[0] == startState or temp is None:
    #   break
  return sol

def getSolutionUcs(pathDict, goal, startState):
  sol = []
  temp = goal
  print 'goal ', goal[0]
  while temp is not None:
    sol.insert(0,temp)
    # print pathDict[temp[0]]
    if pathDict[temp[0]] is not None:
      temp = pathDict[temp[0]]
    else:
      temp = None
    # temp = pathDict[temp[0]] if pathDict[temp[0]] else None
    if temp[0] == startState or temp is None:
      break
  return sol

# format a list, so that it looks like [s,s,w,...]
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

  return sol



def breadthFirstSearch(problem):
  "Search the shallowest nodes in the search tree first. [p 81]"

  # list that holds the states already visited
  explored = set()  # FIFO Queue
  fringe = util.Queue()
  # Dict that for each node n pathDict[n] = parent of n + direction from parent->child
  pathDict = dict()

  startState = Node((problem.startingState(), 'None', 0), None)
  fringe.push(startState)
  returnList = []

  while not fringe.isEmpty():

    # if the parent is the init state, then parent = (x,y)
    # and not ((x,y), Direction, cost). So only get the (x,y)
    parent = fringe.pop()
    parentInfo = parent.getState()
    parentState = getPositionFromState(parentInfo)
    print 'parent info: ', parentInfo
    print 'parent state: ', parentState

    if problem.isGoal(parentState):
      return formatSolution(parent.getSolutionBfs())

    # add to explored if not already visited
    if parentState not in explored:
      # print 'parent state ', parentState
      explored.add(parentState)

      for child in problem.successorStates(parentState):
        # if child[0] not in explored:
          
          # update the dict for a state that we visit for the 
          # first time
        # pathDict[child[0]] = parent
        print 'the parent of ', child[0], 'is ', parent
        # print 'pathDict: ', pathDict
        childNode = Node(child, parent)
        fringe.push(childNode)
          

  print 'path dict: ', pathDict
  print 'return list ', returnList

  #util.raiseNotDefined()
  # return failure if the stack is empty
  return []
  # util.raiseNotDefined()

def getPositionFromState(state):
  stateInformation = state[0] 
  for item in stateInformation:
    if item is tuple and len(item) == 2:
      # this will most likely be the position
      return item
  
  return stateInformation      
def uniformCostSearch(problem):
  "Search the node of least total cost first. "
  explored = set()
  # Dict that for each node n pathDict[n] = parent of n + direction from parent->child
  pathDict = dict()
  # Dict that holds the commulative cost for each key. 
  costDict = dict()

  fringe = util.PriorityQueue()
  fringe.push((problem.startingState(), 'None', 0),  0)
  costDict[problem.startingState()] = 0

  while not fringe.isEmpty():

    parent = fringe.pop()
    parentState = parent[0]
    parentCost = parent[2]

    if problem.isGoal(parentState):
      # print 'dict: ', pathDict
      return formatSolution(getSolutionUcs(pathDict, parent, problem.startingState()))

    # add to explored if not already visited
    # if parentState not in explored:
    explored.add(parentState)

    for child in problem.successorStates(parentState):
      if child[0] not in explored and child[0] not in selectStates(fringe.heap):
      # update the dict for a state that we visit for the
        costDict[child[0]] = child[2] + costDict[parentState]      
        pathDict[child[0]] = parent
        fringe.push(child, costDict[child[0]])
      else:
        # if the cost of child is less that the cost of the element e in the costDict
        # then do pathDict[e] = parent
        otherState = findChild(fringe.heap, child[0])
        if otherState is not None: 
          if costDict[otherState] < costDict[child[0]]:
            print 'here'
            pathDict[otherState] = parent


  # util.raiseNotDefined()

# finds an element e in explored such as e[0] = childState[0], given that
# this element exists
def findChild(fringe, childState):
  for state in fringe:
    # print 'cgild: ', childState
    # print 'state: ', state[1][0]
    if state[1][0] == childState:
      return state[1][0]
  # print '----------------------'
  return None

# takes a list/set with tuples as elements and returns
# a set with the coordinates as elements
def selectStates(explored):
  sol = set()
  if explored is None: 
    return sol
  for e in explored:
    sol.add(e[0])
  return sol

def nullHeuristic(state, problem=None):
  """
  A heuristic function estimates the cost from the current state to the nearest
  goal in the provided SearchProblem.  This heuristic is trivial.
  """
  return 0

def aStarSearch(problem, heuristic=nullHeuristic):
  explored = set()
  # Dict that for each node n pathDict[n] = parent of n + direction from parent->child
  pathDict = dict()
  # Dict that holds the commulative cost for each key. 
  costDict = dict()

  fringe = util.PriorityQueue()
  fringe.push((problem.startingState(), 'None', 0),  0)
  costDict[problem.startingState()] = 0

  while not fringe.isEmpty():

    parent = fringe.pop()
    parentState = parent[0]
    parentCost = parent[2]

    if problem.isGoal(parentState):
      # print 'dict: ', pathDict
      return formatSolution(getSolutionUcs(pathDict, parent, problem.startingState()))

    # add to explored if not already visited
    # if parentState not in explored:
    explored.add(parentState)

    for child in problem.successorStates(parentState):
      if child[0] not in explored and child[0] not in costDict:
      # update the dict for a state that we visit for the
        costDict[child[0]] = child[2] + costDict[parentState]     
        pathDict[child[0]] = parent
        fringe.push(child, costDict[child[0]] + heuristic(child[0], problem))
      else:
        # if the cost of child is less that the cost of the element e in the costDict
        # then do pathDict[e] = parent
        if costDict[child[0]] is not None: 
          if costDict[child[0]] > child[2] + costDict[parentState]:
            costDict[child[0]] = child[2] + costDict[parentState]     
            pathDict[child[0]] = parent
            fringe.push(child, costDict[child[0]] + heuristic(child[0], problem))
            print 'here'
            # costDict[otherState] = otherState[2] + costDict[parentState] + heuristic(otherState[0], problem) - heuristic(pathDict[otherState][0], problem)
            # pathDict[otherState] = parent
  # util.raiseNotDefined()
    
# cost to get from a state n to the goal
# calls searchAgents.manhattanDistance
def h(n, problem):
  return searchAgents.manhattanHeuristic(n[0], problem)

# returns the cost to get to state n 
def g(n):
  return n[2] 

def f(n, problem):
  return h(n, problem) + g(n)
  
# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
