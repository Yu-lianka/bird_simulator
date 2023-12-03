import math
import random
import pygame
import sys

from bird_classes import *

FPS = 30
YELLOW=(255,168,18)
BLUE=(24,255,209)
PURPLE=(116,66,200)
DBLUE=(25,25,112)
RED=(255,83,73)
WHITE=(230,230,250)
GAME_COLORS=[YELLOW,BLUE,PURPLE,DBLUE,RED]
SPEED=15

SCALE=100

WIDTH = 800
HEIGHT = 800




pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("bird_simulator")
s=0



finished = False

clock = pygame.time.Clock()
bird=Bird(screen)
berry=Berry(screen)

while not finished:
    screen.fill(WHITE)
    bird.draw()
    pygame.display.update()

    if s==1:
        bird.move()

    

    clock.tick(FPS)
    
    keys = pygame.key.get_pressed()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

        elif keys[pygame.K_SPACE] and s==0:
            bird.start()
            s+=1
        elif keys[pygame.K_SPACE]:
            bird.start()

    

        bird.move()
        if bird.hittest(berry) and berry.live:
            berry.live = 0
            berry.hit()
            berry.new_berry()

    
            

pygame.quit()
