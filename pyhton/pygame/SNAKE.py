import pygame, sys, random
# permet de réduire ce qu'on doit écrire plusieurs fois
from pygame.math import Vector2
# but : créer le fruit

class SNAKE:
    def __init__(self):
        self.body = [Vector2(5,10),Vector2(6,10),Vector2(7,10)]
        self.direction = Vector2(1,0)
        self.new_block = False

    def draw_snake(self): 
        for block in self.body:
            x_pos = int(block.x * CELL_SIZE)
            y_pos = int(block.y * CELL_SIZE)
            block_rect = pygame.Rect(x_pos,y_pos,CELL_SIZE,CELL_SIZE)            
            pygame.draw.rect(screen,(50,50,200),block_rect)

    def move_snake(self):
        if self.new_block == True:
            body_copy =self.body[:]
            body_copy.insert(0,body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.new_block = False
        else:
            body_copy =self.body[:-1]
            body_copy.insert(0,body_copy[0] + self.direction)
            self.body = body_copy[:]
            
        
    def add_block(self):
        self.new_block = True

class FRUIT:
    def __init__(self):
        self.randomize()

    def draw_fruit(self):
        fruit_rect = pygame.Rect(int(self.pos.x * CELL_SIZE),int(self.pos.y * CELL_SIZE),(CELL_SIZE),(CELL_SIZE))
        pygame.draw.rect(screen,(250,15,15),fruit_rect)

    def randomize(self):
        self.x = random.randint(0,CELL_NUMBER - 1)
        self.y = random.randint(0,CELL_NUMBER - 1)
        self.pos = Vector2(self.x,self.y)


class MAIN:
    def __init__(self):
        self.snake = SNAKE()
        self.fruit = FRUIT()

    def update(self):
        main_game.snake.move_snake()
        self.check_collision()

    def draw_elements(self):    
        self.fruit.draw_fruit()
        self.snake.draw_snake()

    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]:
            self.fruit.randomize()
            self.snake.add_block()

pygame.init()
CELL_SIZE = 30
CELL_NUMBER = 20
# Création de variable
screen = pygame.display.set_mode((CELL_NUMBER * CELL_SIZE,CELL_NUMBER * CELL_SIZE))
clock = pygame.time.Clock()

# Boucle infinie

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE,150)

main_game = MAIN()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            main_game.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                main_game.snake.direction = Vector2(0,-1)
            if event.key == pygame.K_RIGHT:
                main_game.snake.direction = Vector2(1,0)           
            if event.key == pygame.K_DOWN:
                main_game.snake.direction = Vector2(0,1)
            if event.key == pygame.K_LEFT:
                main_game.snake.direction = Vector2(-1,0)
    # Décide de la couleur du fond : s'appuie sur les 3 couleurs primaires avec un pourcentage de 0 à 255      
    screen.fill((175,215,70))
    main_game.draw_elements()
    pygame.display.update()
    clock.tick(60)

""" 1 : 06 : 22"""