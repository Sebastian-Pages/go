import Goban
from evaluate import *

# Global variable
nbnodes = 0

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