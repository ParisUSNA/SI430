#
# MIDN Colton Mantha
# 263948
# 2-17-25
# Project 1 (15-Puzzle): astar Class 
#

from Board import *
from PriQue import *
import copy

# aStar function which takes in board b and heuristic h
def aStar(board,heuristic):

  state = State(board,list(),fcost(board,heuristic),0) # start state
  goalBoard = Board() # goal board state
  open = PriQue() # priority queue of states discovered
  closed = [] # list of states visited

  # runs until the state of current board is same as goal board
  while state.get_board().__ne__(goalBoard):
    # generate successors
    neighbors = get_neighbors(state,heuristic)

    # check if state in closed
    #if stateClosed(state,closed) == False:
    if state.get_board() not in closed:

      # add state to closed
      closed.append(state.get_board())

      # add successors to open priority queue
      for i in range(0,len(neighbors)):
        open.push(neighbors[i])

    # new lowest cost state assigned to state
    state = open.pop()
  return state.get_path(), state.get_gcost()
      
# gets the neighboring states of a current state
# takes in current state and heuristic
def get_neighbors(curr, hr):

  # neighbors list of states and possible moves generated
  neighbors = []
  moves = curr.get_board().generateMoves()

  # creates new state each time and adds to neighbors
  for i in range(0,len(moves)):
    temp = copy.deepcopy(curr)
    temp.get_board().makeMove(moves[i])
    temp.get_path().append(moves[i])
    temp.set_gcost(temp.gcost+1)
    temp.set_cost(fcost(temp.get_board(),hr) + temp.gcost)
    neighbors.append(temp)
  return neighbors

# returns fcost based on heuristic function
def fcost(board, hr):
  if hr == manhattanDistance:
    return manhattanDistance(board.get_board())
  elif hr == misplacedTiles:
    return misplacedTiles(board.get_board())

# returns if a state has been closed
def stateClosed(state, closed):
  for i in range(0,len(closed)):
    if state.get_board() == closed[i]:
      return True
  return False

