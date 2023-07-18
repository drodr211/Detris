import pygame
import random

def drawStaticBoard(gbdata, screen, l):
    for row, xi in enumerate(gbdata):
        for column, yi in enumerate(xi):
            if yi == 1:
                perm = pygame.Rect((column*40+100, row*40+60, l, l))
                pygame.draw.rect(screen, (255, 0, 0), perm)
                #print(str(j)+", ")
def randBoard(gbdata):
    for row, xi in enumerate(gbdata):
            for column, yi in enumerate(xi): xi[column] = random.randint(0,1)

def clearLines(gbdata):
    for row, xi in enumerate(gbdata):
        if xi == [1]*10:
            del xi
            gbdata.insert(0, [0]*10)
            score += 100