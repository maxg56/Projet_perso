import pyxel
from random import choice
LARGEUR =10
LIGNES_VIDES = 3
HAUTEUR =20 + LIGNES_VIDES
TAILLE_CASE = 16
NOIR = 0
GRIS =13
ROURE = 8
FPS =40
DELES_DE_CHUT = FPS //4
POINTS = [0,40,100,300,1200 ]

FORMES = [
    ([(0,0),(-1,0),(-2,0),(1,0)],4),
    ([(0,0),(1,1),(0,-1),(1,0)],5),
    ([(0,0),(-1,0),(1,0),(0,1)],6),
    ([(0,0),(1,0),(0,1),(-1,1)],7),
    ([(0,0),(-1,0),(1,0),(1,1)],8),
    ([(0,0),(-1,0),(0,-1),(0,-2)],9),
    ([(0,0),(1,0),(0,-1),(0,-2)],10)
]

class Tetrmino:
    def __init__(self) -> None:
        self.cases ,self.couleur= choice(FORMES)
        self.cases = [ (x+ LARGEUR //2 ,y+2 )for x,y in self.cases ]
        

    def dessine(self):
        for x ,y in self.cases:
            pyxel.rect(x *TAILLE_CASE,y*TAILLE_CASE,TAILLE_CASE,TAILLE_CASE,self.couleur)



class Tetris:
    def __init__(self) -> None:
        self.grille = [[NOIR for  x in range(LARGEUR)]for y in range(HAUTEUR)]
        self.tetrmino = Tetrmino()
        self.tetrmino2 = Tetrmino()
        self.rérve = None
        self.t = DELES_DE_CHUT
        self.t2 = DELES_DE_CHUT //2
        self.sore = 0


        pyxel.init(LARGEUR*TAILLE_CASE ,HAUTEUR*TAILLE_CASE, title ="Tetris", fps =FPS)
        self.tetrmino.dessine()
        pyxel.mouse(True)
        pyxel.run(self.mise_a_jour,self.dessine)
    def mise_a_jour(self):
        self.t -= 1 
        self.t2 = min(self.t2+1,DELES_DE_CHUT) 
        dx = 0
        rottation = False
        resve = False
        if self.t == 0 : 
            succes = self.deplacent_vertical()
            if not succes:
                for x,y in self.tetrmino.cases:
                    if y == LIGNES_VIDES:
                        pyxel.quit()
                    self.grille[y][x] = self.tetrmino.couleur
                self.tetrmino = self.tetrmino2
                self.tetrmino2 = Tetrmino()
            self.t = DELES_DE_CHUT

        if pyxel.btn(pyxel.KEY_M):
            resve = True
        if pyxel.btn(pyxel.KEY_LEFT):
            dx -=1       
        if pyxel.btn(pyxel.KEY_RIGHT):
            dx += 1
        if pyxel.btn(pyxel.KEY_UP):
            rottation = True

        if self.t2 >= DELES_DE_CHUT//2 :
            if dx != 0:
                self.deplacent_horomino(dx)
            elif rottation:
                self.rotation()
            elif resve :
                self.rerve()
            self.t2 =  0  
        
        a_supprimer  = []
        for y in range(HAUTEUR):
            if all(couleur != NOIR for couleur in self.grille[y]):
                a_supprimer.append(y)
        a_supprimer.reverse()
        for y in a_supprimer:
            self.grille.pop(y)
        for y in a_supprimer:
            self.grille.insert(0 ,[NOIR for x in range(LARGEUR)])

        self.sore += POINTS[len(a_supprimer)]
        

            

        

    
    def dessine(self):
        # fon 

        pyxel.cls(NOIR)

        self.tetrmino.dessine()
        for y in range(HAUTEUR) :
            for x in range(LARGEUR):
                couleur = self.grille[y][x]
                if couleur != NOIR:
                    pyxel.rect(x*TAILLE_CASE,y*TAILLE_CASE,TAILLE_CASE,TAILLE_CASE,couleur)        
        # La grille
        for x in range(LARGEUR):
            pyxel.line(x * TAILLE_CASE, 0, x * TAILLE_CASE,HAUTEUR*TAILLE_CASE , GRIS)
        for y in range(HAUTEUR):
            pyxel.line(0, y * TAILLE_CASE, LARGEUR*TAILLE_CASE, y * TAILLE_CASE, GRIS)

        pyxel.rect(0,0, LARGEUR * TAILLE_CASE ,LIGNES_VIDES*TAILLE_CASE , 7)
        pyxel.text(0,0 , str(self.sore), 10)
        
        self.tetrmino2.dessine()
    
    def deplacent_vertical(self):
        nouvlles =[]
        for x,y in self.tetrmino.cases:
            y += 1
            if y  < HAUTEUR  and self.grille[y][x] == NOIR:
                nouvlles.append((x,y))
            else:
                return False
        self.tetrmino.cases = nouvlles
        return True
    
    def deplacent_vertical_rapide(self):
        nouvlles =[]
        for x,y in self.tetrmino.cases:
            y += 4
            if y  < HAUTEUR  and self.grille[y][x] == NOIR:
                nouvlles.append((x,y))
            else:
                return False
        self.tetrmino.cases = nouvlles
        return True
    
    def deplacent_horomino(self,dx):
        nouvlles =[]
        for x,y in self.tetrmino.cases:
            x += dx
            if  0 <= x  < LARGEUR and self.grille[y][x] == NOIR:
                nouvlles.append((x,y))
            else:
                return False
        self.tetrmino.cases = nouvlles
        return True
    
    def rotation(self):
        x_ref , y_ref = self.tetrmino.cases [0]
        nouvlles =[]
        for x,y in self.tetrmino.cases:
            x -= x_ref 
            y -= y_ref
            x,y= -y,x
            x += x_ref
            y += y_ref
            if  0 <= x  < LARGEUR  and 0 <= y  < HAUTEUR and self.grille[y][x] == NOIR:
                nouvlles.append((x,y))
            else:
                return False
        self.tetrmino.cases = nouvlles
        return True
    
    def rerve(self):
        if self.rérve is not None :
                
            self.rérve ,self.tetrmino = self.tetrmino,self.rérve
            self.tetrmino.cases = self.rérve.cases
        else :
            self.rérve = self.tetrmino
            self.tetrmino = self.tetrmino2
            self.tetrmino2 = Tetrmino()
    
Tetris()