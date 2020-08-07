import pygame, time, sys, random, os
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

font = pygame.font.SysFont(None,30)

Display = pygame.display.set_mode((widht,height))
pygame.display.set_caption('Troodon Survival')
icon = pygame.image.load('ic1.png')
pygame.display.set_icon(icon)
clock = pygame.time.Clock()
DisplayPontos = (height/10, widht/5)

dinoImg = pygame.image.load('troodon.png')
dinoWidth = 70
meteoroIMG = pygame.image.load('meteoro.png')

def meteoros(meteoro_X,Meteoro_Y,meteoroW, meteoroX):
    Display.blit(meteoroIMG,( meteoro_X, Meteoro_Y))
    #pygame.draw.rect(Display, color, [meteoro_X,Meteoro_Y,meteoroW,meteoroX]

def dino(x, y):
    Display.blit(dinoImg,(x, y))

def morreu():
    textMorreu = font.render('Extinto' 
    'Fez Pontos : ' + str(pontos), True, (white))
    Display.blit(textMorreu, (DisplayPontos))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        

def main():

    pontos = 0
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

        x += x_change

        Display.fill(grey)
        textPontos = font.render('Pontos : ' + str(pontos), True, (white))
        Display.blit(textPontos, (DisplayPontos))
        dino(x, y)

        meteoros(meteoro_X, Meteoro_Y, Meteoro_largura, Meteoro_altura)
        Meteoro_Y += meteorospeed
        dino(x,y)

        if Meteoro_Y > height:
            Meteoro_Y = 0 - Meteoro_altura
            meteoro_X = random.randrange(0,widht)
            pontos += 1
            meteorospeed += 1

        if y < Meteoro_Y + Meteoro_altura:
            if x > meteoro_X and x < meteoro_X + Meteoro_largura or x + dinoWidth > meteoro_X and x + dinoWidth < meteoro_X + Meteoro_largura:
                morreu = True
                quitar = True

        if x > widht - dinoWidth or x < 0:
            morreu = True
            quitar = True

        pygame.display.flip()
        clock.tick(120)

main()
pygame.quit()
quit()