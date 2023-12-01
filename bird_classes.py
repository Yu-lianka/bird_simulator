import pygame

WIDTH = 800
HEIGTH = 800

img_berry = pygame.image.load('berry.png')
img_berry.convert()
rect = img_berry.get_rect()

img_bird = pygame.image.load('bird.png')
img_bird.convert()
rect = img_bird.get_rect()

class Bird:
    def __init__(self, screen: pygame.Surface, x=WIDTH*0.5, y=HEIGTH*0.5):
        self.screen = screen
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0


    def move(self):
        if self.x > WIDTH:
            self.vx = self.vx * (-1)
        if self.x < 0:
            self.vx = self.vx * (-1)
        self.x += self.vx
        self.y += self.vy
    def hittest(self, obj):
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
        y = self.y = rnd(300, 550)
        color = self.color = BLACK

    def right_ship(self):
        """ Инициализация новых правых шипов. """
        self.live = 1
        x = self.x = 785
        y = self.y = rnd(5, HEIGTH - 5 , 10)
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

    def hit(self, points=1):
        """Попадание птички в шип."""
        self.points += points
   






