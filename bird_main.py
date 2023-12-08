import math
import random as rnd
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
spikes=[]
spimove=[]
r = 1
m=0

finished = False

clock = pygame.time.Clock()
bird=Bird(screen)


                
while not finished:
    screen.fill(WHITE)
    bird.draw()

    if bird.r==1 and r==1 :
       
        spikes=[]
        spimove=[]
        if s<=5:
            n=s
        else:
            n=rnd.randint(1,5)
        for i in range (n):
            spike=Spike(screen,-5,-80)
            spikes.append(spike)
        s+=1
        r=0
    elif bird.r==0 and r==0 and s>=1:
        spikes=[]
        spimove=[]
        if s<=5:
            n=s
        else:
            n=rnd.randint(1,5)
            z=rnd.randint(0,1)
        for i in range (n):
            z=rnd.randint(0,1)
            spike=Spike(screen,805,80)
            if z==0 or s<=5:
                spikes.append(spike)
            elif z==1 and s>5:
                spimove.append(spike)
        for j in range (m):
            spike=Spike(screen,805,80)
            spimove.append(spike)
        r=1
        s+=1
            
    for i in spikes:
        i.draw()
        i.appear()
    for j in spimove:
        j.draw()
        j.appear()
        j.move()
    
    pygame.display.update()


    if s>0:
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

    for i in spikes:
        if bird.hittest(i):
            bird.live=0
            SPEED=0
            bird.vx=0
            bird.vy=30

    for j in spimove:
        if bird.hittest(j):
            bird.live=0
            SPEED=0
            bird.vx=0
            bird.vy=30

    if bird.live==0 and bird.y>800:
        s=0
        spikes=[]
        spimove=[]
        bird.live=1
        bird.x=WIDTH*0.5
        bird.y=HEIGHT*0.5
        bird.draw()
        SPEED=15
        
pygame.quit()

