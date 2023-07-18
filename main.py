import pygame
import random
from array import *

pygame.init()

def drawStaticBoard() : NotImplemented
def randBoard(): NotImplemented

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 900 
left = 100
right = 500
top = 60
bottom = 860
x = 140
y = 100
l = 40
tickrate = 120
tick = 0
score = 0

clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Detris')
gamespace = pygame.Rect((left,top,right-left,bottom-top))
font = pygame.font.Font(pygame.font.get_default_font(), 36)
block = pygame.Rect((x, y, l, l))
gameboarddata = [ [0]*10 for i in range(20)]

run = True
while run:
    clock.tick(tickrate)
    screen.fill((204, 204, 204))
    drawStaticBoard()

    tick+=1
    if tick == tickrate/2:
        if block.y<bottom-l: block.y+=l
        randBoard()
        drawStaticBoard()
        tick = 0
        
    pygame.draw.rect(screen, (0,0,0), gamespace, 1)
    pygame.draw.rect(screen, (0, 50, 100), block)
    text_surface = font.render('X:'+str(x)+" Y:"+str(y)+" FPS:"+str(round(clock.get_fps())), True, (0, 0, 0))

    for event in pygame.event.get():
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT and x>100: block.x -= l
            elif event.key==pygame.K_RIGHT and x+l<500: block.x += l
            elif event.key == pygame.K_ESCAPE: run = False
    
    screen.blit(text_surface, dest=(0,0))
    pygame.display.flip()
pygame.quit()


#### FUNCTIONS #####
def drawStaticBoard():
    for row, xi in enumerate(gameboarddata):
        for column, yi in enumerate(xi):
            if yi == 1:
                perm = pygame.Rect((column*40+100, row*40+60, l, l))
                pygame.draw.rect(screen, (255, 0, 0), perm)
                #print(str(j)+", ")
def randBoard():
    for row, xi in enumerate(gameboarddata):
            for column, yi in enumerate(xi): xi[column] = random.randint(0,1)

def clearLines():
    for row, xi in enumerate(gameboarddata):
        if xi == [1]*10:
            del xi
            gameboarddata.insert(0, [0]*10)
            score += 100