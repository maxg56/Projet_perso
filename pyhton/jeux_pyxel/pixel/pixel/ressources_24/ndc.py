import pyxel
from typing import Union ,List,Type , Dict
from random import randint,random
from collections import deque 
from f import GenerateurDeLabyrinthe

COULEURS = {
    "NOIR" : 0,
    "BLEU_FONCE" : 1,
    "BLEU_CLAIR" : 3,
    "MARRON_FONCE" : 4,
    "MARRON_CLAIR" : 9, 
    "COULEUR_JOUEUR" : 8 ,   
}
TAILLE_CASE = 8
VUE = 5
HAUTEUR = 127
LARGEUR = 127
NOMBRE_DE_CASE =  HAUTEUR//TAILLE_CASE
FPS = 10
VIDE = 0
MUR = 1
CLE = 2
POR = 3
CASE_DEP = (1, (NOMBRE_DE_CASE - 1))
HAUT = (0, -1)
BAS = (0, 1)
GAUCHE = (-1, 0)
DROITE = (1, 0)
MOVE = [HAUT,BAS,GAUCHE,DROITE]

class GenerateurDeLabyrinthe:
    def __init__(self) -> None:
        pass
class Joueur:
    def __init__(self):
        self.x ,self.y = CASE_DEP
        self.cle_possede = False
    def dessine(self):
        #pyxel.rect(self.x *TAILLE_CASE, self.y *TAILLE_CASE, TAILLE_CASE //2,  TAILLE_CASE -2, 8)
        pyxel.blt(self.x * TAILLE_CASE, self.y * TAILLE_CASE, 0, 24, 32, TAILLE_CASE, TAILLE_CASE, 14)
class Ojest :
    def __init__(self):
        self.x = randint(0,NOMBRE_DE_CASE-1)
        self.y = randint(0,NOMBRE_DE_CASE-1)
    def la_map(self):
        pass
class Porte:
    def __init__(self, niveau: bool = False):
        self.x = randint(0,NOMBRE_DE_CASE-1)
        self.y = randint(0,NOMBRE_DE_CASE-1)
        self.niveau = niveau
        
        
    def dessine(self):
        
        if self.niveau:
            pyxel.blt(self.x * TAILLE_CASE, self.y * TAILLE_CASE, 0, 8, 32, 8, 8, 14)
        else:
            pyxel.blt(self.x * TAILLE_CASE, self.y * TAILLE_CASE, 0, 0, 40, 8, 8, 14)
class Cle:
    def __init__(self,couloir:int =0):
        self.x = randint(0,NOMBRE_DE_CASE-1)
        self.y = randint(0,NOMBRE_DE_CASE-1)
        self.couloir = couloir
        
    def dessine(self):
        pyxel.blt(self.x *TAILLE_CASE, self.y *TAILLE_CASE, 0, 0, 32, 8, 8, 14)

