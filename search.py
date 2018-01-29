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

# Data Structure for a node in the graph. Each node has a state
# and a parent. getSolution traces back from a state s to its parent
# until we cannot go back any futher
class Node:

  def __init__(self, state, parent=None, cost=0):
    self.state = state
    self.parent = parent
    self.cost = cost

  def getState(self):
    return self.state
  def getParent(self):
    return self.parent
  def getCost(self):
    return self.cost

  def getSolution(self):

    sol = []
    sol.insert(0, self.state)
    parent = self.parent
    while parent.getParent() is not None:
      sol.insert(0, parent.getState())
      parent = parent.parent
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
    parentObj = parent.getState()
    parentState = parentObj[0]

    if problem.isGoal(parentState):
      return formatSolution(parent.getSolution())

    # add to explored if not already visited
    if parentState not in explored:
      # print 'parent state ', parentState
      explored.add(parentState)

      for child in problem.successorStates(parentState):
        childNode = Node(child, parent)
        fringe.push(childNode)
          

  #util.raiseNotDefined()
  # return failure if the stack is empty
  return []


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
    parentObj = parent.getState()
    parentState = parentObj[0]


    if problem.isGoal(parentState):
      return formatSolution(parent.getSolution())

    # add to explored if not already visited
    if parentState not in explored:
      explored.add(parentState)

      for child in problem.successorStates(parentState):
        childNode = Node(child, parent)
        fringe.push(childNode)
          

  print 'path dict: ', pathDict
  print 'return list ', returnList
  # return failure if the stack is empty
  return []
  # util.raiseNotDefined()

def uniformCostSearch(problem):
  "Search the node of least total cost first. "
  explored = set()
  # Dict that for each node n pathDict[n] = parent of n + direction from parent->child
  pathDict = dict()
  # Dict that holds the commulative cost for each key. 
  costDict = dict()

  fringe = util.PriorityQueue()
  startState = Node((problem.startingState(), 'None', 0), None)
  fringe.push(startState, 0)
  costDict[problem.startingState()] = 0

  while not fringe.isEmpty():

    parent = fringe.pop()
    parentObj = parent.getState()
    parentState = parentObj[0]
    if problem.isGoal(parentState):
      # print 'dict: ', pathDict
      return formatSolution(parent.getSolution())

    # add to explored if not already visited
    # if parentState not in explored:
    explored.add(parentState)

    for child in problem.successorStates(parentState):
      childState = child[0]
      if childState not in explored and childState not in selectStates(fringe.heap):
      # update the dict for a state that we visit for the
        costDict[child[0]] = child[2] + costDict[parentState]      
        pathDict[child[0]] = parent
        childNode = Node(child, parent, child[2] + parent.getCost())
        fringe.push(childNode, childNode.getCost())


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
  startState = Node((problem.startingState(), 'None', 0), None)
  fringe.push(startState, 0)
  costDict[problem.startingState()] = 0

  while not fringe.isEmpty():

    parent = fringe.pop()
    parentObj = parent.getState()
    parentState = parentObj[0]

    if problem.isGoal(parentState):
      return formatSolution(parent.getSolution())

    # add to explored if not already visited
    # if parentState not in explored:
    explored.add(parentState)

    for child in problem.successorStates(parentState):
      childState = child[0]
      if childState not in explored and childState not in selectStates(fringe.heap):
      # update the dict for a state that we visit for the
        costDict[child[0]] = child[2] + costDict[parentState]     
        pathDict[child[0]] = parent
        childNode = Node(child, parent, child[2] + parent.getCost())
        cost = childNode.getCost() + heuristic(childState, problem)
        fringe.push(childNode, cost)
    
  
# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
