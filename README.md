# Rendu Projet GO 

**Contexte** : 
- Projet d'études Universitaire, Master 1 Informatique - Université de Bordeaux.  
 **Kirsan GEOFFROY**
 **Sebastian PAGES**
 **Groupe 1** 

##Description des points forts de votre joueur :
- **Les points fort de notre joueur** c'est la liste de coups de départs ainsi que la recherche d'arbre en Iterative Deepening (c-a-d tant qu'il reste du temps l'algorithme continue de tourner en incrémentant la valeur de la profondeur à chaque tour) qui nous permet d'explorer un maximum de noeuds. L'heuristique fonctionne bien en début de partie.
- **Technique utilisée** : Itérative Deepening AlphaBeta (Time), heuristique triviale, coups d'ouvertures prédéfinis 
- **Heuristique codée** :  Au début, nous avions optés au départ pour une heuristique triviale, elle faisait simplement la différence entre les pions blans et les pions noirs. Nous avons réfléchis par la suite pour implémenter une heuristique de manière à favoriser les clusters de pierres vivantes. Pour éviter que ces groupe de pierres perdent leur liberté, nous avons mieux évaluer les jeux où les pierres ont plus de liberté. Pour capturer des territoires nous avons utilisé la fonction de calcule de surface conquise dans l'heuristique.
- Au début nous avions choisi MiniMax comme recherche d'arbre, puis nous avons remarqué que AlphaBeta était plus efficace. Cependant AlphaBeta ne pouvait aller que jusqu'a profondeur 2 en début de partie c'est pourquoi nous avons choisis d'opter pour la technique itérative deepening pour pouvoir visiter plus de noeuds en fin de partie, car il y aura moins d'embranchements. 
- **Points faibles** : Nous n'arrivons pas à faire en sorte que notre heuristique calcule des coups intelligents, elle ne fait que placer les pions de gauche à droite et de bas en haut, même si nous augmentons la profondeur de recherche de l'abre ça ne change rien. Pourtant nous faisons en sorte de choisir aléatoirement entre les meilleurs coups possibles. Nous avons essayé d'implémenter des heuristiques plus intelligentes tel que : vérifier si la case ciblée est un oeil (c-a-d une case libre entourés de pierres) mais nous n'avons pas réussi. 
Notre joueur ne s'arrete pas de jouer meme s'il peux finir la partie et gagner. Ce qui amène à remplir le plateau et créer des situations où le plateau et surchargé et notre heuristque évalue mal ce type de plateau. Pour empecher cela nous avons privilégier les plateaux moins chargé lorsque que le nombre de pierre dépasse un certain seuil.

**Statistique W/L** : 
- Notre joueur a battu le randomPlayer 8/10, il a perdu 2/10.
- Contre le GnuGoPlayer nous ne gagnons jamais cependant nous pouvons récuperer entre 1 et 3 pierres. 