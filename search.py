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

  initFrontier = util.Stack()
  explored = []
  initState = problem.startingState()
  initFrontier.push(initState)
  explored.append(initState)
  returnList = recDfs(problem, initFrontier, initState, explored)
  print 'return list ', returnList

  #util.raiseNotDefined()

  return returnList

def recDfs(problem, frontier, state, explored):
  # recursive part of the DFS algorithm
  x = None

  if problem.isGoal(state):
    print 'stack at sol: ', frontier.list
    return solution(frontier)
  
  
  print 'state in rec is: ', state
  successorList = problem.successorStates(state)

  for child in successorList:
    if child[0] not in explored:
      frontier.push(child)
      explored.append(child[0])
      x = recDfs(problem, frontier, child[0], explored)
    
  if x is None:
    print 'here'
    n = frontier.pop()
    print 'poppiing node: ', n[0]
    return  
  else:
    return x 


  # if len(successorList) == 0 or allSuccessorsExplored(successorList, explored):
  #   print 'here'
  #   n = frontier.pop()
  #   print 'poppiing node: ', n[0]
  #   return 


# def recDfs(problem, frontier, state, explored):
#   # recursive part of the DFS algorithm
  
  
#   print 'state in rec is: ', state
#   successorList = problem.successorStates(state)
#   if len(successorList) == 0 or allSuccessorsExplored(successorList, explored):
#     print 'here'
#     n = frontier.pop()

#   for child in successorList:
#     if child[0] not in explored:
#       frontier.push(child)
#       explored.append(child[0])
#       if problem.isGoal(child[0]):
#         print 'stack at solution time is: ', frontier.list
#         return solution(frontier) 
#       recDfs(problem, frontier, child[0], explored)



def allSuccessorsExplored(successors, explored):

  for s in successors:
    if s[0] not in explored:
      return False

  return True

def solution(frontier):

  from game import Directions
  s = Directions.SOUTH
  w = Directions.WEST
  e = Directions.EAST
  n = Directions.NORTH

  sol = []
  for item in frontier.list:
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
