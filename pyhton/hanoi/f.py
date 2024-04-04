import pygame
from pygame.locals import *
import time
import pyxel
class Display_hanoi:

    color_red = (255, 0, 0)
    color_blue = (0, 0, 255)
    color_green = (0, 255, 0)
    color_black = (0, 0, 0)
    color_white = (255, 255, 255)
    

    def __init__(self, title, width, height, pause_t):
        pygame.init()
        self.width = width
        self.height = height
        self.pause_time = pause_t
        pygame.display.set_caption(title)
        self.window_surface = pygame.display.set_mode((width, height))

    def drawHanoi(self, lLeft, lMiddle, lRight):
        n = len(lLeft[1]) + len(lMiddle[1]) + len(lRight[1])
        recHeight = int(self.height / n)
        maxRecWidth = self.width / 3
        self.window_surface.fill(self.color_white)

        indx = 0

        # La fonction Hanoi change l'ordre des listes, il faut donc un sort
        for i in sorted((lLeft, lMiddle, lRight)):
            refY = self.height-recHeight
            for j in i[1]:
                recWidth = int(maxRecWidth * j / n)
                refX = int(indx + (maxRecWidth - recWidth) / 2)
                recColor = self.color_blue

                # Le changement porte toujours sur le dernier element de la pile middle
                if len(lMiddle[1]) > 0 and j == lMiddle[1][-1]:
                    recColor = self.color_green
                #rect = Rect(indx, self.height - l[i] * ratioHeigt, recWidth, l[i] * ratioHeigt)
                rect = Rect(refX, refY, recWidth, recHeight)
                pygame.draw.rect(self.window_surface, recColor, rect)
                refY -= recHeight
            indx += maxRecWidth

        pygame.display.flip()
        time.sleep(self.pause_time)

    def waitQuit(self):
        launched = True
        while launched:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    launched = False


def hanoi(nb_disques, depart, arrivee, intermediaire):
    if nb_disques > 0:
        hanoi(nb_disques-1, depart, intermediaire, arrivee)
        print('Déplacer', depart, 'vers', arrivee)
        hanoi(nb_disques-1, intermediaire, arrivee, depart)

def hanoi_display(nb_disques, depart, arrivee, intermediaire):
    if nb_disques > 0:
        hanoi_display(nb_disques-1, depart, intermediaire, arrivee)
        arrivee[1].append(depart[1].pop())
        graphHanoi.drawHanoi(depart, arrivee, intermediaire)
        hanoi_display(nb_disques-1, intermediaire, arrivee, depart)

#print('Nombre de deplacements', hanoi(20, 'gauche', 'droite', 'milieu'))

graphHanoi = Display_hanoi('Les tours de Hanoï', 1500, 600,  2)
nb_disques = 3
depart = (1, list(range(nb_disques,0,-1)))
arrivee = (3, [])
intermediaire = (2, [])
graphHanoi.drawHanoi(depart, arrivee, intermediaire)
hanoi_display(nb_disques, depart, arrivee, intermediaire)
graphHanoi.waitQuit()


class DisplayHanoi:
    def __init__(self, nb_disques):
        # Initialisation de Pyxel avec une résolution de 160x120 pixels et une fréquence d'images de 30 par seconde
        pyxel.init(160, 120, fps=30)
        
        # Initialisation des attributs de la classe
        self.nb_disques = nb_disques
        self.depart = list(range(nb_disques, 0, -1))
        self.arrivee = []
        self.intermediaire = []
        self.frame_count = 0
        
        # Exécution de la boucle principale du jeu avec les fonctions update et draw
        pyxel.run(self.update, self.draw)

    def update(self):
        # Incrémentation du compteur de frames
        self.frame_count += 1

        # Logique de mise à jour du jeu ici (déplacement des disques, etc.)

        if self.frame_count == 60:
            # Réinitialisation du compteur après 60 frames (1 seconde)
            self.frame_count = 0
            # Effectuer des actions après le délai (par exemple, déplacer un disque)

    def draw(self):
        # Effacement de l'écran
        pyxel.cls(0)
        # Appel de la fonction pour dessiner la tour de Hanoï
        self.drawHanoi()

    def drawHanoi(self):
        n = self.nb_disques
        rec_height = 8
        max_rec_width = 20
        indx = 0

        # Dessin des piliers et des disques
        for i in [self.depart, self.intermediaire, self.arrivee]:
            ref_y = 120 - rec_height
            for j in i:
                rec_width = int(max_rec_width * j / n)
                ref_x = int(indx + (max_rec_width - rec_width) / 2)
                pyxel.rect(ref_x, ref_y, rec_width, rec_height, 12)
                ref_y -= rec_height
            indx += max_rec_width

# Création de l'instance de la classe DisplayHanoi avec 3 disques
hanoi_display = DisplayHanoi(3)
