import time
import Goban 
from evaluate import *
from random import choice

# Global variable
nbnodes = 0
# Opening moves from https://senseis.xmp.net/?9x9Openings
bestMoves= [42,50,51,60,39,40]

########################
# Function for the first 6 moves: 
########################
def getBestMove(b) :
    coup = bestMoves.pop()
    if coup in b.weak_legal_moves() :
        return coup
    else :
        return -1

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
    for m in b.weak_legal_moves():
        b.push(choice(b.weak_legal_moves()))
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
    for m in b.weak_legal_moves():
        c = choice(b.weak_legal_moves())
        while c=="PASS" :
            c = choice(b.weak_legal_moves())
        b.push(c)
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
    for m in b.weak_legal_moves():
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

########################
# Iterative Deepening Alpha Beta : 
########################
def IDAlphaBeta(b, depth=3):
    if len(bestMoves)>0 :
        coup = getBestMove(b)
        return coup
    else : 
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