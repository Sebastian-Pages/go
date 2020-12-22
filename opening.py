import Goban

bestMoves= [(5,5)]

def Opening(b, count,limiteCPU=None):
    coup = getBestMove(b)
    return coup

def getBestMove(b) :
    for i in bestMoves:
        if i in b.generate_legal_moves() :
            bestMoves.pop()
            return i
        else :
            return (-1,-1)
       