import math
import random


class Sprite:
    X_change = 0
    Y_change = 10

    def __init__(self, screen_driver, sprite):
        self.screen = screen_driver
        self.sprite = sprite

    def blit(self, *args):
        self.screen.blit(self.sprite, *args)


class Bullet(Sprite):
    fired = False
    x, y = (0, 480)

    def move(self):
        if self.fired:
            self.blit((self.x + 16, self.y + 10), )
            self.y -= self.Y_change
        self.try_reload_bullet()

    def try_reload_bullet(self):
        if self.y <= 0:
            self.y = 480
            self.fired = False

    def isCollision(self, enemy) -> bool:
        distance = math.sqrt(math.pow(enemy.x - self.x, 2) + (math.pow(enemy.y - self.y, 2)))
        return distance < 27


class Player(Sprite):
    X, Y = (370, 480)

    def move(self):
        self.X += self.X_change
        if self.X <= 0:
            self.X = 0
        elif self.X >= 736:
            self.X = 736
        self.blit((self.X, self.Y), )


class Enemy(Sprite):
    x, y = (0, 0)
    X_change = 4
    Y_change = 40

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.x = random.randint(0, 736)
        self.y = random.randint(50, 150)

    def move(self):
        if self.y > 444:
            self.y = 2000
            return False

        self.x += self.X_change
        if self.x <= 0:
            self.X_change = 4
            self.y += self.Y_change
        elif self.x >= 736:
            self.X_change = -4
            self.y += self.Y_change
        self.blit((self.x, self.y), )
        return True
