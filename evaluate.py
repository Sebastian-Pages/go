import Goban
import evaluateCluster
########################
# Fonction evaluation (heuristique): 
########################
def evaluate(self):
    print("Voissins: ",self._neighborsEntries)
    score_black = self._nbBLACK
    score_white = self._nbWHITE
    scoreTotal = score_white - score_black
    return scoreTotal

def evaluate(b):
    print('eval')
    color=b._BLACK
    a=1
    c=1
    score = 0 
    for stringNumber in b._stringUnionFind:
        stringSizes=b._stringSizes[stringNumber]
        stringLiberties=b._stringLiberties[stringNumber]
        if b[stringNumber] == color:     #b.__getitem__(b,stringNumber) == color:     
            score+= a * stringSizes**2 + c * stringLiberties
        else :   
            score-= a * stringSizes**2 + c * stringLiberties