import Goban
import evaluateCluster
import numpy as np
########################
# Fonction evaluation (heuristique): 
########################

def evaluate(b):
    score_black = b._nbBLACK
    score_white = b._nbWHITE
    capture_white = b._capturedWHITE
    capture_black = b._capturedBLACK
    diff = (capture_white-capture_black) + (score_white - score_black)
    if b.next_player == b._BLACK:
        return diff
    return -1 * diff

# Evaluate diff 
# def evaluate(b):
#     black_stones = 0
#     white_stones = 0
#     for r in range(1, b._BOARDSIZE + 1):
#         for c in range(1, b._BOARDSIZE + 1):
#             p = b._BOARDSIZE * r+c
#             color = b.get()
#             if color == b._BLACK:
#                 black_stones += 1
#             elif color == b._WHITE:
#                 white_stones += 1
#     diff = black_stones - white_stones
#     if b.next_player == b._BLACK:
#         return diff
#     return -1 * diff

# Evaluate Cluster 
# def evaluate(b):
#     b._neighbors = []
#     b._neighborsEntries = []
#     for nl in [b._get_neighbors(fcoord) for fcoord in range(b._BOARDSIZE**2)] :
#         b._neighborsEntries.append(len(b._neighbors))
#         for n in nl:
#             b._neighbors.append(n)
#             print(b._neighbors)
#         b._neighbors.append(-1) # Sentinelle
#     b._neighborsEntries = np.array(b._neighborsEntries, dtype='int16')
#     b._neighbors = np.array(b._neighbors, dtype='int8')
#     print(b._neighborsEntries)
#     return b._neighbors

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