class Jeu:
    def __init__(self):
        
        self. n = 0.1
        self.score = 0
        self.joueur = Joueur()
        self.porte = Porte(COULEURS["MARRON_CLAIR"])
        self.cle = Cle(COULEURS["BLEU_CLAIR"])
        
        self.map = self.génératre_de_map(self.n)
        
        pyxel.init(128, 128, title="NDC 2024" , fps=FPS)
        pyxel.load("ndc.pyxres")
        pyxel.run(self.mise_a_jour, self.dessine)


    def mise_a_jour(self):
        dx = 0
        dy = 0

        if pyxel.btn(pyxel.KEY_DOWN)or pyxel.btn(pyxel.KEY_S):
            dx, dy = BAS
        elif pyxel.btn(pyxel.KEY_UP) or pyxel.btn(pyxel.KEY_Z):
            dx, dy = HAUT
        elif pyxel.btn(pyxel.KEY_RIGHT) or pyxel.btn(pyxel.KEY_D):
            dx, dy = DROITE
        elif pyxel.btn(pyxel.KEY_LEFT) or pyxel.btn(pyxel.KEY_Q):
            dx, dy = GAUCHE
    
        if (dx + self.joueur.x) *TAILLE_CASE  >= LARGEUR or (dx + self.joueur.x) *TAILLE_CASE  <  0 :
            dx = 0   
 
        if (dy + self.joueur.y) *TAILLE_CASE  >= HAUTEUR or (dy + self.joueur.y) *TAILLE_CASE  < 0:
            dy = 0

        if self.map[dx + self.joueur.x][dy + self.joueur.y] == MUR :
                dy , dx = 0,0 

        self.joueur.x += dx
        self.joueur.y += dy 
        if (self.joueur.x , self.joueur.y) == (self.cle.x,self.cle.y):
            self.joueur.cle_possede = True

        if (self.joueur.x , self.joueur.y) == (self.porte.x,self.porte.y) and self.joueur.cle_possede:
            self.n += 0.1 
            self.score += 1
        
            self.joueur = Joueur()
            if self.score % 2 == 0:   
                self.porte = Porte(True)
            else:
                self.porte = Porte(False)
            self.cle = Cle(COULEURS["BLEU_CLAIR"])
            self.map = self.génératre_de_map(self.n)
            if  self.n >= 1 :
                print("Bravo vous êtes arrivé au niveau", int(self.n * 10), "!")
                pyxel.quit()

               
        
        

        
   
    def génératre_de_map(self,n:float) ->List[List[int]]:
        if n >= 0.4 :
            n = 0.4
        carte = [[MUR if random()< n else VIDE for  _ in range(NOMBRE_DE_CASE+1)] for _ in range(NOMBRE_DE_CASE+1)]
        carte[self.joueur.x][self.joueur.y] = 2
        carte[self.cle.x][self.cle.y] = CLE
        carte[self.porte.x][self.porte.x] = POR
        
       
        return carte

    def mapv2(self,taille) ->List[List[int]]:
        labyrinthe = []
        contre = 0
        for j in range(NOMBRE_DE_CASE+1):
            line =[]
            for i in range(NOMBRE_DE_CASE+1):
                if i == 0 or i == NOMBRE_DE_CASE or j == 0 or j == NOMBRE_DE_CASE:
                    line.append(MUR)
                elif j %2 == 0 :
                    if i %2 == 0 :
                        line.append(MUR)
                    else:
                        line.append(VIDE)
                        contre += 1
                else:
                    if i %2 == 0 :
                        line.append(VIDE)
                        contre += 1
                    else:
                        line.append(MUR)
            labyrinthe.append(line)
        print(contre)
        return labyrinthe
        

    def dessine(self):
        pyxel.cls(COULEURS["NOIR"])

        dx = max(self.joueur.x-VUE,0)
        fx = min(self.joueur.x+VUE,NOMBRE_DE_CASE)+1
        dy = max(self.joueur.y-VUE,0)
        fy = min(self.joueur.y+VUE,NOMBRE_DE_CASE)+1
        
        for i in range(dx,fx):
            for j in range(dy,fy):
                pyxel.rect(i *TAILLE_CASE, j *TAILLE_CASE, TAILLE_CASE ,  TAILLE_CASE , COULEURS["BLEU_FONCE"])
                if self.map[i][j] == MUR: 
                    if self.score % 2 == 0:   
                        pyxel.blt(i * TAILLE_CASE, j * TAILLE_CASE, 0, 8, 40, TAILLE_CASE, TAILLE_CASE, 14)
                    else:
                        pyxel.blt(i * TAILLE_CASE, j * TAILLE_CASE, 0, 16, 32, TAILLE_CASE, TAILLE_CASE, 14)
                
                    
        
        if not self.joueur.cle_possede  and dx<=self.cle.x < fx  and dy <= self.cle.y < fy : 
            self.cle.dessine()
        if dx<=self.porte.x < fx  and dy <= self.porte.y < fy:
            self.porte.dessine()
        self.joueur.dessine()
        
Jeu()