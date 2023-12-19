from pilesFiles import Pile, File
from Arbres import Arbre

arbre =("*",[
    ("+",[(3,[]),(8,[])]),
    ("-",[(5,[]),(6,[])])
    ])
'("",[])'
["x",[]]
def convrticere(forme,ardre)  : 
    Valeur ,enfant = arbre

    if len(arbre) == 0:
        return Arbre()
    if arbre[1] == []:
        return Arbre(arbre[0])
    voai = []
    for enfant in ardre[1]:
        voai.append( convrticere(enfant))
    arbre = Arbre(arbre[0],voai)
    return arbre

def parcourir_arbre(arbre):
   Valeur ,enfant = arbre

    print(symbole)  # Fais quelque chose avec le symbole, par exemple l'afficher

    for sous_arbre in sous_arbres:
        parcourir_arbre(sous_arbre)

parcourir_arbre(arbre)