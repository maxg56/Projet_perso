import pyxel



class Tuile:
    def __init__(self, largeur: int = 0, hauteur: int = 0, x: int = 0, y: int = 0, z: int = 0):
        self.largeur = largeur
        self.hauteur = hauteur
        self.x = x
        self.y = y
        self.z = z

    def Rendu(self):
        pass
        



class App:
    def __init__(self):
        pyxel.init(160, 120) 
        self.x = 0
        pyxel.run(self.update, self.draw)
        
        

    def update(self):
        pyxel.image(0).set(10, 10, ["0123", "4567", "89ab", "cdef"])
        self.x = (self.x + 1) % pyxel.width

    def draw(self):
        pyxel.cls(0)
        pyxel.rect(self.x, 0, 8, 8, 9)

App()


