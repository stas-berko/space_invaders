import pygame
import random
import math


def init():
    global screen, background, clock, num_of_enemies

    pygame.init()
    num_of_enemies = 6

    screen = pygame.display.set_mode((800, 600))
    background = pygame.image.load('../assets/img/background/background1.png')
    clock = pygame.time.Clock()

    pygame.display.set_caption("eKids project")
    icon = pygame.image.load('../assets/img/ufo.png')
    pygame.display.set_icon(icon)

    create_player()
    create_bullet()
    create_enemies(num_of_enemies)

    run_game()


def create_player():
    global playerImg, playerX, playerY, playerX_change
    playerImg = pygame.image.load('../assets/img/player/player1.png')
    playerX = 370
    playerY = 480
    playerX_change = 0


def draw_player(x, y):
    global playerX
    if x <= 0:
        playerX = 0
    elif x >= 736:
        playerX = 736
    screen.blit(playerImg, (playerX, y))


def create_enemies(): #explosionSound
    global enemyImg, enemyX, enemyY, enemyX_change, enemyY_change
    enemyImg = pygame.image.load('./assets/img/enemy/enemy0.png')
    enemyX = random.randint(0, 736)
    enemyY = random.randint(50, 150)
    enemyX_change = 4
    enemyY_change = 40


def draw_enemy(x, y):
    screen.blit(enemyImg, (x, y))


def create_bullet():
    global fireSound, bulletImg, bulletX, bulletY, bulletX_change, bulletY_change, bullet_state
    fireSound = pygame.mixer.Sound('../assets/sound/laser.wav')
    bulletImg = pygame.image.load('../assets/img/bullet/bullet1.png')
    bulletX = 0
    bulletY = 480
    bulletX_change = 0
    bulletY_change = 10
    bullet_state = "ready"


def draw_fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))


def event_handling():
    global running, playerX_change, bulletX
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

            # if keystroke is pressed check whether its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5

            if event.key == pygame.K_SPACE and bullet_state == "ready":
                bulletX = playerX
                draw_fire_bullet(bulletX, bulletY)
                fireSound.play()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0


def run_game():
    global bulletY, bullet_state, playerX, running
    running = True
    while running:

        clock.tick(50)
        screen.blit(background, (0, 0))

        event_handling()

        if bulletY <= 0:
            bulletY = 480
            bullet_state = "ready"

        if bullet_state == "fire":
            draw_fire_bullet(bulletX, bulletY)
            bulletY -= bulletY_change

        playerX += playerX_change
        draw_player(playerX, playerY)

        enemyX += enemyX_change
        if enemyX <= 0:
            enemyX_change = 4
            enemyY += enemyY_change
        elif enemyX >= 736:
            enemyX_change = -4
            enemyY += enemyY_change

        draw_enemy(enemyX, enemyY)

        pygame.display.update()


init()
