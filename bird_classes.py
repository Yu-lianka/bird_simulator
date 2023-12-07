import math
from random import choice

import pygame
import random
import time
from random import randrange as rnd

WIDTH = 800
HEIGTH = 800

FPS = 30
YELLOW=(255,168,18)
BLUE=(24,255,209)
PURPLE=(116,66,200)
DBLUE=(25,25,112)
RED=(255,83,73)
BLACK = (0, 0, 0)
WHITE=(230,230,250)
GAME_COLORS=[YELLOW,BLUE,PURPLE,DBLUE,RED]
SPEED=15

SCALE=100



img_berry = pygame.image.load('berry.png')
img_berry.convert()
rect = img_berry.get_rect()

'''img_bird = pygame.image.load('bird.png')
img_bird.convert()
rect = img_bird.get_rect()'''

class Bird:
    def __init__(self, screen: pygame.Surface, x=WIDTH*0.5, y=HEIGTH*0.5):
        '''Создание птички, загрузка изображения'''
        self.screen = screen
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0
        self.ind=1
        self.f=0

        self.BIRD = pygame.image.load('BIRD_1.png').convert_alpha()
        self.BIRD=pygame.transform.scale(self.BIRD,(SCALE*1.3,SCALE))

    def start(self):
        '''Прыжок: вызывается нажатием пробела или при столкновении со стеной'''
        self.vy=-SPEED-2
        self.vx=SPEED*self.ind
        self.x += self.vx
        self.y += self.vy
        
    def move(self):
        '''Перемещение птички, отталкивание от стен'''
        g=2
        self.vx=SPEED*self.ind
        self.y += self.vy
        self.x += self.vx
        self.vy += g
        
        if self.x + SCALE*1.3*0.5 > WIDTH-10:
            self.ind *=(-1)
            self.vy = -SPEED
            self.x-=10
            self.f=1
            
        if self.x - SCALE*1.3*0.5 < 0+10:
            self.ind *=(-1)
            self.vy = -SPEED
            self.x+=10
            self.f=1

    def hittest(self, obj):
        '''Проверка сталкивания с шипами. ЭТУ ФУНКЦИЮ НЕ ТРОГАЛА'''
        if (self.x-obj.x)**2+ (self.y-obj.y)**2<(self.r+obj.r)**2:
            return True
        else:
            return False

    def draw(self):
        '''Вывод птички на экран + отражение при изменении направления движения'''
        if self.f==1:
            self.BIRD=pygame.transform.flip(self.BIRD,1,0)
            self.f=0
            
        screen.blit(self.BIRD,[self.x-SCALE*1.3*0.5,self.y-SCALE*0.5])

    def eat(self, obj):
        if (self.x-obj.x)**2+ (self.y-obj.y)**2<(self.r+obj.r)**2:
            return True
        else:
            return False
 
 
class Ship:
    def __init__(self, screen: pygame.Surface, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.a = 10
        self.points = 0
        self.live = 1
        self.left_ship()
        self.right_ship()

    def left_ship(self):
        """ Инициализация новых левых шипов. """
        self.live = 1
        x = self.x = 5
        y = self.y = rnd(5, HEIGTH - 5 , 10)
        color = self.color = BLACK

    def right_ship(self):
        """ Инициализация новых правых шипов. """
        self.live = 1
        x = self.x = 795
        y = self.y = rnd(5, HEIGTH - 5 , 10)
        color = self.color = BLACK


    def up_ship(self):
        """ Инициализация новых левых шипов. """
        self.live = 1
        x = self.x = rnd(5, WIDTH - 5 , 10)
        y = self.y = 795
        color = self.color = BLACK

    def down_ship(self):
        """ Инициализация новых правых шипов. """
        self.live = 1
        x = self.x = rnd(5, WIDTH - 5 , 10)
        y = self.y = 5
        color = self.color = BLACK

    def draw_left(self):
        pygame.draw.polygon(
            self.screen,
            self.color,
            [(self.x + self.a/(2*math.sqrt(3)), self.y - self.a/2),(self.x - 2 * self.a/(2*math.sqrt(3)), self.y), (self.x + self.a/(2*math.sqrt(3)), self.y + self.a/2 ) ]
        )

    def draw_right(self):
        pygame.draw.polygon(
            self.screen,
            self.color,
            [(self.x - self.a/(2*math.sqrt(3)), self.y - self.a/2),(self.x + 2 * self.a/(2*math.sqrt(3)), self.y), (self.x - self.a/(2*math.sqrt(3)), self.y + self.a/2 ) ]
        )

    def draw_up(self):
        pygame.draw.polygon(
            self.screen,
            self.color,
            [(self.x - self.a/2, self.y + self.a/(2*math.sqrt(3))),(self.x, self.y - self.a/math.sqrt(3)), (self.x + self.a/2, self.y + self.a/2 ) ]
        )

    def draw_down(self):
        pygame.draw.polygon(
            self.screen,
            self.color,
            [(self.x - self.a/2, self.y - self.a/(2*math.sqrt(3))),(self.x, self.y + self.a/math.sqrt(3)), (self.x + self.a/2, self.y - self.a/2 ) ]
        )



    def hit(self, points=1):
        """Попадание птички в шип."""
        self.points += points

class Berry:
    def __init__(self, screen: pygame.Surface):
        '''Создание птички, загрузка изображения'''
        self.screen = screen
        self.x = x = rnd(30, 770)
        self.y = y = rnd(30, 770)
        self.live = 1
        self.f=0
        self.new_berry()

    def new_berry(self):
        """ Инициализация новой. """
        self.live = 1
        x = self.x = rnd(30, 770)
        y = self.y = rnd(30, 770)

    def hit(self, points=1):
        """Съедание ягоды."""
        self.points += points




