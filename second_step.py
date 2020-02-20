import pygame

# Intialize the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))

# Background
background = pygame.image.load('assets/img/background/background1.png')

# Caption and Icon
pygame.display.set_caption("eKids project")
icon = pygame.image.load('assets/img/ufo.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('assets/img/player/player1.png')
playerX = 370
playerY = 480
playerX_change = 0

# Step 2 - 1
# Bullet

def player(x, y):
    screen.blit(playerImg, (x, y))

def fire_bullet(x, y):
    global bullet_state # I don't like it. Can not use global to avoid unnecessary explanations ?
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))

# Timer
clock = pygame.time.Clock()

# Game Loop
running = True
while running:

    clock.tick(50)

    # RGB = Red, Green, Blue
    screen.fill((0, 0, 0))
    # Background Image
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # if keystroke is pressed check whether its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5

            if event.key == pygame.K_SPACE:
                # Step 2 - 2
                # if bullet_state is "ready":
                # Get the current x cordinate of the spaceship
                pass

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    # Step 2 - 3
    # Bullet Movement

    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    player(playerX, playerY)
    pygame.display.update()
