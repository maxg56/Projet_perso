
from pilesFiles import Pile, File
 
def hauteur(arbre : list):
    """
    Renvoie la hauteur de l'arbre
    Renvoie 1 si l'arbre est une feuille
    """
    if len(arbre) == 0:
        return 0
    if len(arbre) == 1 or arbre[1] == []:
        return 1
    return 1 + max([hauteur(enfant)for enfant in arbre[1]])

def taille(arbre: list ):
    """
    Renvoie la taille de l'arbre (le nombre de noeud)
    """
    if len(arbre) == 0:
        return 0
    if len(arbre) == 1 or arbre[1] == []:
        return 1
    return 1 + sum([taille(enfant)for enfant in arbre[1]])


def parcours_largeur(arbre : list) -> None:
    """
    Renvoie la liste des valeurs des noeuds
    rencontrés lors d'un parcours en largeur
    """
    if len(arbre) == 0:
        return []
    file = File()
    file.enfiler(arbre )
    resultat = []

    while not file.est_vide():
        ardre = file.defiler()
        resultat.append(ardre[0])
        for enfants in ardre[1]:
            file.enfiler(enfants)
        return resultat

def parcours_profondeur_prefixe(arbre : tuple):
    """
    Renvoie la liste des valeurs des noeuds
    rencontrés lors d'un parcours en profondeur prefixe
    """
    if len(arbre) == 0:
        return []
    if len(arbre) == 1 or arbre[1] == []:
        return [ardre[0]]
    resultat = []
    resultat.append(ardre[0])
    for enfant in ardre[1]:
        resultat += parcours_profondeur_prefixe(enfant)
    return resultat

def parcours_profondeur_postfixe(arbre):
    """
    Renvoie la liste des valeurs des noeuds
    rencontrés lors d'un parcours en profondeur postfixe
    """
    if len(arbre) == 0:
        return []
    if len(arbre) == 1 or arbre[1] == []:
        return [ardre[0]]
    resultat = []
    
    for enfant in ardre[1]:
        resultat += parcours_profondeur_postfixe(enfant)
    resultat.append(ardre[0])
    return resultat

ardre =("*",[
    ("+",[(3,[]),(8,[])]),
    ("-",[(5,[]),(6,[])])
    ])
ardre =[5,[]]




