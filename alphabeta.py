def evaluate(b):
    scores= {'k':200,'q':9,'r':5,'b':3,'n':3,'p':1}
    scoreTotal = 0
    coeffPionReine=1/150
    for k,p in b.piece_map().items():
        value = scores[p.symbol().lower()]

        #différenceir ami/ennemi    
        if p.symbol().lower() == p.symbol():
            value = - value
        scoreTotal +=value

        #bonifier un pion qui avance
        if p.symbol()== 'p' or  p.symbol()== 'P':
            ligne = k//8
            col = k % 8
            if p.symbol() == p.symbol().lower():
                scoreTotal -=(ligne)* coeffPionReine
            else:
                scoreTotal +=(7-ligne) * coeffPionReine
    return scoreTotal