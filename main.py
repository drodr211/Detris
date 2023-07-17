import pygame
pygame.init()

w = 600
h = 900
x = 100
y = 100
l = 40
screen = pygame.display.set_mode((w, h))
font = pygame.font.Font(pygame.font.get_default_font(), 36)

tick = 0

run = True
while run: 

    pygame.time.Clock().tick(60)
    screen.fill((204, 204, 204))
    
    tick+=1
    if tick == 60: 
        y= y+l
        tick = 0
    
    pygame.draw.rect(screen, (0, 50, 100), (x, y, l, l))
    pygame.draw.line(screen, (0,0,0), (100,100), (100, 860) )
    pygame.draw.line(screen, (0,0,0), (500,100), (500, 860) )
    pygame.draw.line(screen, (0,0,0), (100, 860), (500, 860) )
    pygame.draw.line(screen, (0,0,0), (100,100), (500, 100) )
    text_surface = font.render('X:'+str(x)+"Y:"+str(y), True, (0, 0, 0))


    for event in pygame.event.get():
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT and x>100:
                x -= 20
            elif event.key==pygame.K_RIGHT and x+l<500:
                x += 20
        if event.type == pygame.QUIT:
            run = False
    
    screen.blit(text_surface, dest=(0,0))
    pygame.display.flip()

pygame.quit()