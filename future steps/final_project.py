import pygame
import random
from sprites import Enemy, Player, Bullet


class Game:
    player = None
    bullet = None
    enemies = []
    running = True
    game_over = False

    def __init__(self, game_name='Space Destroyer', num_of_enemies=6, FPS=60):
        pygame.init()
        self.background = pygame.image.load('assets/img/background/background1.png')
        self.endgame_screen = pygame.image.load('assets/img/background/gameover.png')
        self.clock = pygame.time.Clock()
        self.clock.tick(FPS)
        self.screen = pygame.display.set_mode((800, 600))
        self.num_of_enemies = num_of_enemies
        pygame.display.set_caption(game_name)
        pygame.display.set_icon(pygame.image.load('assets/img/ufo.png'))

    def add_player(self, player: Player):
        self.player = player

    def add_bullet(self, bullet: Bullet):
        self.bullet = bullet

    def add_enemy(self, enemy: Enemy):
        self.enemies.append(enemy)

    def check_collision(self, enemy: Enemy) -> bool:
        return self.bullet.isCollision(enemy)

    def move_sprites(self):
        if self.player:
            self.player.move()
        if self.bullet:
            self.bullet.move()

        for enemy in self.enemies:
            if enemy.move():
                if self.check_collision(enemy):
                    self.bullet.y = 480
                    self.bullet.fired = False
                    enemy.x = random.randint(0, 736)
                    enemy.y = random.randint(50, 150)
            else:
                self.game_over = True

    def event_handling(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.player.X_change = -5
                if event.key == pygame.K_RIGHT:
                    self.player.X_change = 5
                if event.key == pygame.K_SPACE:
                    if not self.bullet.fired:
                        self.bullet.fired = True
                        self.bullet.x = self.player.X

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    self.player.X_change = 0

    def run(self):

        while self.running:

            if self.game_over:
                self.screen.blit(self.endgame_screen, (0, 0))
            else:
                self.screen.blit(self.background, (0, 0))

                self.move_sprites()

            self.event_handling()

            pygame.display.update()


if __name__ == '__main__':

    game = Game()

    game.add_player(Player(game.screen, pygame.image.load('assets/img/player/player1.png')))
    game.add_bullet(Bullet(game.screen, pygame.image.load('assets/img/bullet/bullet1.png')))

    for i in range(game.num_of_enemies):
        game.add_enemy(Enemy(game.screen, pygame.image.load('assets/img/enemy/enemy1.png')))

    game.run()
