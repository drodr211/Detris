import pygame
from array import *
from funcs import *

pygame.init()
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

CLOCK = pygame.time.Clock()
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Detris')
GAMESPACE = pygame.Rect((left,top,right-left,bottom-top))
FONT = pygame.font.Font(pygame.font.get_default_font(), 36)

block = pygame.Rect((x, y, l, l))
gbdata = [ [0]*10 for i in range(20)]

run = True
while run:
    CLOCK.tick(tickrate)
    SCREEN.fill((204, 204, 204))
    
    tick+=1
    if tick == tickrate/2:
        if block.y<bottom-l: block.y+=l
        tick = 0
        
    pygame.draw.rect(SCREEN, (0,0,0), GAMESPACE, 1)
    drawStaticBoard(gbdata, SCREEN, l)
    pygame.draw.rect(SCREEN, (0, 50, 100), block)
    text_surface = FONT.render('X:'+str(x)+" Y:"+str(y)+" FPS:"+str(round(CLOCK.get_fps())), True, (0, 0, 0))

    for event in pygame.event.get():
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT and x>100: block.x -= l
            elif event.key==pygame.K_RIGHT and x+l<500: block.x += l
            elif event.key == pygame.K_ESCAPE: run = False
    
    SCREEN.blit(text_surface, dest=(0,0))
    pygame.display.flip()
pygame.quit()