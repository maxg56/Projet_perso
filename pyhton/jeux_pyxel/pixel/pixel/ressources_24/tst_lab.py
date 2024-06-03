from typing import List

def mapv2(taille: int) -> List[List[int]]:
    MUR = 1  # Représente un mur dans le labyrinthe
    VIDE = 0  # Représente un espace vide dans le labyrinthe
    
    labyrinthe = []
    contre = 0

    for j in range(taille + 1):
        line = []
        for i in range(taille + 1):
            if i == 0 or i == taille or j == 0 or j == taille:
                line.append(MUR)
            elif j % 2 == 0:
                if i % 2 == 0:
                    line.append(MUR)
                else:
                    line.append(VIDE)
                    contre += 1
            else:
                if i % 2 == 0:
                    line.append(VIDE)
                    contre += 1
                else:
                    line.append(MUR)
        labyrinthe.append(line)

    print(f"Nombre d'espaces vides: {contre}")
    return labyrinthe

# Exemple d'utilisation
taille = 5
labyrinthe = mapv2(taille)
for ligne in labyrinthe:
    print(ligne)
