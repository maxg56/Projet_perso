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
        for y, row in enumerate(self.grille):
            for x, cell in enumerate(row):
                if cell is None:
                    color = arcade.color.WHITE
                else:
                    color = cell
                arcade.draw_rectangle_filled(x * TAILLE_CASE + TAILLE_CASE // 2, 
                                             y * TAILLE_CASE + TAILLE_CASE // 2, 
                                             TAILLE_CASE, TAILLE_CASE, color)

    def on_draw(self):
        arcade.start_render()
        self.draw_grid()

def main():
    app = App()
    arcade.run()

if __name__ == "__main__":
    main()
