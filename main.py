import pygame
pygame.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 900
tickrate = 120
tick = 0
x = 100
y = 100
l = 40
clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
font = pygame.font.Font(pygame.font.get_default_font(), 36)



run = True
while run: 

    clock.tick(tickrate)
    screen.fill((204, 204, 204))
    pygame.draw.line(screen, (0,0,0), (100,100), (100, 860) )
    pygame.draw.line(screen, (0,0,0), (500,100), (500, 860) )
    pygame.draw.line(screen, (0,0,0), (100, 860), (500, 860) )
    pygame.draw.line(screen, (0,0,0), (100,100), (500, 100) )
    
    tick+=1
    if tick == tickrate/2: 
        y = y+l
        tick = 0

    pygame.draw.rect(screen, (0, 50, 100), (x, y, l, l))
    text_surface = font.render('X:'+str(x)+" Y:"+str(y)+" FPS:"+str(round(clock.get_fps())), True, (0, 0, 0))


    for event in pygame.event.get():
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT and x>100:
                x -= l
            elif event.key==pygame.K_RIGHT and x+l<500:
                x += l
        if event.type == pygame.QUIT:
            run = False
    
    screen.blit(text_surface, dest=(0,0))
    pygame.display.flip()

pygame.quit()