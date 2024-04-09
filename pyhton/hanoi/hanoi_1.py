import pyxel
from typing import List,Tuple,Union,Deque
from Piles import Piles 

LARGEUR, HAUTEUR = 200, 120
LARGEUR_BASE, HAUTEUR_BASE = LARGEUR // 6, 5
X_BASE_1, Y_BASE = 20, HAUTEUR - 10
X_BASE_2 = X_BASE_1 + LARGEUR_BASE * 2
X_BASE_3 = X_BASE_2 + LARGEUR_BASE * 2


class Bloc:
    """Classe représentant un bloc dans la tour de Hanoi."""
    def __init__(self, valeur :int , longueur:int, hauteur:int, x:int, y:int) -> None:
        self.valeur = valeur
        self.longueur = int(longueur)
        self.hauteur = hauteur
        self.x, self.y = x, y
        

    def dessine_Bloc(self, couleur:int)->None:
        """dessine les Bloce"""
        pyxel.rect(self.x, self.y, self.longueur, self.hauteur, couleur)
        pyxel.text(self.x+(self.longueur//2),self.y,str(self.valeur),7)
        

    def Déplace(self, x:int,y:int)->None:
        """Déplace un bloc aux coordonnées spécifiées."""
        self.x = x 
        self.y = y 
        
    def __str__(self) -> str:
        return(f'v ={self.valeur} l,h ={self.longueur,self.hauteur} x = {self.x}y ={self.y}')

class Toure :
    """Classe représentant une tour dans le jeu de Hanoi."""
    def __init__(self, x_base :int ,y_base:int =Y_BASE ,etage :int = None ) -> None:
        self.tours = Piles()
        self.ref_x = x_base 
        self.ref_y = y_base -8
        self.r =6
        if etage is not None:
            rec_height = 8
            
            largeur_etage_min = 11
            largeur_etage = int(largeur_etage_min +6*etage)
            if largeur_etage > LARGEUR_BASE:
                largeur_etage = LARGEUR_BASE
                self.r =2.2
            
            

            for n in range(etage,0,-1):
                largeur_etage  -=self.r
                if self.tours.est_vide():
                    b_ref_x =self.ref_x + LARGEUR_BASE//2 - largeur_etage//2
                else:
                    b2 :Bloc = self.tours.depiler()
                    b_ref_x = b2.x +b2.longueur//2 - largeur_etage//2
                    self.tours.empiler(b2)
                x2 = b_ref_x 
                self.tours.empiler(Bloc(n, largeur_etage, rec_height,b_ref_x, self.ref_y))
                self.ref_y -= rec_height
                
            
            
        
    def dessine_tore(self) -> Piles:
        """dessine les tore """
        tmp =Piles()
        while not self.tours.est_vide():
            bl:Bloc = self.tours.depiler()
            bl.dessine_Bloc(12)
            tmp.empiler(bl)
        while not tmp.est_vide():
            self.tours.empiler(tmp.depiler())
        return self.tours
    
    def deplasé_vre(self,toure ) :
        if type(toure) is Toure and not self.tours.est_vide():
            b :Bloc = self.tours.depiler()
            if not toure.tours.est_vide():
                b2 :Bloc = toure.tours.depiler()
                ref_x = b2.x + b2.longueur//2 -b.longueur//2
                toure.tours.empiler(b2)
            else:
                 ref_x = toure.ref_x  +LARGEUR_BASE//2- b.longueur//2
            b.Déplace(ref_x,toure.ref_y)
            toure.tours.empiler(b)
            self.ref_y += 8
            toure.ref_y -= 8

   
class DisplayHanoi:
    """Classe principale pour afficher le jeu de Hanoi."""
    def __init__(self, nb_disques :int ,fps :int =30,ot :bool = True, __x1__  = X_BASE_1,__X2__ =X_BASE_2,__X3__ =X_BASE_3) ->None:
        
        pyxel.init(LARGEUR, HAUTEUR, fps=fps)
        self.ot = True
        self.nb_disques = nb_disques
        self.tour_debut= Toure(__x1__,Y_BASE,nb_disques)
        self.tour_milue = Toure(__X2__)
        self.tour_fin = Toure(__X3__)
        
        self.i_orde = 0
        self.frame_count =0
        if self.ot :
            self.orde=self.sousion()
        
        # Exécution de la boucle principale du jeu avec les fonctions update et draw
        pyxel.run(self.update, self.draw)

    def update(self):
        self.frame_count += 1
        
        if self.frame_count == 30:

            if self.i_orde < len(self.orde) and self.ot:
                self.sd(self.orde[self.i_orde],self.tour_debut,self.tour_milue,self.tour_fin)
                self.i_orde += 1
            self.frame_count = 0
            

    def draw(self):
        # Effacement de l'écran
        pyxel.cls(7)

        for x_base in (X_BASE_1, X_BASE_2, X_BASE_3):
            pyxel.rect(x_base, Y_BASE, LARGEUR_BASE, HAUTEUR_BASE, 13)
            
        self.tour_debut.dessine_tore() 
        self.tour_milue.dessine_tore()
        self.tour_fin.dessine_tore()  

    def hanoi(self, n, debut :str = "a" , temporaire :str = "b", fin :str = "c"):
        if n == 1:
            return   debut + fin
        else:
            return (
                self.hanoi(n - 1, debut, fin, temporaire)
                + debut
                + fin
                + self.hanoi(n-1, temporaire, debut, fin)
            )
    
    def sousion(self) -> List[Tuple[set]]:
        reslta = []
        val2 = []

        for val in self.hanoi(self.nb_disques):
            val2.append(val)

            if len(val2) == 2:
                reslta.append(tuple(val2))
                val2 = []

        return reslta
    
    def sd(self,asion :Tuple[str], debut :Toure , milue : Toure , fin : Toure ):
        if asion[0] == "a" :
            if asion[1] == "b":
                debut.deplasé_vre(milue)
            else:
                debut.deplasé_vre(fin)
        elif asion[0] == "b" :
            if asion[1] == "a":
                milue.deplasé_vre(debut)
            else:
                milue.deplasé_vre(fin)
        else:
            if asion[1] == "a":
                fin.deplasé_vre(debut)
            else:
               fin.deplasé_vre(milue)

        





a = DisplayHanoi(10)