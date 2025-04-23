#
# MIDN Colton Mantha
# 263948
# 2-17-25
# Project 1 (15-Puzzle): main driver Class 
#

from astar import *
from Board import *
from PriQue import *
import copy
import pdb

if __name__ == "__main__":
    n = int(input("Enter scramble size: ")) 
    b1 = Board()
    b1.scramble(n)
    b2 = Board()
    p , n1  = aStar(b1, misplacedTiles) # p = path to solve it (list), n1 = # of boards to take (int)
    print(len(p))
#    print(n1)
    applyMoves(b1,p)
    print(b1==b2)
    b1 = Board()
    b1.scramble(n)
    p , n2  = aStar(b1, manhattanDistance)
    print(len(p))
#    print(n2)
    applyMoves(b1,p)
    print(b1==b2)
    print(n1>=n2)
