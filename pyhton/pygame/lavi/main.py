import pygame
import sys
from bruit_de_perlin import bruit_de_perlin


class Game:
    def __init__(self):
        pygame.init()
        self.width = 800
        self.height = 600
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Mon jeu Pygame")
        self.image = pygame.image.load("/home/max_dev/Documents/git/Projet_perso/pyhton/pygame/lavi/ressources/tente.png")
        self.image2 = pygame.image.load("/home/max_dev/Documents/git/Projet_perso/pyhton/pygame/lavi/ressources/peti.png")
        self.camera_x = 0
        self.camera_y = 0

    def handle_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.camera_x -= 5
        if keys[pygame.K_RIGHT]:
            self.camera_x += 5
        if keys[pygame.K_UP]:
            self.camera_y -= 5
        if keys[pygame.K_DOWN]:
            self.camera_y += 5

    def render(self):
        self.screen.fill((100, 200, 30))
        self.screen.blit(self.image, (100 - self.camera_x, 100 - self.camera_y))
        self.screen.blit(self.image2, (10 - self.camera_x, 10 - self.camera_y))
        pygame.display.flip()

    def run(self):
        clock = pygame.time.Clock()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.handle_input()
            self.render()
            clock.tick(60)  # Limiter la vitesse de la boucle principale à 60 images par seconde

if __name__ == "__main__":
    game = Game()
    game.run()

