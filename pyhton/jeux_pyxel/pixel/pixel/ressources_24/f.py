import random
from typing import List, Tuple

# Constantes pour les différents types de cases dans le labyrinthe
MUR = 1
VIDE = 0
DEPART = 2
ARRIVEE = 3

class GenerateurDeLabyrinthe:
    def __init__(self, taille: int):
        self.taille = taille
        self.labyrinthe = [[MUR for _ in range(taille)] for _ in range(taille)]
        self.depart = (0, 0)
        self.arrivee = (taille - 1, taille - 1)
    
    def generer_labyrinthe(self):
        # Initialisation de la pile et marquage du point de départ
        stack = [self.depart]
        self.labyrinthe[self.depart[0]][self.depart[1]] = VIDE

        # Déplacements possibles : haut, bas, gauche, droite
        directions = [(-2, 0), (2, 0), (0, -2), (0, 2)]

        while stack:
            x, y = stack[-1]
            random.shuffle(directions)  # Mélanger les directions pour un labyrinthe aléatoire

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if 0 <= nx < self.taille and 0 <= ny < self.taille and self.labyrinthe[nx][ny] == MUR:
                    # Ouvrir le mur entre les cellules
                    self.labyrinthe[x + dx // 2][y + dy // 2] = VIDE
                    self.labyrinthe[nx][ny] = VIDE
                    stack.append((nx, ny))
                    break
            else:
                stack.pop()

        self.labyrinthe[self.depart[0]][self.depart[1]] = DEPART
        self.labyrinthe[self.arrivee[0]][self.arrivee[1]] = ARRIVEE

    def afficher_labyrinthe(self):
        
        for ligne in self.labyrinthe:
            print("".join(["#" if case == MUR else " " if case == VIDE else "A" if case == DEPART else "D" for case in ligne]))

# Exemple d'utilisation
taille_du_labyrinthe = 21  
generateur = GenerateurDeLabyrinthe(taille_du_labyrinthe)
generateur.generer_labyrinthe()
generateur.afficher_labyrinthe()
