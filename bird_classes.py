import pygame

WIDTH = 800
HEIDTH = 800

img_berry = pygame.image.load('berry.png')
img_berry.convert()
rect = img_berry.get_rect()

img_bird = pygame.image.load('bird.png')
img_bird.convert()
rect = img_bird.get_rect()

class Bird:
    def __init__(self, screen: pygame.Surface, x, y):
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


