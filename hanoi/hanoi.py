import pyxel
from random import random
class Element:
    """_summary_"""

    def __init__(self, valeur):
        self.valeur = valeur
        self.successeur = None

    def renvoie_valeur(self):
        return self.valeur

    def renvoie_successeur(self):
        return self.successeur

    def modifie_valeur(self, valeur):
        self.valeur = valeur

    def modifie_successeur(self, successeur):
        self.successeur = successeur

    def __str__(self):
        return f" {self.valeur} -> {self.successeur } "
class Piles:
    def __init__(self):
        self.tette = None

    def est_vide(self):
        return self.tette is None

    def empiler(self, x):
        nouvel_element = Element(x)
        if not self.est_vide():
            nouvel_element.successeur = self.tette

        self.tette = nouvel_element

    def depiler(self):
        if self.est_vide():
            raise ValueError("LA pile set vide")

        v = self.tette.valeur
        self.tette = self.tette.successeur

        return v
    
    def __str__(self) -> str:
        if self.est_vide():
            return "la pile est vide"
        else :
            return f"Hout || {self.tette} || Bas".format()


LARGEUR ,HAUTEUR = 160 ,120
LARGEUR_BASE ,HAUTEUR_BASE = LARGEUR//6,5
X_BASE_1 , Y_BASE = 20,HAUTEUR-10
X_BASE_2 = X_BASE_1 + LARGEUR_BASE*2
X_BASE_3 = X_BASE_2 + LARGEUR_BASE*2
LST_COULER =[1,2,3,4,5,6,8,9,10,11,12,14,15]
def generateur(etage : int ) :
    """Sert à générer les piles de la bonne taille pour les Tour de ahanoi"""
    tours = Piles()
    for i in range(etage,0,-1):
        tours.empiler(i)
    return tours
def dessine_tore(pimes : Piles,x_base ,y_base ):
    """Sert à dessiner les piles"""
    if not pimes.empiler():
        v = pimes.depiler()
        y_base += HAUTEUR_BASE
        largeu -= 4
        pyxel.rect(x_base, y_base, largeu, HAUTEUR_BASE, LST_COULER[random(len(LST_COULER))])
        pyxel.text(x_base, y_base,str(v),7)
        
        
def hanoi(taille, debut, tenporaire, fin):
    if taille == 1:
        return debut + fin
    else:
        return (
            hanoi(taille - 1, debut, fin, tenporaire)
            + debut
            + fin
            + hanoi(taille - 1, tenporaire, debut, fin))



class App:
    def __init__(self):
        pyxel.init(LARGEUR, HAUTEUR)
        self.x = 0
        pyxel.run(self.update, self.draw)
        
        

    def update(self):
        pyxel.image(0).set(10, 10, ["0123", "4567", "89ab", "cdef"])
        self.x = (self.x + 1) % pyxel.width

    def draw(self):
        pyxel.cls(7)
        for x_base in [X_BASE_1, X_BASE_2, X_BASE_3]:
            pyxel.rect(x_base, Y_BASE, LARGEUR_BASE, HAUTEUR_BASE, 13)
        
        
App()