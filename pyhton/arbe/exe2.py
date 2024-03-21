
from Arbres import Arbre

arbre =("*",[
    ("+",[(3,[]),(8,[])]),
    ("-",[(5,[]),(6,[])])
    ])
'("",[])'
arbre3 = ["x",[["x",[["x",[]]]],["x",[]]]]
["x",[]]
def convertisseur(arbre1) -> Arbre  : 
    """ il convertit un arbre sous la forme ("",[]) en un ogest de la classe Arbre """
    if len(arbre1) == 0:
        return Arbre()
    if arbre1[1] == []:
        return Arbre(arbre1[0])
    voai = []
    for enfant in arbre1[1]:
        voai.append( convertisseur(enfant))
    arbre = Arbre(arbre1[0],voai)
    return arbre

a = convertisseur(arbre)
d = convertisseur(arbre3)



print(d)
print(a)
