import pygame 

pygame.init()

widht = 800
height = 600

Display = pygame.display.set_mode((widht,height))
pygame.display.set_caption('FUNCIONA P***A')

black = (0, 0, 0)
white = (255, 255, 255)

clock = pygame.time.Clock()
carImg = pygame.image.load('troodon.png')
carWidth = 70

def car(x, y):
    Display.blit(carImg,(x, y))

def loop():

    crashed = False
    x = (widht * 0.45)
    y = (height *0.8)
    x_change = 0
    car_speed = 0

    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -5
            elif event.key == pygame.K_RIGHT:
                x_change = 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_change = 0

        x += x_change

        Display.fill(white)
        car(x, y)

        if x > widht - carWidth or x < 0:
            crashed = True

        pygame.display.update()
        clock.tick(120)

loop()
pygame.quit()
quit()