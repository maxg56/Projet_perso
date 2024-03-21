import arcade

TAILLE_CASE = 20
NB_CASES = 20
LARGEUR = NB_CASES * TAILLE_CASE
HAUTEUR = NB_CASES * TAILLE_CASE

class Bateau:
    def __init__(self, largeur: int = 2, hauteur: int = 2) -> None:
        self.largeur = largeur
        self.hauteur = hauteur

class Entrepose(Bateau):
    def __init__(self, largeur: int = 2, hauteur: int = 2) -> None:
        super().__init__(largeur, hauteur)
        self.stock = {}
        self.color = (0, 0, 255)  # Couleur bleue pour les cases remplies

class App(arcade.Window):
    def __init__(self):
        super().__init__(LARGEUR, HAUTEUR, "Grille")
        self.grille = self.creation_grille()
        self.grille[0][0] = arcade.color.RED

    def creation_grille(self):
        grille = [[None for _ in range(NB_CASES)] for _ in range(NB_CASES)]
        return grille

    def draw_grid(self):
        for x in range(0, LARGEUR, TAILLE_CASE):
            arcade.draw_line(x, 0, x, HAUTEUR, arcade.color.BLACK, 2, 2)

        for y in range(0, HAUTEUR, TAILLE_CASE):
            arcade.draw_line(0, y, LARGEUR, y, arcade.color.BLACK, 2, 2)

    def on_draw(self):
        arcade.start_render()
        self.draw_grid()

def main():
    app = App()
    arcade.run()

if __name__ == "__main__":
    main()
