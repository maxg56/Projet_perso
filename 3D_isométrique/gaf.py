import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from random import randrange





def dessine(batiments, fichier=None):
    """Dessine les batiments en perspective isométrique.
    Si on fournit un nom de fichier, la figure est sauvegardée
    à cet emplacement, sinon elle est simplement affichée.
    """
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    couleurs = ["#%06X" % randrange(0, 0xFFFFFF) for _ in range(len(batiments))]
    # Dessine chaque bâtiment en utilisant ax.bar3d
    for( x_d, x_f, y_d, y_f, z_d, z_f) ,couleurs in zip(batiments,couleurs):
        ax.bar3d(x_d, y_d, z_d, x_f - x_d, y_f - y_d, z_f - z_d, color=couleurs)
        
    # Calcul des limites des axes x et y
    x_max = max(x_f for x_d, x_f, _, _, _, _ in batiments)
    y_max = max(y_f for _, _, y_d, y_f, _, _ in batiments)
    
    # Configuration de l'axe
    ax.set_aspect('equal', adjustable='box')
    #ax.set_xticks(range(x_max + 1))
    #ax.set_yticks(range(y_max + 1))
    #ax.set_xlim(0, x_max)
    #ax.set_ylim(0, y_max)
    
    # Sauvegarde ou affichage de la figure
    if fichier is not None:
        plt.savefig(fichier)
    else:
        plt.show()


from random import randrange

def chevauchement(batiments, x_d, x_f, y_d, y_f, z_d, z_f):
    """Vérifie s'il y a chevauchement avec les bâtiments existants."""
    for b in batiments:
        if (x_d < b[1] and x_f > b[0] and
            y_d < b[3] and y_f > b[2] and
            z_d < b[5] and z_f > b[4]):
            return True
    return False

def batiments_aleatoires(n, x_maxi=10, y_maxi=10, z_maxi=5, largeur_max=5)-> list:
    """
    Renvoie n triplets (gauche, droite, haut, bas, devant, derrière)
    avec 0 <= gauche < x_maxi
         gauche + 1 <= droite <= x_maxi
         0 <= haut < y_maxi
         haut + 1 <= bas <= y_maxi
         0 <= devant < z_maxi
         devant + 1 <= derrière <= z_maxi
    """
    batiments = []
    while len(batiments) != n:
        x_d = randrange(0, x_maxi - 1)
        x_f = min(largeur_max, randrange(1, x_maxi - x_d))
        y_d = randrange(0, y_maxi - 1)
        y_f = min(largeur_max, randrange(1, y_maxi - y_d))
        z_d = 0
        z_f = randrange(1, z_maxi - 1)

        if not chevauchement(batiments, x_d, x_d + x_f, y_d, y_d + y_f, z_d, z_d + z_f):
            batiments.append((x_d, x_d + x_f, y_d, y_d + y_f, z_d, z_d + z_f))
    return batiments



dessine(batiments_aleatoires(20,20,20,20,5) )

