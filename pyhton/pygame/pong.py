import pygame
import sys

# Initialisation de Pygame
pygame.init()

# Paramètres du jeu
LARGEUR ,LONGUEUR=  720 ,1280

WIDTH, HEIGHT = 800, 600
BALL_SPEED = 4
PADDLE_SPEED = 10

# Couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Création de la fenêtre du jeu
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

# Police pour le texte
font = pygame.font.Font(None, 74)

# Initialisation des objets du jeu
ball = pygame.Rect(WIDTH // 2 - 15, HEIGHT // 2 - 15, 30, 30)
paddle_left = pygame.Rect(50, HEIGHT // 2 - 60, 20, 120)
paddle_right = pygame.Rect(WIDTH - 70, HEIGHT // 2 - 60, 20, 120)

ball_speed = [BALL_SPEED, BALL_SPEED]
paddle_left_speed = 0
paddle_right_speed = 0

# États du jeu
start_screen = True
game_over = False

# Boucle principale du jeu
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if start_screen or game_over:
                start_screen = False
                game_over = False
                ball.x = WIDTH // 2 - 15
                ball.y = HEIGHT // 2 - 15
                ball_speed = [BALL_SPEED, BALL_SPEED]
            elif event.key == pygame.K_z:
                paddle_left_speed = -PADDLE_SPEED
            elif event.key == pygame.K_s:
                paddle_left_speed = PADDLE_SPEED
            elif event.key == pygame.K_UP:
                paddle_right_speed = -PADDLE_SPEED
            elif event.key == pygame.K_DOWN:
                paddle_right_speed = PADDLE_SPEED
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_z or event.key == pygame.K_s:
                paddle_left_speed = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                paddle_right_speed = 0

    if not start_screen and not game_over:
        # Déplacement des raquettes en vérifiant les limites de l'écran
        if paddle_left_speed < 0 and paddle_left.top > 0:
            paddle_left.y += paddle_left_speed
        elif paddle_left_speed > 0 and paddle_left.bottom < HEIGHT:
            paddle_left.y += paddle_left_speed

        if paddle_right_speed < 0 and paddle_right.top > 0:
            paddle_right.y += paddle_right_speed
        elif paddle_right_speed > 0 and paddle_right.bottom < HEIGHT:
            paddle_right.y += paddle_right_speed

        # Rebondissement de la balle sur les murs verticaux
        if ball.top <= 0 or ball.bottom >= HEIGHT:
            ball_speed[1] = -ball_speed[1]

        # Sortie de la balle par les côtés
        if ball.left <= 0 or ball.right >= WIDTH:
            game_over = True

        # Rebondissement de la balle sur les raquettes
        if ball.colliderect(paddle_left) or ball.colliderect(paddle_right):
            ball_speed[0] = -ball_speed[0]

        # Déplacement de la balle
        ball.x += ball_speed[0]
        ball.y += ball_speed[1]

    # Dessin
    screen.fill(BLACK)

    if start_screen:
        start_text = font.render("Press any key to start", True, WHITE)
        screen.blit(start_text, (WIDTH // 2 - start_text.get_width() // 2, HEIGHT // 2 - start_text.get_height() // 2))
    elif game_over:
        game_over_text = font.render("Game Over", True, WHITE)
        screen.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 2 - game_over_text.get_height() // 2))
    else:
        pygame.draw.rect(screen, WHITE, paddle_left)
        pygame.draw.rect(screen, WHITE, paddle_right)
        pygame.draw.ellipse(screen, WHITE, ball)

    # Mise à jour de l'affichage
    pygame.display.flip()

    # Limite de vitesse
    pygame.time.Clock().tick(60)
