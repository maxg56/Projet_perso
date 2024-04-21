import pygame

# pygame setup
pygame.init()
LARGEUR =  720
LONGUEUR = 1280
RAYON = 40
avancer_x = 10
avancer_y = 10
screen = pygame.display.set_mode((LONGUEUR, LARGEUR))
clock = pygame.time.Clock()
running = True
dt = 100

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    pygame.draw.circle(screen, "red", player_pos, RAYON)

    
    keys = pygame.key.get_pressed()
    
    if player_pos.y+(RAYON//2) >= LARGEUR :
        avancer_y *= -1
    if player_pos.y+(RAYON//2) <= 0 :
        avancer_y *= -1
    
    if player_pos.x+(RAYON//2) >= LONGUEUR :
        avancer_x *= -1
    if player_pos.x+(RAYON//2) <= 0 :
        avancer_x *= -1


   
    if keys[pygame.K_z]:
        player_pos.y -= avancer_y * dt
    if keys[pygame.K_s]:
        player_pos.y += avancer_y * dt
    if keys[pygame.K_q]:
        player_pos.x -= avancer_x * dt
    if keys[pygame.K_d]:
        player_pos.x += avancer_x * dt


    player_pos.y += avancer_y
    player_pos.x += avancer_x
    
    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()