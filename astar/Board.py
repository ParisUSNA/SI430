#
# MIDN Colton Mantha
# 263948
# 2-17-25
# Project 1 (15-Puzzle): Board Class 
#

import random

class Board(object):
  # A board is just a 2-d list, plus a location of the blank, fo easier move generation.
  def __init__(self):
    self.b = [['b', 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]]
    self.lb = [0, 0]
    
  # Returns a list of places the blank can be moved to.  Note the use of map and filter.  Good tools for AI
  # programming
  def generateMoves(self):
    delta = [[-1,0],[1,0],[0,-1],[0,1]]
    result = list(map(lambda x: pairAdd(x,self.lb), delta)) 
    result = list(filter(lambda x: inRange(x), result))
    return result

  # Takes a move location, and actually changes the board.
  def makeMove(self,m):
    # It had better be next to the current location.
    if (manhattan(m,self.lb) > 1):
        raise RuntimeError('Bad move executed on board: ' + str(m) + 'lb: ' + str(self.lb))
    self.b[self.lb[0]][self.lb[1]] = self.b[m[0]][m[1]]
    self.b[m[0]][m[1]] = 'b'
    self.lb = m

  # Mix up the board. 
  def scramble(self,n,s=2018):
    random.seed(s)
    for i in range(n):
      moves = self.generateMoves()
      self.makeMove(moves[random.randint(0,len(moves)-1)])

  # are boards equal?
  def __eq__(self,other):
    return self.b == other.b
  def __ne__(self,other):
    return self.b != other.b
  def key(self):
    return str(self.b)
  
  # get methods
  def get_board(self):
    return self.b
  def get_blank(self):
    return self.lb
#---------------------------------
# End of Board class

# apply a list of moves to the board.
def applyMoves(board,moveList):
  for m in moveList:
    board.makeMove(m)

# Some utility functions 
def pairAdd(a,b):
  return [a[0]+b[0],a[1]+b[1]]

def inRange(p):
  return p[0] >= 0 and p[0] < 4 and p[1] >=0 and p[1] < 4

# The heuristics go here

# manhattan distance heuristic
# takes in a board state s
# returns the f cost based on the manhattan distance heuristic
def manhattanDistance(s):
  cost = 0
  for i in range(0,16):
    tile = s[int(i)//4][int(i)%4]
    if i == 0:
      x,y = findNum(s,'b')
      cost += manhattan([0,0],[x,y])
    else:
      x,y = findNum(s,i)
      cost += manhattan([int(i)//4,int(i)%4],[x,y])
  return cost

# finds num in board state
def findNum(s, n):
  for i in range(0, 16):
    x = s[int(i)//4][int(i)%4]
    if (n == 'b' and x == 'b') or (x != 'b' and int(x) == n):
      return (int(i)//4), (int(i)%4)
  return -1,-1
    
# This is not the actual manhattan distance heuristic, but may
# be helpful
def manhattan(a,b):
  # takes two locations on the board and returns the difference
  return abs(a[0]-b[0])+abs(a[1]-b[1])

# misplacedTiles heuristic returns the number of tiles not in their goal
# position give a board state s
def misplacedTiles(s):
  sum = 0
  for i in range(0,16):
    if i == 0:
      if s[0][0] != 'b':
        sum += 1
    elif s[int(i)//4][int(i)%4] != i:
      sum += 1
  return sum