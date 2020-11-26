import time
import Goban 

# Global variable
nbnodes = 0

########################
# Fonction evaluation (heuristique): 
########################
def evaluate(b):
    score_black = b._nbBLACK
    score_white = b._nbWHITE
    scoreTotal = score_white - score_black
    return scoreTotal

########################
# IA MiniMax  
########################
def MaxMin(b, depth=3):
    global nbnodes
    #nbnoeuds+=1
    if b.is_game_over():
        res = b.result()
        if res == '1-0':
            return 400
        elif res == '0-1':
            return -400
        else:
            return 0
    if depth == 0:
        return evaluate(b)
    v = None
    for m in b.generate_legal_moves():
        b.push(m)
        retour = MinMax(b,depth-1)
        if v is None or v < retour:
            v = retour
        b.pop()
    return v 

def MinMax(b, depth=3):
    global nbnodes
    nbnodes+=1
    if b.is_game_over():
        res = b.result()
        if res == '1-0':
            return 400
        elif res == '0-1':
            return -400
        else:
            return 0
    if depth == 0:
        return evaluate(b)
    v = None
    for m in b.generate_legal_moves():
        b.push(m)
        retour = MaxMin(b,depth-1)
        if v is None or v > retour:
            v = retour
        b.pop()
    return v 

def IAMiniMax(b, depth=3):
    global nbnodes
    nbnodes += 1
    coup = None 
    best = -800 # -800 = -infini
    for m in b.generate_legal_moves():
        b.push(m)
        v = MinMax(b, depth -1)
        if v > best or coup == None : 
            best = v  
            coup = m 
        b.pop()
    return coup        

########################
# IA Alpha Beta : 
########################
def MaxValue(b, alpha, beta, depth=3, limiteCPU=None):
    global nbnodes
    nbnodes += 1
    if limiteCPU is not None and time.time()>limiteCPU :
        raise TimeoutError
    if b.is_game_over():
        res = b.result 
        if res == '1-0':
            return 400
        elif res == '0-1':
            return -400
        else :
            return 0
    if depth == 0 :
        return evaluate(b)
    for m in b.generate_legal_moves():
        b.push(m)
        try : 
            v = MinValue(b, alpha, beta, depth-1)
        except TimeoutError :
            b.pop()
            raise TimeoutError
        b.pop()
        if v > alpha : 
            alpha = v
        if alpha >= beta : 
            return beta 
    return alpha

def MinValue(b, alpha, beta, depth=3, limiteCPU=None):
    global nbnodes
    nbnodes += 1
    if limiteCPU is not None and time.time()>limiteCPU :
        raise TimeoutError
    if b.is_game_over():
        res = b.result 
        if res == '1-0':
            return 400
        elif res == '0-1':
            return -400
        else :
            return 0
    if depth == 0 :
        return evaluate(b)
    for m in b.generate_legal_moves():
        b.push(m)
        try : 
            v = MaxValue(b, alpha, beta, depth-1, limiteCPU)
        except TimeoutError :
            b.pop()
            raise TimeoutError
        b.pop()
        if v < beta : 
            beta = v
        if alpha >= beta : 
            return alpha 
    return beta

# On considère -infini = -800 et +infini = 800
def IAAlphaBeta(b, depth=3, limiteCPU=None):
    alpha = -800 
    beta = 800
    coup = None 
    for m in b.generate_legal_moves():
        b.push(m)
        try :   
            v = MinValue(b, alpha, beta, depth-1, limiteCPU)
        except TimeoutError :
            b.pop()
            raise TimeoutError
        if v > alpha :#or coup == None : 
            alpha = v 
            coup = m 
        b.pop()
    return coup 
    
def IDAlphaBeta(b, depth=3):
    maxCPU = time.time() + depth
    thisDepth = 1 
    res = None 
    t = 0 
    while True : 
        try :
            t = time.time()
            res = IAAlphaBeta(b, depth=thisDepth, limiteCPU = maxCPU)
            t = time.time()
        except TimeoutError : 
            return res 
        thisDepth += 1

board = Goban.Board()

#Match IAMiniMax vs IAAlphaBeta
depth = 3 
while not board.is_game_over():
    t = time.time()
    nb = nbnodes 
    coup = IAAlphaBeta(board, depth)
    print('Comparaison : alpha-beta profondeur 3 : ', nbnodes - nb, 'noeuds en ', time.time()-t, ' secondes') 
    board.push(coup) 
    if board.is_game_over():
        break
    t = time.time()
    nb = nbnodes 
    coup = IAMiniMax(board, depth)
    print('Comparaison : Mini - Max profondeur 3 : ', nbnodes - nb, 'noeuds en ', time.time()-t, ' secondes') 
    board.push(coup) 
    print(board)
print('Resultat : ', board.result())
    