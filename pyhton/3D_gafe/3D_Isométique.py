import pyxel
from typing import List,Tuple,Union,Any
from math import cos,sin 
LARGEUR =20
Z =10 
HAUTEUR =10
TAIHE_CASE = 36
NOUAR = 7
class juex  :
    def __init__(self,fps :int =30,) ->None:
        
        pyxel.init(LARGEUR*TAIHE_CASE, HAUTEUR*TAIHE_CASE, fps=fps)
        self.gri =[[[NOUAR for x in range(LARGEUR) ]for y in range(HAUTEUR)]for z in range(Z)]
        
       
        self.frame_count =0

        
        
        
        # Exécution de la boucle principale du jeu avec les fonctions update et draw
        pyxel.run(self.update, self.draw)

    def update(self):
        self.frame_count += 1
        
        if self.frame_count == 30:
            pass

           
            

    def draw(self):
        
        pyxel.image(0)
        for x in range(LARGEUR):
            pyxel.line(x,x,x,HAUTEUR,7)
            
        
juex()