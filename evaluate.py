import Goban
import numpy as np
from random import choice
########################
# Fonction evaluation (heuristique): 
########################

#Trivial heuristic -> difference between the number of stones for each one
# def evaluate(b):
#     score_black = b._nbBLACK
#     score_white = b._nbWHITE
#     capture_white = b._capturedWHITE
#     capture_black = b._capturedBLACK
#     diff = (capture_white-capture_black) + (score_white - score_black)
#     return diff

# def is_eyeish(b, c):
#     """ test if c is inside a single-color diamond and return the diamond
#     color or None; this could be an eye, but also a false one """
#     eyecolor = None
#     for d in b._get_neighbors(b):
#         if board[d].isspace():
#             continue
#         if board[d] == '.':
#             return None
#         if eyecolor is None:
#             eyecolor = board[d]
#             othercolor = eyecolor.swapcase()
#         elif board[d] == othercolor:
#             return None
#     return eyecolor

# def is_eye(b, color):
#     """ test if c is an eye and return its color or None """
#     eyecolor = is_eyeish(b, b._BLACK)
#     if eyecolor is None:
#         return None

#     # Eye-like shape, but it could be a falsified eye
#     falsecolor = eyecolor.swapcase()
#     false_count = 0
#     at_edge = False
#     for d in diag_neighbors(c):
#         if b[d].isspace():
#             at_edge = True
#         elif b[d] == falsecolor:
#             false_count += 1
#     if at_edge:
#         false_count += 1
#     if false_count >= 2:
#         return None

#     return eyecolor

#Evaluate Cluster -> Prioritize a move if it increase a cluster
def evaluate(b):
    b._neighbors = []
    b._neighborsEntries = []
    for nl in [b._get_neighbors(fcoord) for fcoord in range(b._BOARDSIZE**2)] :
        b._neighborsEntries.append(len(b._neighbors))
        for n in nl:
            b._neighbors.append(n)
        b._neighbors.append(-1) # Sentinelle
    b._neighborsEntries = np.array(b._neighborsEntries, dtype='int16')
    b._neighbors = np.array(b._neighbors, dtype='int8')
    #return b._neighbors[0]
    return choice(b._neighbors)

# def evaluate(b):
#     print('eval')
#     color=b._BLACK
#     a=1
#     c=1
#     score = 0 
#     for stringNumber in b._stringUnionFind:
#         stringSizes=b._stringSizes[stringNumber]
#         stringLiberties=b._stringLiberties[stringNumber]
#         if b[stringNumber] == color:     #b.__getitem__(b,stringNumber) == color:     
#             score+= a * stringSizes**2 + c * stringLiberties
#         else :   
#             score-= a * stringSizes**2 + c * stringLiberties