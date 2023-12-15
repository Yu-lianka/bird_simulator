import math
import random as rnd
import pygame

from bird_const import *

      


class Bird:
    def __init__(self, screen: pygame.Surface, bird, x=WIDTH * 0.5, y=HEIGHT * 0.5):
        """Создание птички, загрузка изображения"""
        print(HEIGHT, WIDTH)
        self.screen = screen
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0
        self.ind = 1
        self.f = 0
        self.live = 1
        self.r = 0
        self.R = SCALE * 1.3 * 0.25
        self.BIRD = bird

    def start(self):
        """Прыжок: вызывается нажатием пробела или при столкновении со стеной"""
        if self.live == 1:
            self.vy = -SPEED - 2
            self.vx = SPEED * self.ind
            self.x += self.vx
            self.y += self.vy

    def move(self):
        """Перемещение птички, отталкивание от стен"""
        g = 2
        self.vx = SPEED * self.ind
        self.y += self.vy
        self.x += self.vx
        self.vy += g

        if self.x + SCALE * 1.3 * 0.25 > WIDTH - 10 and self.live == 1:
            self.ind *= (-1)
            self.vy = -SPEED
            self.x -= 10
            self.f = 1
            self.r = 1

        if self.x - SCALE * 1.3 * 0.25 < 0 + 10 and self.live == 1:
            self.ind *= (-1)
            self.vy = -SPEED
            self.x += 10
            self.f = 1
            self.r = 0

    def hittest(self, obj):
        """Проверка сталкивания с шипами на стенах"""

        return ((obj.x + obj.a / (2 * math.sqrt(3)) + 60 > self.x - self.R and 
                 obj.x + obj.a / (2 * math.sqrt(3)) < self.x + self.R and 
                 obj.y + 1 > self.y - SCALE * 0.25 and 
                 obj.y - 1 < self.y + SCALE * 0.25 and obj.a < 0) or 
                (obj.x - obj.a / (2 * math.sqrt(3)) + 60 > self.x - self.R and 
                 obj.x - obj.a / (2 * math.sqrt(3)) < self.x + self.R and 
                 obj.y + 1 > self.y - SCALE * 0.25 and 
                 obj.y - 1 < self.y + SCALE * 0.25 and obj.a > 0))
        
    def berry_hittest(self, obj):
        """проверка столкновения ягоды и птички"""
        
        return (self.x - obj.x)**2 + (self.y- obj.y)**2 < (self.R + obj.R)**2

    def hit_bottom(self):
        return self.y + SCALE * 0.25 > HEIGHT - 40 or self.y - SCALE * 0.25 < 40

    def draw(self):
        """Вывод птички на экран + отражение при изменении направления движения"""
        if self.f == 1:
            self.BIRD = pygame.transform.flip(self.BIRD, 1, 0)
            self.f = 0

        self.screen.blit(self.BIRD, [self.x - SCALE * 1.3 * 0.25, self.y - SCALE * 0.25])


class Spike:
    def __init__(self, screen: pygame.Surface, x, a):
        """Иниацилизация шипов"""
        self.screen = screen
        self.x = x
        self.y = rnd.randint(64, HEIGHT - 64)
        self.a = a
        self.points = 0
        self.live = 1
        self.color = DBLUE
        self.vy = 5 * rnd.uniform(-1, 1)

    def new_spike(self, x):
        self.y = rnd.randint(64, HEIGHT - 64)
        self.x = x

    def move(self):
        pass

    def appear(self):
        """Появление шипов (выползание из-за стены) """
        if self.a < 0:
            if self.x < 26:
                self.x += 10
        else:
            if self.x > 790 - 24:
                self.x -= 10

    def draw_down(self, y):
        self.y = y
        pygame.draw.polygon(
            self.screen,
            self.color,
            [(self.x - self.a / 2, self.y + self.a / (2 * math.sqrt(3))),
             (self.x, self.y - self.a / math.sqrt(3)),
             (self.x + self.a / 2, self.y + self.a / (2 * math.sqrt(3)))]
        )

    def draw(self):
        """Прорисовка шипов"""

        pygame.draw.polygon(
            self.screen,
            self.color,
            [(self.x + self.a / (2 * math.sqrt(3)), self.y - self.a / 2),
             (self.x - 2 * self.a / (2 * math.sqrt(3)), self.y),
             (self.x + self.a / (2 * math.sqrt(3)), self.y + self.a / 2)]
        )

    def hit(self, points=1):
        """Попадание птички в шип."""
        self.points += points
        
class Moving_Spike(Spike):
    def move(self):
        """Движение шипов по вертикали """

        self.y += self.vy

        if self.y + self.a / 2 > HEIGHT - 5:
            self.vy *= -1
            self.y -= 5

        elif self.y - abs(self.a) / 2 < 5:
            self.vy *= -1
            self.y += 5

class Berry:
    def __init__(self, screen: pygame.Surface):
        """Создание ягоды, загрузка изображения"""
        self.screen = screen
        self.x = x = rnd.randint(100, 700)
        self.y = y = rnd.randint(130, 670)
        self.live = 1
        self.k = 0 #number of eaten berries
        self.R = SCALE*0.1
        self.BERRY = pygame.image.load('pictures/RED_BERRIES.png').convert_alpha()
        self.BERRY = pygame.transform.scale(self.BERRY, (SCALE*0.5, SCALE*0.5))
        self.BERRY = pygame.transform.flip(self.BERRY, 1, 0)
        
    def draw(self):
        """draw berry"""

        self.screen.blit(self.BERRY, [self.x - SCALE * 1.3 * 0.25, self.y - SCALE * 0.25])
        
