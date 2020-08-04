import pygame, time, sys, random
from pygame.locals import *

pygame.init()
pygame.font.init()

widht = 700
height = 700

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
grey = (155, 155, 155)

myfont = pygame.font.SysFont(None, 50)

pontos = 0

Display = pygame.display.set_mode((widht,height))
pygame.display.set_caption('Troodon Survival')
clock = pygame.time.Clock()

dinoImg = pygame.image.load('troodon.png')
meteoroIMG = pygame.image.load('meteoro.png')

def meteoros(meteoro_X,Meteoro_Y,meteoroW, meteoroX):
    Display.blit(meteoroIMG,( meteoro_X, Meteoro_Y))
    #pygame.draw.rect(Display, color, [meteoro_X,Meteoro_Y,meteoroW,meteoroX])

dinoWidth = 70
beefWidth = 70

def dino(x, y):
    Display.blit(dinoImg,(x, y))

def main():

    quitar = False
    x = (widht * 0.45)
    y = (height * 0.8)
    x_change = 0
    dino_speed = 0
    
    meteoro_X = random.randrange(0,widht)
    Meteoro_Y = -600
    meteorospeed = 7 
    Meteoro_largura = 70
    Meteoro_altura = 70
    meteoroIMG = pygame.image.load('meteoro.png')

    while not quitar:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitar = True
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -5
            elif event.key == pygame.K_RIGHT:
                x_change = 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_change = 0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                main()


        x += x_change

        Display.fill(grey)
        dino(x, y)

        meteoros(meteoro_X, Meteoro_Y, Meteoro_largura, Meteoro_altura)
        Meteoro_Y += meteorospeed
        dino(x,y)
        Sobrevividos = 0 
        meteorosC = 1

        def meteorosSobrevividos(contagem):
            pontosTXT = myfont.render('Sobrevividos {0}'.format(pontos))
            textrect = pontosTXT.get_rect()
            textrect.x = Display.get_rect().x
            textrect.y = Display.get_rect().y
            pontos.blit(pontosTXT, (5,10))
            pontos += 1

        if Meteoro_Y > height:
            Meteoro_Y = 0 - Meteoro_altura
            meteoro_X = random.randrange(0,widht)
            Sobrevividos += 1
            meteorospeed += 1
            Meteoro_largura += (Sobrevividos * 1.2)

        if Meteoro_Y > height:
            Meteoro_Y = 0 - Meteoro_altura
            meteoro_X = random.randrange(0,widht)

        if y < Meteoro_Y + Meteoro_altura:
            if x > meteoro_X and x < meteoro_X + Meteoro_largura or x + dinoWidth > meteoro_X and x + dinoWidth < meteoro_X + Meteoro_largura:
                quitar = True

        if x > widht - dinoWidth or x < 0:
            quitar = True

        pygame.display.flip()
        clock.tick(120)

main()
pygame.quit()
quit()