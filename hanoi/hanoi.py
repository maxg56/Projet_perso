import pyxel
from random import randint
from Piles import Piles

LARGEUR ,HAUTEUR = 160 ,120
LARGEUR_BASE ,HAUTEUR_BASE = LARGEUR//6,5
X_BASE_1 , Y_BASE = 20,HAUTEUR-10
X_BASE_2 = X_BASE_1 + LARGEUR_BASE*2
X_BASE_3 = X_BASE_2 + LARGEUR_BASE*2
LST_COULEURS =[1,2,3,4,5,6,8,9,10,11,12,14,15]
ETAGE  = 4

class Bloc:
    def __init__(self,vale,longueur, hauteur,x,y) -> None:
        self.vale =vale
        self.longuer = longueur
        self.hauteur = hauteur
        self.x,self.affiche_yy =x,y
    
    def affiche_vale(self):
        return self.vale
    
    def affiche_longuer(self):
        return self.longuer
    
    def affiche_hauteuer(self):
        return self.hauteur
    
    def affiche_x(self):
        return self.x
    
    def affiche_y(self):
        return self.y 
    
    def dessine_Bloc(self,coleur):
        
        pyxel.rect(self.x, self.y, self.largeu, self.hauteur, coleur)
        

def generateur(etage : int ) :
    """Sert à générer les piles de la bonne taille pour les Tour de ahanoi"""
    tours = Piles()
    for i in range(etage,0,-1):
        print(i)
        tours.empiler(Bloc(i,20*i,HAUTEUR_BASE,10,10))
    return tours

def dessine_tore(pile:Piles):
    if not pile.est_vide():
        v : Bloc = pile.depiler
        v.dessine_Bloc(6)
        
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
    def __init__(self,etage):
        pyxel.init(LARGEUR, HAUTEUR)
        self.tour = generateur(etage)
        self.x = 0
        pyxel.run(self.update, self.draw)
        
        

    def update(self):
        pass

    def draw(self):
        couleur = LST_COULEURS[randint(0, len(LST_COULEURS) - 1)]
        pyxel.cls(7)
        dessine_tore(self.tour)
        for x_base in [X_BASE_1, X_BASE_2, X_BASE_3]:
            pyxel.rect(x_base, Y_BASE, LARGEUR_BASE, HAUTEUR_BASE, 13)
        
       
a=App(ETAGE)
