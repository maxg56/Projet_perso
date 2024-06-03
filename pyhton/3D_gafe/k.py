import pyxel 
from random import randint, randrange
from collections import deque


LARGEUR = 15
LIGNES_VIDES = 3
HAUTEUR = 15
TAILLE_CASE = 16
NOIR = 0
COULERE_DU_FON = 6
GRIS =13
COULEUR_SERPENT = 8 
FPS =10
DELAI_DEPLACEMENT = FPS // 8
CASES_DEP = [(3, 8), (4, 8), (5, 8)]
HAUT = (0, -1)
BAS = (0, 1)
GAUCHE = (-1, 0)
DROITE = (1, 0)
CASE_POMME = (13, 8)

class Serpent:
    def __init__(self):
        self.couleur = COULEUR_SERPENT
        self.cases  = deque()
        for (x,y) in CASES_DEP:
            self.cases.append((x,y))
        self.orientation = DROITE
            
    def avance(self):
        x, y = self.cases[-1]
        self.cases.popleft()
        x, y = (x + self.orientation[0], y + self.orientation[1])
        if x >= LARGEUR:
            x = 0
        if x < 0:
            x = LARGEUR - 1
        if y >= HAUTEUR:
            y = 0
        if y < 0:
            y = HAUTEUR - 1
        self.cases.append((x, y))

    def dessine(self):
        for x, y in self.cases:
            pyxel.rect(
                x * TAILLE_CASE,
                y * TAILLE_CASE,
                TAILLE_CASE,
                TAILLE_CASE,
                self.couleur,
            )
    

class Pomme:
    def __init__(self) -> None:
        self.depart = CASE_POMME
        self.cases = (randint(0,LARGEUR), randint(0,HAUTEUR))
        
    def dessine(self):
        pyxel.rect(self.cases[0]*TAILLE_CASE, self.cases[1]*TAILLE_CASE, TAILLE_CASE ,TAILLE_CASE , 8)

class Jeu :
    def __init__(self) -> None:
        self.serpent = Serpent()
        self.pomme = Pomme()
        self.timer_deplacement = DELAI_DEPLACEMENT
        pyxel.init(LARGEUR*TAILLE_CASE ,HAUTEUR*TAILLE_CASE, fps =FPS)
        pyxel.mouse(True)
        pyxel.run(self.mise_a_jour,self.dessine)
    
    def mise_a_jour(self) :
        if pyxel.btn(pyxel.KEY_UP)and self.serpent.orientation != BAS:
            self.serpent.orientation = HAUT
        elif pyxel.btn(pyxel.KEY_DOWN)and self.serpent.orientation != HAUT:
            self.serpent.orientation = BAS
        elif pyxel.btn(pyxel.KEY_LEFT)and self.serpent.orientation != DROITE:
            self.serpent.orientation = GAUCHE
        elif pyxel.btn(pyxel.KEY_RIGHT and self.serpent.orientation != GAUCHE):
            self.serpent.orientation = DROITE
        
        """
        while self.serpent.cases[-1] != self.pomme.cases:
            self.serpent.cases.popleft()"""

        self.serpent.avance()

    def dessine(self):
        pyxel.cls(COULERE_DU_FON)
        
        for x in range( LARGEUR):
            pyxel.line(x * TAILLE_CASE,
                       0,
                        x * TAILLE_CASE,
                        HAUTEUR * TAILLE_CASE,
                        GRIS
                          )
            for y in range(0, HAUTEUR):
                if (x + y) % 2 == 0:
                    pyxel.rect(x * TAILLE_CASE, y * TAILLE_CASE, TAILLE_CASE, TAILLE_CASE, 11)
                else:
                    pyxel.rect(x * TAILLE_CASE, y * TAILLE_CASE, TAILLE_CASE, TAILLE_CASE, 6)

       

        for y in range(HAUTEUR):
            pyxel.line(0,
                       y * TAILLE_CASE,
                        LARGEUR * TAILLE_CASE,
                        y * TAILLE_CASE,
                        GRIS
                          )
            

        self.pomme.dessine()
        self.serpent.dessine()
class Bouton:
    def __init__(self, x, y, largeur, hauteur, texte):
        self.x = x
        self.y = y
        self.largeur = largeur
        self.hauteur = hauteur
        self.texte = texte
        self.couleur_fond = 7
        self.couleur_texte = 0

    def dessiner(self):
        pyxel.rect(self.x, self.y, self.largeur, self.hauteur, self.couleur_fond)
        pyxel.text(self.x + 5, self.y + 5, self.texte, self.couleur_texte)

    def clic(self, x, y):
        if self.x <= x <= self.x + self.largeur and self.y <= y <= self.y + self.hauteur:
            return True
        return False

class App:
    def __init__(self):
        pyxel.init(200, 150, fps=60)
        pyxel.mouse(True)

        self.bouton = Bouton(50, 50, 100, 30, "Fermer")

        pyxel.run(self.mise_a_jour, self.dessine)

    def mise_a_jour(self):
        
       
            if self.bouton.clic(pyxel.mouse_x, pyxel.mouse_y):
                Jeu()
                pyxel.quit()
                


    def dessine(self):
        pyxel.cls(0)
        self.bouton.dessiner()




if __name__ == "__main__":
   
    Jeu()

