
from Arbres import Arbre

arbre =("*",[
    ("+",[(3,[]),(8,[])]),
    ("-",[(5,[]),(6,[])])
    ])
'("",[])'
["x",[]]
def convrticere(ardre) -> Arbre  : 

    if len(arbre) == 0:
        return Arbre()
    if arbre[1] == []:
        return Arbre(arbre[0])
    voai = []
    for enfant in ardre[1]:
        voai.append( convrticere(enfant))
    arbre = Arbre(arbre[0],voai)
    return arbre
a = convrticere(arbre)

a.dessiner()
