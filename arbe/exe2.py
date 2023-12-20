
from Arbres import Arbre

arbre =("*",[
    ("+",[(3,[]),(8,[])]),
    ("-",[(5,[]),(6,[])])
    ])
'("",[])'
["x",[]]
def convrticere(ardre) -> Arbre  : 

    if len(ardre) == 0:
        return Arbre()
    if ardre[1] == []:
        return Arbre(ardre[0])
    voai = []
    for enfant in ardre[1]:
        voai.append( convrticere(enfant))
    arbre = Arbre(ardre[0],voai)
    return arbre
a = convrticere(arbre)

print(a)
