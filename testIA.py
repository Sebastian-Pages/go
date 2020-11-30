import Goban
import time
from minimax import *
from alphabeta import *

# Global variable
nbnodes = 0

board = Goban.Board()

#Match IAMiniMax vs IAAlphaBeta
depth = 2 
while not board.is_game_over():
    t = time.time()
    nb = nbnodes 
    coup = IAAlphaBeta(board, depth)
    print('Comparaison : alpha-beta profondeur ', depth, ': ', nbnodes - nb, 'noeuds en ', time.time()-t, ' secondes') 
    board.push(coup) 
    if board.is_game_over():
        break
    t = time.time()
    nb = nbnodes 
    coup = IAMiniMax(board, depth)
    print('Comparaison : Mini - Max profondeur: ', depth, ': ', nbnodes - nb, 'noeuds en ', time.time()-t, ' secondes') 
    board.push(coup) 
    print(board)
print('Resultat : ', board.result())