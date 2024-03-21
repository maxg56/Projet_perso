import pyxel
from random import randint
from Piles import Piles

LARGEUR, HAUTEUR = 160, 120
LARGEUR_BASE, HAUTEUR_BASE = LARGEUR // 6, 5
X_BASE_1, Y_BASE = 20, HAUTEUR - 10
X_BASE_2 = X_BASE_1 + LARGEUR_BASE * 2
X_BASE_3 = X_BASE_2 + LARGEUR_BASE * 2
LST_COULEURS = [1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 14, 15]
ETAGE = 4


class Bloc:
    def __init__(self, valeur, longueur, hauteur, x, y) -> None:
        self.valeur = valeur
        self.longueur = longueur
        self.hauteur = hauteur
        self.x, self.y = x, y

    def dessine_Bloc(self, couleur):
        pyxel.rect(self.x, self.y, self.longueur, self.hauteur, couleur)
        pyxel.text(self.x,self.y,str(self.valeur),7)

    def Déplace(self, x,y):
        self.x = x 
        self.y = y 
        
    def __str__(self) -> str:
        return(f'v ={self.valeur} l,h ={self.longueur,self.hauteur} x = {self.x}y ={self.y}')

def generateur(etage: int):
    tours = Piles()
    y = Y_BASE
    for i in range(etage, 0, -1):
        x = X_BASE_1 +2
        y -= HAUTEUR_BASE
        tours.empiler(Bloc(i, 20 * i, HAUTEUR_BASE, x, y))
    return tours


def dessine_tore(pile: Piles):
    
    for i in range(5):
       if not pile.est_vide() :
            valeur_sommet : Bloc = pile.depiler()
            valeur_sommet.dessine_Bloc(7)
        
        # Autres opérations avec la valeur du sommet sans dépiler l'élément








def hanoi(taille, debut : Piles, temporaire:Piles, fin : Piles):
    if taille == 1:
        return   debut + fin
    else:
        return (
            hanoi(taille - 1, debut, fin, temporaire)
            + debut
            + fin
            + hanoi(taille - 1, temporaire, debut, fin)
        )

def séparation_en_2(lst):
    h = []
    val2 = []

    for val in lst:
        val2.append(val)

        if len(val2) == 2:
            h.append(tuple(val2))
            val2 = []

    if val2:
        h.append(tuple(val2))

    return h




def sd(list :list, debut : Piles , milue : Piles , fin : Piles ):
    for asion in list :
        if asion[0] == "a" :
            if asion[1] == "b":
                milue.empiler(debut.depiler())
            else:
                fin.empiler(debut.depiler())
        elif asion[0] == "b" :
            if asion[1] == "a":
                debut.empiler(milue.depiler())
            else:
                fin.empiler(milue.depiler())
        else:
            if asion[1] == "a":
                debut.empiler(fin.depiler())
            else:
                milue.empiler(fin.depiler())

"""debut = generateur(ETAGE)
temporaire= Piles()
fin = Piles()

j =hanoi(ETAGE,"a","b","c")
lis=séparation_en_2(j)
sd(lis,debut,temporaire,fin)"""

import pyxel


class TourDeHanoi:
    def __init__(self,  etage):
        # Initialisation de Pyxel avec une résolution de 160x120 pixels et une fréquence d'images de 30 par seconde
        pyxel.init(160, 120, fps= 1)
        # Initialisation des attributs pour la deuxième partie du code
        self.etage = etage
        self.tour_debut = generateur(etage)
        self.tour_milue = Piles()
        self.tour_fin = Piles()
        self.x = 0
        self.frame_count = 0
        print(self.tour_debut)
        # Exécution de la boucle principale du jeu avec les fonctions update et draw
        pyxel.run(self.update, self.draw)

    def update(self):
        # Incrémentation du compteur de frames
        #self.frame_count = (self.frame_count + 1) % 60
        pass
        # Ajoutez ici toute logique de mise à jour supplémentaire pour le jeu

    def draw(self):
        # Effacement de l'écran
        pyxel.cls(0)
        
        # Appel de la fonction pour dessiner la tour de Hanoï
        

        # Dessin des éléments de la deuxième partie du code
        n =dessine_tore(self.tour_debut)

        for x_base in [X_BASE_1, X_BASE_2, X_BASE_3]:
            pyxel.rect(x_base, Y_BASE, LARGEUR_BASE, HAUTEUR_BASE, 13)

    def drawHanoi(self):
        pass 

# Assurez-vous d'importer correctement les autres fonctions et classes utilisées dans votre code initial.


a = TourDeHanoi(ETAGE)
