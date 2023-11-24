import math
import random
import pygame
import sys

FPS = 30
YELLOW=(255,168,18)
BLUE=(24,255,209)
PURPLE=(116,66,200)
DBLUE=(25,25,112)
RED=(255,83,73)
WHITE=(230,230,250)
GAME_COLORS=[YELLOW,BLUE,PURPLE,DBLUE,RED]

WIDTH = 800
HEIGHT = 800

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("bird_simulator")

finished = False

clock = pygame.time.Clock()

while not finished:
    screen.fill(WHITE)

    pygame.display.flip()

    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
