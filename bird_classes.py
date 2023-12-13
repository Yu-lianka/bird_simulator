import math
import random as rnd
import pygame
import time


FPS = 30
YELLOW=(255,168,18)
BLUE=(178,182,235)
PURPLE=(116,66,200)
DBLUE=(25,25,112)
RED=(255,83,73)
WHITE=(230,230,250)
MYBLUE=(226,224,249)

DGREY=(66,60,99)
GREY=(162,162,208)

GAME_COLORS=[YELLOW,BLUE,PURPLE,DBLUE,RED]
SPEED=15

SCALE=200

WIDTH = 800
HEIGHT = 800



img_berry = pygame.image.load('berry.png')
img_berry.convert()
rect = img_berry.get_rect()

'''img_bird = pygame.image.load('bird.png')
img_bird.convert()
rect = img_bird.get_rect()'''

class Bird:
    def __init__(self, screen: pygame.Surface, bird, x=WIDTH*0.5, y=HEIGHT*0.5):
        '''Создание птички, загрузка изображения'''
        self.screen = screen
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0
        self.ind=1
        self.f=0
        self.live=1
        self.r=0
        self.R=SCALE*1.3*0.5
        self.BIRD=bird




    def start(self):
        '''Прыжок: вызывается нажатием пробела или при столкновении со стеной'''
        if self.live==1:
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
        
        if self.x + SCALE*1.3*0.5 > WIDTH-10 and self.live==1:
            self.ind *=(-1)
            self.vy = -SPEED
            self.x-=10
            self.f=1
            self.r=1
           
            
        if self.x - SCALE*1.3*0.5 < 0+10 and self.live==1:
            self.ind *=(-1)
            self.vy = -SPEED
            self.x+=10
            self.f=1
            self.r=0

    def hittest(self, obj):
        '''Проверка сталкивания с шипами на стенах'''

        if (obj.x + obj.a/(2*math.sqrt(3))+60 > self.x-self.R and \
           obj.x + obj.a/(2*math.sqrt(3)) < self.x+self.R and \
           obj.y+1 > self.y-SCALE*0.5 and \
           obj.y-1 < self.y+SCALE*0.5 and obj.a<0) or \
           (obj.x - obj.a/(2*math.sqrt(3))+60 > self.x-self.R and \
           obj.x - obj.a/(2*math.sqrt(3)) < self.x+self.R and \
           obj.y+1 > self.y-SCALE*0.5 and \
           obj.y-1 < self.y+SCALE*0.5 and obj.a>0):
            return True
        else:
            return False

    def hit_bottom (self):
        '''if (obj.y-obj.a/math.sqrt(3)<self.y+SCALE*0.5 and obj.a>0) or \
        (obj.y-obj.a/math.sqrt(3)>self.y-SCALE*0.5 and obj.a<0):'''
        if self.y+SCALE*0.5>HEIGHT-40 or self.y-SCALE*0.5<40:
            return True
        else:
            return False

    #def hit (self):
        

    def draw(self):
        '''Вывод птички на экран + отражение при изменении направления движения'''
        if self.f==1:
            self.BIRD=pygame.transform.flip(self.BIRD,1,0)
            self.f=0
            
        screen.blit(self.BIRD,[self.x-SCALE*1.3*0.5,self.y-SCALE*0.5])
 
class Spike:
    def __init__(self, screen: pygame.Surface, x,a):
        '''Иниацилизация шипов'''
        self.screen = screen
        self.x = x
        self.y =rnd.randint(64,HEIGHT-64)
        self.a = a
        self.points = 0
        self.live = 1
        self.color = DBLUE
        self.vy=5*rnd.uniform(-1,1)

        
    def new_spike(self, x):
        self.y=rnd.randint(64,HEIGHT-64)
        self.x=x

    def move(self):
        '''Движение шипов по вертикали '''
        
        self.y+=self.vy


        if self.y+self.a/2>HEIGHT-5:
            self.vy*=-1
            self.y-=5

        elif self.y - abs(self.a)/2<5:
            self.vy*=-1
            self.y+=5

    def appear(self):
        '''Появление шипов (выползание из-за стены) '''
        if self.a<0:
            if self.x<26:
                self.x+=10
        else:
            if self.x>790-24:
                self.x-=10


    def draw_down(self,y):
        self.y=y
        pygame.draw.polygon(
            self.screen,
            self.color,
            [(self.x - self.a/2, self.y + self.a/(2*math.sqrt(3))),
             (self.x, self.y - self.a/math.sqrt(3)),
             (self.x + self.a/2, self.y + self.a/(2*math.sqrt(3))) ]
        )



    def draw(self):
        '''Прорисовка шипов'''

        pygame.draw.polygon(
            screen,
            self.color,
            [(self.x + self.a/(2*math.sqrt(3)), self.y - self.a/2),
             (self.x - 2 * self.a/(2*math.sqrt(3)), self.y),
             (self.x + self.a/(2*math.sqrt(3)), self.y + self.a/2 ) ]
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




