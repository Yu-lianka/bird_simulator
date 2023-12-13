import math
import random as rnd
import pygame
import sys

from bird_classes import *

FPS = 30
MyGREEN=(58,107,56)
DRED=(127,24,13)
RED = 0xFF0000
BLUE = 0x0000FF
YELLOW = 0xFFC91F
GREEN = 0x00FF00
MAGENTA = 0xFF03B8
CYAN = 0x00FFCC
BLACK = (0, 0, 0)
WHITE = 0xFFFFFF
GREY = 0x7D7D7D
GAME_COLORS = [YELLOW, GREEN, MAGENTA, CYAN]

WIDTH = 800
HEIGHT = 600
POINTS = 0
LIFE=5




pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("bird_simulator")

BIRD_1 = pygame.image.load('BIRD_1.png').convert_alpha()
BIRD_1=pygame.transform.scale(BIRD_1,(SCALE*1.3,SCALE))

BIRD_2 = pygame.image.load('BIRD_2.png').convert_alpha()
BIRD_2 =pygame.transform.scale(BIRD_2,(SCALE*1.3,SCALE))
BIRD_2=pygame.transform.flip(BIRD_2,1,0)

chosen = False

BACK=WHITE





s=0
spikes=[]
spimove=[]
bottom=[]
r = 1
m=0

finished = False
chosen = False
clock = pygame.time.Clock()

screen.fill(WHITE)
pygame.draw.line(screen, DBLUE, [0, 0], [0, HEIGHT], 32)
pygame.draw.line(screen, DBLUE, [WIDTH, 0], [WIDTH, HEIGHT], 32)

#Выбор персонажа
while not chosen:
    pygame.display.flip()
    Mouse_x, Mouse_y = pygame.mouse.get_pos()
    if Mouse_x>75 and Mouse_x<325 and Mouse_y>275 and Mouse_y<525:
        mycol1=YELLOW
        mycol2=BLUE
    elif Mouse_x>475 and Mouse_x<725 and Mouse_y>275 and Mouse_y<550:
        mycol1=BLUE
        mycol2=PURPLE
    else:
        mycol1=mycol2=BLUE
    for X in range(48,816,64):
        spd=Spike(screen, X, 64)
        spd.draw_down(HEIGHT-spd.a/(2*math.sqrt(3)))
        spu=Spike(screen, X, -64)
        spu.draw_down(abs(spu.a)/(2*math.sqrt(3)))
        bottom.append(spd)
        bottom.append(spu)
        
    pygame.draw.circle(screen, (mycol1), (200, 400), 150)
    pygame.draw.circle(screen, (mycol2), (600, 400), 150)
    pygame.draw.circle(screen, (BLUE), (200, 400), 170, 10)
    pygame.draw.circle(screen, (BLUE), (600, 400), 170, 10)
    screen.blit(BIRD_1,[200-SCALE*1.3*0.5,400-SCALE*0.5])
    screen.blit(BIRD_2,[600-SCALE*1.3*0.5,400-SCALE*0.5])
    
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if Mouse_x<400:
                SCALE=100
                BIRD_1=pygame.transform.scale(BIRD_1,(SCALE*1.3,SCALE))
                BIRD=BIRD_1
                chosen = True
            elif Mouse_x>400:
                SCALE=100
                BIRD_2 =pygame.transform.scale(BIRD_2,(SCALE*1.3,SCALE))
                BIRD=BIRD_2
                chosen = True
bird=Bird(screen, BIRD)
                
while not finished:
    
    screen.fill(BACK)
    


            

    if chosen == True:
        pygame.draw.circle(screen, (BLUE), (WIDTH*0.5, HEIGHT*0.5), 280, 16)
        pygame.draw.circle(screen, (BLUE), (WIDTH*0.5, HEIGHT*0.5), 250)

    
    text = ' {score:n}'
    font = pygame.font.SysFont(None,550)

    img=font.render(text.format(score=s),True,BACK)
    pos = img.get_rect(center=(WIDTH//2-59, HEIGHT//2+10))

    screen.blit(img,pos)


    
    bird.draw()

    for X in range(48,816,64):
        spd=Spike(screen, X, 64)
        spd.draw_down(HEIGHT-spd.a/(2*math.sqrt(3)))
        spu=Spike(screen, X, -64)
        spu.draw_down(abs(spu.a)/(2*math.sqrt(3)))
        bottom.append(spd)
        bottom.append(spu)
    
    pygame.draw.line(screen, DBLUE, [0, 0], [0, HEIGHT], 32)
    pygame.draw.line(screen, DBLUE, [WIDTH, 0], [WIDTH, HEIGHT], 32)



    if bird.r==1 and r==1 :
       
        spikes=[]
        spimove=[]
        if s<=5:
            n=s
        else:
            n=rnd.randint(1,5)
            z=rnd.randint(0,1)
        for i in range (n):
            z=rnd.randint(0,1)
            spike=Spike(screen, -100+32,-75)
            if z==0 or s<=5:
                spikes.append(spike)
            elif z==1 and s>5:
                spimove.append(spike)
        for j in range (m):
            spike=Spike(screen, -100+32,-75)
            spimove.append(spike)
        r=0
        s+=1

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
            spike=Spike(screen, WIDTH+5+100,75)
            if z==0 or s<=5:
                spikes.append(spike)
            elif z==1 and s>5:
                spimove.append(spike)
        for j in range (m):
            spike=Spike(screen, WIDTH+5+100,75)
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
            BACK=GREY

            #bird.hit

    for j in spimove:
        if bird.hittest(j):
            bird.live=0
            SPEED=0
            bird.vx=0
            bird.vy=30
            BACK=GREY

            #bird.hit()

    if bird.hit_bottom():
        bird.live=0
        SPEED=0
        bird.vx=0
        bird.vy=30
        BACK=GREY


    if bird.live==0 and bird.y>800:
        s=0
        spikes=[]
        spimove=[]
        bird.live=1
        bird.x=WIDTH*0.5
        bird.y=HEIGHT*0.5
        bird.draw()
        BACK=WHITE

        SPEED=15
        
pygame.quit()
