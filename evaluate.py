import Goban
########################
# Fonction evaluation (heuristique): 
########################
def evaluate(b):
    score_black = b._nbBLACK
    score_white = b._nbWHITE
    scoreTotal = score_white - score_black
    return scoreTotal
