import pygame
import random
import math


def finalize(message):
    background = pygame.image.load('./assets/img/background/gameover.png')

    screen.blit(background, (0, 0))

    f1 = pygame.font.Font(None, 200)
    text1 = f1.render(message, 1, (180, 0, 0))
    screen.blit(text1, (100, 300))
    pygame.display.update()

    while True:
        clock.tick(50)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            if event.type == pygame.KEYDOWN:
                exit()


def init():
    global screen, background, clock, num_of_enemies, enemy_alive, enemy_dead, game_result_win

    pygame.init()
    num_of_enemies = 6
    enemy_alive = "enemy_alive"
    enemy_dead = "enemy_dead"

    win_message = "You Win!"
    lost_message = "You Lost!"
    game_result_win = False

    screen = pygame.display.set_mode((800, 600))
    background = pygame.image.load('./assets/img/background/background1.png')
    clock = pygame.time.Clock()

    pygame.display.set_caption("eKids project")
    icon = pygame.image.load('./assets/img/ufo.png')
    pygame.display.set_icon(icon)

    create_player()
    create_bullet()
    create_enemies(num_of_enemies)

    run_game()

    print(game_result_win)

    if game_result_win:
        finalize(win_message)
    else:
        finalize(lost_message)


def create_player():
    global playerImg, playerX, playerY, playerX_change
    playerImg = pygame.image.load('./assets/img/player/player1.png')
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


def create_enemies(enemies_count):
    global enemyImg, enemyX, enemyY, enemyX_change, enemyY_change, enemy_state
    enemyImg = []
    enemyX = []
    enemyY = []
    enemyX_change = []
    enemyY_change = []
    enemy_state = []

    for i in range(enemies_count):
        enemyImg.append(pygame.image.load('./assets/img/enemy/enemy' + str(i) + '.png'))
        enemyX.append(random.randint(0, 736))
        enemyY.append(random.randint(50, 150))
        enemyX_change.append(4)
        enemyY_change.append(40)
        enemy_state.append(enemy_alive)


def draw_enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))


def create_bullet():
    global fireSound, explosionSound, bulletImg, bulletX, bulletY, bulletX_change, bulletY_change, bullet_state
    fireSound = pygame.mixer.Sound('./assets/sound/laser.wav')
    explosionSound = pygame.mixer.Sound('./assets/sound/explosion.wav')
    bulletImg = pygame.image.load('./assets/img/bullet/bullet1.png')
    bulletX = 0
    bulletY = 480
    bulletX_change = 0
    bulletY_change = 10
    bullet_state = "ready"


def draw_fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))


def isCollision(enemyX, enemyY, bulletX, bulletY, collision_radius=27):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + (math.pow(enemyY - bulletY, 2)))
    if distance < collision_radius:
        return True
    else:
        return False


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

            if (event.key == pygame.K_SPACE) and (bullet_state == "ready"):
                bulletX = playerX
                draw_fire_bullet(bulletX, bulletY)
                fireSound.play()

        if event.type == pygame.KEYUP:
            if (event.key == pygame.K_LEFT) or (event.key == pygame.K_RIGHT):
                playerX_change = 0


def run_game():
    global bulletY, bullet_state, playerX, running, game_result_win
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

        if all(state == enemy_dead for state in enemy_state):
            game_result_win = True
            running = False

        if (max(enemyY) > 420):
            running = False

        for i in range(num_of_enemies):

            if (isCollision(enemyX[i], enemyY[i], playerX, playerY, 40)):
                running = False

            enemyX[i] += enemyX_change[i]
            if enemyX[i] <= 0:
                enemyX_change[i] = 4
                enemyY[i] += enemyY_change[i]
            elif enemyX[i] >= 736:
                enemyX_change[i] = -4
                enemyY[i] += enemyY_change[i]

            # Collision
            collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
            if (collision):
                explosionSound.play()
                bulletY = 480
                bullet_state = "ready"
                enemy_state[i] = enemy_dead
                enemyX[i] = random.randint(0, 736)
                enemyY[i] = random.randint(50, 150)

            if (enemy_state[i] == enemy_alive):
                draw_enemy(enemyX[i], enemyY[i], i)

        pygame.display.update()


init()
