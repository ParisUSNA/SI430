#
# MIDN Colton Mantha
# 263948
# 2-17-25
# Project 1 (15-Puzzle): Priority Queue Class 
#

from Board import *
import heapq
from dataclasses import dataclass

# State class
class State:
  def __init__(self,board,path,cost,gcost):
    self.board = board #current board
    self.path = path # list of moves to get to this path
    self.cost = cost # total cost of path
    self.gcost = gcost # total number of moves

  # get methods
  def get_path(self):
    return self.path
  def get_cost(self):
    return self.cost
  def get_gcost(self):
    return self.gcost
  def get_board(self):
    return self.board
  
  # set methods
  def set_path(self, path):
    self.path = path
  def set_cost(self, cost):
    self.cost = cost
  def set_gcost(self, gcost):
    self.gcost = gcost

  # equivelance of 2 states method
  def __eq__(self,state):
    return self.board.__eq__(state.get_board())
  # non equivelance of 2 states method
  def __ne__(self,state):
    return self.board.__ne__(state.get_board())
  
  # overwrites __lt__ method
  def __lt__(self, other):
    return self.get_cost() < other.get_cost()

  # to string method
  def toString(self):
    print(f'Board = {self.board.key()}\nPath = {self.path}\nCost = {self.cost}\nGCost = {self.gcost}')

# Priority Queue class based on minheap
class PriQue(object):

  # pushes a state onto open
  def __init__(self):
    self.open = [] # min-heap list

  # pushes a state onto open
  def push(self, state):
    heapq.heappush(self.open, state)

  # pops the minimum cost state off of open
  def pop(self):
    return heapq.heappop(self.open)
  


  



