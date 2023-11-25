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

    def __str__(self) -> str:
        return(f'v ={self.valeur} l,h ={self.longueur,self.hauteur} x = {self.x}y ={self.y}')

def generateur(etage: int):
    tours = Piles()
    for i in range(etage, 0, -1):
        tours.empiler(Bloc(i, 20 * i, HAUTEUR_BASE, 10, 10))
    return tours


def dessine_tore(pile: Piles):
    if not pile.est_vide():
        v: Bloc = pile.depiler()
        v.dessine_Bloc(15)





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




def sd(list :list, dedut : Piles , milue : Piles , fin : Piles ):
    for asion in list :
        if asion[0] == "a" :
            if asion[1] == "b":
                milue.empiler(dedut.depiler())
            else:
                fin.empiler(dedut.depiler())
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

debut = generateur(ETAGE)
temporaire= Piles()
fin = Piles()

j =hanoi(ETAGE,"a","b","c")
lis=séparation_en_2(j)
sd(lis,debut,temporaire,fin)


class App:
    def __init__(self, etage):
        pyxel.init(LARGEUR, HAUTEUR)
        self.tour_debut= generateur(etage)
        self.tour_milue = Piles()
        self.tour_fin = Piles()
        self.x = 0
        
        pyxel.run(self.update, self.draw)

    def update(self):
        pass

    def draw(self):
        pyxel.cls(7)
        dessine_tore(self.tour_debut)
        for x_base in [X_BASE_1, X_BASE_2, X_BASE_3]:
            pyxel.rect(x_base, Y_BASE, LARGEUR_BASE, HAUTEUR_BASE, 13)


a = App(ETAGE)
