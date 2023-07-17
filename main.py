import pygame
pygame.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 900 
left = 100
right = 500
top = 100
bottom = 860
x = 140
y = 140
l = 40
tickrate = 120
tick = 0

clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
gamespace = pygame.Rect((left,top,right-left,bottom-top))
font = pygame.font.Font(pygame.font.get_default_font(), 36)

block = pygame.Rect((x, y, l, l))

run = True
while run:
    clock.tick(tickrate)
    screen.fill((204, 204, 204))
    
    tick+=1
    if tick == tickrate/2: 
        block.y+=l
        tick = 0
    
    pygame.draw.rect(screen, (0,0,0), gamespace)
    pygame.draw.rect(screen, (0, 50, 100), block)

    if pygame.Rect.colliderect(gamespace, block):
        run == False
    
    text_surface = font.render('X:'+str(x)+" Y:"+str(y)+" FPS:"+str(round(clock.get_fps())), True, (0, 0, 0))

    for event in pygame.event.get():
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT and x>100:
                block.x -= l
            elif event.key==pygame.K_RIGHT and x+l<500:
                block.x += l
            elif event.key == pygame.K_ESCAPE:
                run = False
    
    screen.blit(text_surface, dest=(0,0))
    pygame.display.flip()

pygame.quit()