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


def generateur(etage: int):
    tours = Piles()
    for i in range(etage, 0, -1):
        tours.empiler(Bloc(i, 20 * i, HAUTEUR_BASE, 10, 10))
    return tours


def dessine_tore(pile: Piles):
    if not pile.est_vide():
        v: Bloc = pile.depiler()
        v.dessine_Bloc(15)


def hanoi(taille, debut, temporaire, fin):
    if taille == 1:
        return debut + fin
    else:
        return (
            hanoi(taille - 1, debut, fin, temporaire)
            + debut
            + fin
            + hanoi(taille - 1, temporaire, debut, fin)
        )


class App:
    def __init__(self, etage):
        pyxel.init(LARGEUR, HAUTEUR)
        self.tour = generateur(etage)
        self.x = 0
        pyxel.run(self.update, self.draw)

    def update(self):
        pass

    def draw(self):
        pyxel.cls(7)
        dessine_tore(self.tour)
        for x_base in [X_BASE_1, X_BASE_2, X_BASE_3]:
            pyxel.rect(x_base, Y_BASE, LARGEUR_BASE, HAUTEUR_BASE, 13)


a = App(ETAGE)
